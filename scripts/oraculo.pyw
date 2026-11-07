"""Ponto de entrada do Oráculo para a tarefa agendada do Windows.

Roda no `pythonw.exe` da instalação base do Python (sem console): o `pythonw.exe` do
venv é só um lançador, que abre um `python.exe` de console e faz o Windows Terminal
mostrar uma aba vazia. O projeto não tem dependências de terceiros, então basta apontar
o `src/` do repositório. Sem console, um erro de partida seria invisível: ele vai para
`data/companion-crash.log`."""

import datetime
import pathlib
import sys
import traceback

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

try:
    from mtg_builder.cli import main
    main(["arena", "companion"] + sys.argv[1:])
except SystemExit as exit_:
    if exit_.code not in (None, 0):
        crash = ROOT / "data" / "companion-crash.log"
        crash.parent.mkdir(parents=True, exist_ok=True)
        with open(crash, "a", encoding="utf-8") as handle:
            handle.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} saída {exit_.code}: {exit_}\n")
    raise
except BaseException:
    crash = ROOT / "data" / "companion-crash.log"
    crash.parent.mkdir(parents=True, exist_ok=True)
    with open(crash, "a", encoding="utf-8") as handle:
        handle.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {sys.executable} cwd={pathlib.Path.cwd()}\n")
        handle.write(traceback.format_exc() + "\n")
    raise
