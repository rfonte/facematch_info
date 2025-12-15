# src/logger_config.py
import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from typing import Optional


def setup_logger(
    log_filename: str = "log_analise_facial.log",
    level: Optional[int] = None,
    rotation: str = "time",  # 'size' or 'time' (default: time-based rotation)
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    when: str = "midnight",
    interval: int = 1,
) -> logging.Logger:
    """Configure and return a logger with both console and rotating file handlers.

    - `log_filename`: path to the log file.
    - `level`: logging level (e.g. `logging.INFO`). If None, uses env `LOG_LEVEL` or INFO.
    - `max_bytes` / `backup_count`: rotation settings for file handler.
    """
    if level is None:
        lvl = os.environ.get("LOG_LEVEL", "INFO")
        try:
            level = getattr(logging, lvl.upper(), logging.INFO)
        except Exception:
            level = logging.INFO

    # Ensure directory exists
    log_dir = os.path.dirname(os.path.abspath(log_filename))
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("facematch_info")
    logger.setLevel(level)

    # Avoid adding handlers multiple times during repeated setup calls
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # File handler: size-based or time-based rotation
        if rotation == "time":
            file_handler = TimedRotatingFileHandler(log_filename, when=when, interval=interval, backupCount=backup_count)
        else:
            file_handler = RotatingFileHandler(log_filename, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console / stdout handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger