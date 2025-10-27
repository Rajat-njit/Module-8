import os
import logging
from pathlib import Path
from app.logger import AppLogger, logger

# ----------------------------
# Logger Singleton Tests
# ----------------------------

def test_logger_is_singleton():
    """Ensure multiple instances share the same logger object."""
    logger1 = AppLogger().get_logger()
    logger2 = AppLogger().get_logger()
    assert logger1 is logger2, "Logger instances should be identical (singleton)."


def test_logs_directory_created(tmp_path, monkeypatch):
    """Ensure the logs directory is created automatically."""
    test_dir = tmp_path / "logs"
    monkeypatch.chdir(tmp_path)  # simulate fresh environment

    # Instantiate logger
    AppLogger._instance = None  # reset singleton for this test
    AppLogger()

    assert test_dir.exists(), "logs directory should be auto-created"


def test_log_file_created_and_written(tmp_path, monkeypatch):
    """Ensure a log file is created and messages are written to it."""
    monkeypatch.chdir(tmp_path)
    AppLogger._instance = None  # reset singleton for isolation
    log = AppLogger().get_logger()

    log.info("Test log message")
    log_file = tmp_path / "logs" / "app.log"

    assert log_file.exists(), "Log file should be created"

    contents = log_file.read_text()
    assert "Test log message" in contents, "Log file should contain written message"


def test_log_format_and_level(tmp_path, monkeypatch):
    """Ensure log entries contain timestamp and level."""
    monkeypatch.chdir(tmp_path)
    AppLogger._instance = None  # reset singleton
    log = AppLogger().get_logger()

    log.warning("Format test warning")
    content = (tmp_path / "logs" / "app.log").read_text()

    # Check that the log contains a timestamp-like pattern and level
    assert "[" in content and "]" in content, "Log line should contain timestamp/level format"
    assert "WARNING" in content, "Log line should contain correct log level"
