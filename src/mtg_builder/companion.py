"""Oráculo: companheiro do MTG Arena, como o do Untapped.

Fica em segundo plano esperando o `MTGA.exe`; quando o Arena abre, abre a janela flutuante
(`overlay.py`) e passa a ler o `Player.log`: pacotes de draft viram o ranking do motor de
picks e partidas viram deck, oponente, turnos, vida e resultado. Quando o Arena fecha, a
janela fecha e o Oráculo volta a esperar. Instalado como atalho na pasta Inicializar do
Windows (`mtg arena companion --install`), sobe sozinho a cada login, sem console
(`pythonw.exe`). Registra o que faz em `data/companion.log`.
"""

import logging
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from . import arena_log, arena_match, db, overlay

NAME = "Oráculo"
PROCESS = "MTGA.exe"
LOG_FILE = db.DATA_DIR / "companion.log"
DRAFT_TYPES = {"join", "pack", "pack_and_pick", "pick", "complete", "unknown"}
MATCH_LINES = 30


def arena_running():
    try:
        out = subprocess.run(["tasklist", "/FI", f"IMAGENAME eq {PROCESS}", "/NH"], capture_output=True,
                             text=True, timeout=15, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)).stdout
    except (OSError, subprocess.SubprocessError):
        return False
    return PROCESS.lower() in out.lower()


def classify_all(header, obj):
    """Eventos de draft e de partida no mesmo leitor. O lado do draft devolve "unknown" para
    qualquer linha que cite um evento de draft, inclusive o `EventSetDeckV3` do deck de
    Limitado (visto em 2026-11-09: o registro das partidas ficou com o deck de Ladder
    anterior); essa linha ainda passa pelo classificador de partida."""
    draft = arena_log.classify(header, obj)
    if draft and draft["type"] != "unknown":
        return draft
    return arena_match.classify_match(header, obj) or draft


def compose(state, running=True):
    """Texto da janela: o ranking do draft quando ele é o evento mais recente; senão, a
    visão da partida (mão, campos, cemitérios, exílio, dicas e últimos lances)."""
    stamp = datetime.now().strftime("%H:%M:%S")
    header = f"{NAME} · Arena {'aberto' if running else 'fechado'} · {stamp}"
    if state["draft_text"] and state["draft_at"] >= state["match_at"]:
        return header + "\n\n" + state["draft_text"]
    if state.get("match_text"):
        pre = "\n".join(state["lines"][-4:])
        return header + "\n\n" + (pre + "\n\n" if pre else "") + state["match_text"]
    if state["lines"]:
        return header + "\n\n" + "\n".join(state["lines"][-MATCH_LINES:])
    return header + "\n\naguardando um draft ou uma partida..."


class Session:
    """Uma abertura do Arena: um leitor de log e as duas sessões (draft e partida)."""

    def __init__(self, follower, draft_session, match_session, log, check_every=6):
        self.follower, self.draft, self.match, self.log = follower, draft_session, match_session, log
        self.state = {"lines": [], "draft_text": None, "draft_at": 0.0, "match_at": 0.0}
        self.ticks, self.check_every = 0, check_every

    def handle(self, event):
        now = time.time()
        if event["type"] in DRAFT_TYPES:
            text = self.draft.handle(event)
            if text:
                self.state["draft_text"], self.state["draft_at"] = text, now
                return True
            return False
        line = self.match.handle(event)
        if line:
            if event["type"] != "game_state":
                self.state["lines"].append(datetime.now().strftime("%H:%M:%S ") + line)
            self.state["match_at"] = now
            if event["type"] in ("game_state", "room"):
                self.state["match_text"] = self.match.board()
            return True
        return False

    def poll(self):
        self.ticks += 1
        if self.ticks % self.check_every == 0 and not arena_running():
            raise overlay.CloseWindow
        changed = any([self.handle(event) for event in self.follower.poll()])
        if changed or self.ticks == 1:
            return compose(self.state)
        return None


def run(make_sessions, log, wait_seconds=3, once=False):
    """Laço principal: espera o Arena, abre a janela, espera o Arena fechar, repete.
    `make_sessions()` devolve (sessão de draft, sessão de partida) novas a cada abertura."""
    log.info("%s iniciado (pid %s)", NAME, os.getpid())
    while True:
        while not arena_running():
            time.sleep(wait_seconds)
        log.info("Arena aberto")
        path = arena_log.find_log()
        if path is None:
            log.warning("Player.log não encontrado; tentando de novo em 15 s")
            time.sleep(15)
            continue
        draft_session, match_session = make_sessions()
        follower = arena_log.LogFollower(path, from_start=False, classifier=classify_all)
        session = Session(follower, draft_session, match_session, log)
        try:
            overlay.run_window(session.poll, title=f"{NAME} — MTG Arena", log=log.info)
        except Exception:
            log.exception("erro na janela")
        log.info("janela fechada")
        if once:
            return
        while arena_running():          # fechada com Esc: só reabre quando o Arena reiniciar
            time.sleep(wait_seconds)
        log.info("Arena fechado")


# --- instalação ----------------------------------------------------------------------------
# Tarefa do Agendador do Windows, não atalho nem processo filho: o Windows Terminal e o
# VS Code encerram a árvore inteira de processos quando a aba fecha (foi o que derrubou o
# Oráculo em 2026-11-07), e uma tarefa agendada nasce fora de qualquer terminal. Ela
# dispara no login do usuário e pode ser iniciada e parada à mão.

TASK = "Oraculo - MTG Deck Builder"
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def shortcut_path():
    """Atalho da primeira instalação (pasta Inicializar); removido ao instalar a tarefa."""
    base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    return base / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup" / "Oraculo - MTG Deck Builder.lnk"


LAUNCHER = Path(__file__).resolve().parents[2] / "scripts" / "oraculo.pyw"


def pythonw():
    """`pythonw.exe` da instalação base (sem console). O do venv é um lançador que abre um
    `python.exe` de console, e o Windows Terminal mostra uma aba vazia para ele."""
    for base in (Path(sys.base_prefix), Path(sys.executable).parent):
        exe = base / "pythonw.exe"
        if exe.exists():
            return exe
    return Path(sys.executable)


def command():
    return [str(pythonw()), str(LAUNCHER)]


def task_command():
    cmd = command()
    return f'"{cmd[0]}" {" ".join(cmd[1:])}'


def _run(args, timeout=60):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace",
                          timeout=timeout, creationflags=NO_WINDOW)


def _powershell(script):
    return _run(["powershell", "-NoProfile", "-NonInteractive", "-Command", script])


def task_state():
    """'Ready', 'Running', 'Disabled'... ou None se a tarefa não existe."""
    result = _powershell(f"(Get-ScheduledTask -TaskName '{TASK}' -ErrorAction Stop).State")
    return result.stdout.strip() or None if result.returncode == 0 else None


def _processes():
    """[(pid, pid do pai)] dos processos do Oráculo (menos o processo atual)."""
    # o próprio powershell.exe desta consulta carrega o padrão na linha de comando: fica de fora
    result = _powershell("Get-CimInstance Win32_Process | Where-Object { ($_.CommandLine -like '*oraculo.pyw*' "
                         "-or $_.CommandLine -like '*mtg_builder.cli arena companion*') -and $_.Name -notlike 'powershell*' } "
                         "| ForEach-Object { \"$($_.ProcessId) $($_.ParentProcessId)\" }")
    pairs = []
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) == 2 and all(p.isdigit() for p in parts) and int(parts[0]) != os.getpid():
            pairs.append((int(parts[0]), int(parts[1])))
    return pairs


def running_pids():
    return [pid for pid, _parent in _processes()]


def running_instances():
    """Quantos Oráculos há de fato: o `pythonw.exe` do venv é um lançador que cria o
    `python.exe` filho, e os dois casam com a busca."""
    pairs = _processes()
    pids = {pid for pid, _parent in pairs}
    return sum(1 for _pid, parent in pairs if parent not in pids)


def _failed(result, what):
    return RuntimeError(f"Não consegui {what}: {result.stderr.strip() or result.stdout.strip() or 'erro desconhecido'}")


def install():
    """Cria (ou recria) a tarefa agendada que dispara no login do usuário. Usa os cmdlets
    do PowerShell: `schtasks /SC ONLOGON` exige administrador, `Register-ScheduledTask`
    para o próprio usuário não."""
    cmd = command()
    script = (
        f"$a = New-ScheduledTaskAction -Execute '{cmd[0]}' -Argument '{' '.join(cmd[1:])}'; "
        "$t = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME; "
        "$s = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries "
        "-ExecutionTimeLimit ([TimeSpan]::Zero) -MultipleInstances IgnoreNew; "
        f"Register-ScheduledTask -TaskName '{TASK}' -Action $a -Trigger $t -Settings $s -RunLevel Limited "
        "-Force -ErrorAction Stop | Out-Null"
    )
    result = _powershell(script)
    if result.returncode != 0:
        raise _failed(result, "criar a tarefa agendada")
    link = shortcut_path()
    if link.exists():
        link.unlink()
    return TASK


def start():
    """Inicia a tarefa agora (fora do terminal). Sem a tarefa, levanta RuntimeError."""
    if task_state() is None:
        raise RuntimeError("Tarefa não instalada: rode `mtg arena companion --install`.")
    result = _powershell(f"Start-ScheduledTask -TaskName '{TASK}' -ErrorAction Stop")
    if result.returncode != 0:
        raise _failed(result, "iniciar a tarefa")
    return True


def stop():
    """Encerra a tarefa e qualquer Oráculo iniciado à mão. Devolve quantos processos parou."""
    _powershell(f"Stop-ScheduledTask -TaskName '{TASK}' -ErrorAction SilentlyContinue")
    pids = running_pids()
    for pid in pids:
        _run(["taskkill", "/PID", str(pid), "/F"])
    return len(pids)


def uninstall():
    stop()
    result = _powershell(f"Unregister-ScheduledTask -TaskName '{TASK}' -Confirm:$false -ErrorAction Stop")
    link = shortcut_path()
    if link.exists():
        link.unlink()
    return result.returncode == 0


def configure_logging():
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, encoding="utf-8",
                        format="%(asctime)s %(levelname)s %(message)s")
    return logging.getLogger("companion")
