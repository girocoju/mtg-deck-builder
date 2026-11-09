import logging
from pathlib import Path

import pytest

from mtg_builder import arena_log, arena_match, companion, overlay
from test_arena_log import H, fake_arena_db, make_pick, notify, room  # noqa: F401
from test_decks import conn  # noqa: F401


class FakeDraft:
    def __init__(self):
        self.seen = []

    def handle(self, event):
        self.seen.append(event["type"])
        return f"ranking P{event['pack']}" if event["type"] == "pack" else None


def test_combined_classifier_routes_draft_and_match_events(conn, tmp_path, monkeypatch):  # noqa: F811
    path = tmp_path / "Player.log"
    path.write_text("DETAILED LOGS: ENABLED\n", encoding="utf-8")
    follower = arena_log.LogFollower(path, classifier=companion.classify_all)
    arena_path = tmp_path / "Raw_CardDatabase_x.mtga"
    fake_arena_db(arena_path)
    draft, match = FakeDraft(), arena_match.MatchSession(conn, arena_log.ArenaCards(arena_path))
    session = companion.Session(follower, draft, match, logging.getLogger("t"), check_every=1000)
    first = session.poll()
    assert first.startswith(companion.NAME) and "aguardando" in first
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(room("Playing") + "\n")
    text = session.poll()
    assert "partida em Ladder" in text and session.poll() is None          # nada novo: None
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(notify(1, 1, [101, 102]) + "\n" + make_pick(1, 1, 101) + "\n")
    text = session.poll()
    assert draft.seen == ["pack", "pick"] and "ranking P1" in text and "partida em" not in text
    monkeypatch.setattr(companion, "arena_running", lambda: False)
    session.check_every = 1
    with pytest.raises(overlay.CloseWindow):
        session.poll()


def test_task_and_command_shapes(tmp_path, monkeypatch):
    monkeypatch.setenv("APPDATA", str(tmp_path))
    link = companion.shortcut_path()
    assert link.parent == tmp_path / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
    cmd = companion.command()
    assert Path(cmd[0]).name == "pythonw.exe" and Path(cmd[1]).name == "oraculo.pyw" and Path(cmd[1]).exists()
    assert companion.task_command().endswith("oraculo.pyw") and companion.TASK
    calls = []
    ok = type("R", (), {"returncode": 0, "stdout": "", "stderr": ""})()
    monkeypatch.setattr(companion, "_run", lambda args, timeout=60: calls.append(args) or ok)
    monkeypatch.setattr(companion, "_powershell", lambda script: calls.append(script) or ok)
    monkeypatch.setattr(companion, "task_state", lambda: "Ready")
    monkeypatch.setattr(companion, "running_pids", lambda: [4242])
    assert companion.install() == companion.TASK and "Register-ScheduledTask" in calls[-1] and "-AtLogOn" in calls[-1]
    assert companion.start() is True and calls[-1].startswith("Start-ScheduledTask")
    assert companion.stop() == 1 and calls[-1] == ["taskkill", "/PID", "4242", "/F"]
    assert companion.uninstall() is True and calls[-1].startswith("Unregister-ScheduledTask")
