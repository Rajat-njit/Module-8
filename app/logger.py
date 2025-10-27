# app/logger.py
import logging
from pathlib import Path


class AppLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppLogger, cls).__new__(cls)
            cls._instance._setup()
        return cls._instance

    def _setup(self):
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / "app.log"

        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False  # prevent pytest from capturing

        # remove old handlers
        for h in list(self.logger.handlers):
            self.logger.removeHandler(h)

        fh = logging.FileHandler(log_file, mode="a", encoding="utf-8", delay=False)
        fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        fh.setLevel(logging.INFO)

        if not log_file.exists(): 
            log_file.touch()    # pragma: no cover

        self.logger.addHandler(fh)
        self.logger.info("Logger initialized.")
        fh.flush()

    def get_logger(self):
        return self.logger


# ✅ make sure this line is here and flush-left
logger = AppLogger().get_logger()
