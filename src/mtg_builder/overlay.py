"""Janela flutuante do assistente de draft: sempre no topo, semitransparente, só leitura.

Não desenha sobre a superfície do jogo: é uma janela comum do Windows marcada como
*topmost*. Com o Arena em modo janela ou tela cheia sem bordas ela fica visível; em tela
cheia exclusiva o jogo a cobre. Teclas: Esc fecha, + e - mudam o tamanho da fonte, F move
a janela para o outro canto.

Duas implementações, escolhidas em tempo de execução:

1. tkinter (biblioteca padrão), quando o Python tem o Tcl/Tk instalado;
2. PowerShell + WinForms (`overlay.ps1`), que todo Windows tem: o Python escreve o texto
   em um arquivo temporário e a janela o relê a cada meio segundo. Se o Python parar de
   escrever (Ctrl+C, erro), a janela se fecha sozinha em alguns segundos.
"""

import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

WAITING = "aguardando o log do Arena..."


class CloseWindow(Exception):
    """Levantada por `poll()` para fechar a janela (ex.: o Arena foi fechado)."""


def _point_tcl():
    """Instalações do Python para Windows sem a opção Tcl/Tk no venv: aponta a biblioteca
    do Python base quando ela existe."""
    base = Path(sys.base_prefix) / "tcl"
    for name, env in (("tcl8.6", "TCL_LIBRARY"), ("tk8.6", "TK_LIBRARY")):
        if (base / name).exists():
            os.environ.setdefault(env, str(base / name))


def _run_tk(poll, title, interval_ms, width, height, alpha, font_size):
    _point_tcl()
    import tkinter as tk
    root = tk.Tk()                       # TclError aqui = sem Tcl/Tk; quem chama cai no PowerShell
    root.title(title)
    root.attributes("-topmost", True)
    try:
        root.attributes("-alpha", alpha)
    except tk.TclError:   # pragma: no cover
        pass
    root.configure(bg="#101418")
    screen_w = root.winfo_screenwidth()
    corner = {"right": True}

    def place():
        x = screen_w - width - 16 if corner["right"] else 16
        root.geometry(f"{width}x{height}+{x}+40")

    place()
    size = [font_size]
    text = tk.Text(root, bg="#101418", fg="#e8e8e8", insertbackground="#e8e8e8", font=("Consolas", size[0]),
                   wrap="none", borderwidth=0, padx=8, pady=6, state="disabled")
    text.pack(fill="both", expand=True)

    def show(content):
        text.configure(state="normal")
        text.delete("1.0", "end")
        text.insert("1.0", content)
        text.configure(state="disabled")

    def resize(delta):
        size[0] = max(7, min(18, size[0] + delta))
        text.configure(font=("Consolas", size[0]))

    def flip(_event=None):
        corner["right"] = not corner["right"]
        place()

    def tick():
        try:
            content = poll()
        except CloseWindow:
            root.destroy()
            return
        except Exception as error:       # a janela nunca morre por erro de leitura
            content = f"erro: {error}"
        if content is not None:
            show(content)
        root.after(interval_ms, tick)

    root.bind("<Escape>", lambda _e: root.destroy())
    for key in ("<plus>", "<KP_Add>"):
        root.bind(key, lambda _e: resize(1))
    for key in ("<minus>", "<KP_Subtract>"):
        root.bind(key, lambda _e: resize(-1))
    root.bind("<f>", flip)
    root.bind("<F>", flip)
    show(WAITING)
    root.after(100, tick)
    root.mainloop()


def _write(path, text):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(f"{int(time.time())}\n{text}", encoding="utf-8-sig")
    os.replace(tmp, path)


def _run_powershell(poll, title, interval_ms, width, height, alpha, font_size, log=print):
    script = Path(__file__).parent / "overlay.ps1"
    path = Path(tempfile.gettempdir()) / f"mtg-overlay-{os.getpid()}.txt"
    _write(path, WAITING)
    command = ["powershell", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-STA",
               "-File", str(script), "-Path", str(path), "-Title", title, "-Width", str(width),
               "-Height", str(height), "-Opacity", str(alpha).replace(",", "."), "-FontSize", str(font_size)]
    process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log("janela aberta pelo PowerShell (tkinter indisponível neste Python); feche-a com Esc")
    text = WAITING
    try:
        while process.poll() is None:
            try:
                content = poll()
            except CloseWindow:
                break
            except Exception as error:
                content = f"erro: {error}"
            if content is not None:
                text = content
            _write(path, text)           # também serve de sinal de vida para a janela
            time.sleep(interval_ms / 1000)
    finally:
        if process.poll() is None:
            process.terminate()
        try:
            path.unlink()
        except OSError:
            pass


def run_window(poll, title="Draft", interval_ms=500, width=720, height=760, alpha=0.93, font_size=10, log=print):
    """`poll()` é chamada a cada `interval_ms`; se devolver texto, a janela o mostra.
    Tenta o tkinter e, sem Tcl/Tk, usa a janela em PowerShell."""
    try:
        import tkinter as tk
        try:
            return _run_tk(poll, title, interval_ms, width, height, alpha, font_size)
        except tk.TclError:
            pass
    except ImportError:
        pass
    if sys.platform != "win32":
        raise RuntimeError("tkinter indisponível e a janela em PowerShell só existe no Windows; use o modo terminal")
    return _run_powershell(poll, title, interval_ms, width, height, alpha, font_size, log)
