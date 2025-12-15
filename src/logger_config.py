# src/logger_config.py
import logging
import os
import shutil
from pathlib import Path
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from typing import Optional


def setup_logger(
    log_filename: str = os.path.join("logs", "log_analise_facial.log"),
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

    # Ensure directory exists (top-level logs folder)
    base_log_dir = os.path.dirname(os.path.abspath(log_filename))
    if base_log_dir and not os.path.exists(base_log_dir):
        os.makedirs(base_log_dir, exist_ok=True)

    # Create a daily subdirectory under the base logs directory only when the base dir is 'logs'
    try:
        from datetime import datetime

        if os.path.basename(os.path.normpath(base_log_dir)).lower() == "logs":
            today = datetime.now().strftime("%Y-%m-%d")
            daily_dir = os.path.join(base_log_dir, today)
            os.makedirs(daily_dir, exist_ok=True)
            # update log_filename to point inside the daily directory
            log_filename = os.path.join(daily_dir, os.path.basename(log_filename))
            log_dir = daily_dir
        else:
            log_dir = base_log_dir
    except Exception:
        log_dir = base_log_dir

    # Move existing top-level log files into the logs directory (if any)
    try:
        repo_root = Path(__file__).resolve().parents[1]
        base_name = Path(log_filename).name
        # look for files in repo root that start with the base name (e.g., log_analise_facial.log, log_analise_facial.log.2025-...)
        for p in repo_root.iterdir():
            if p.is_file() and p.name.startswith(base_name) and Path(log_dir).resolve() not in p.resolve().parents:
                dest = Path(log_dir) / p.name
                # avoid overwriting existing file in logs/; add numeric suffix if necessary
                if dest.exists():
                    stem = dest.stem
                    suffix = dest.suffix
                    i = 1
                    while True:
                        candidate = Path(log_dir) / f"{stem}.{i}{suffix}"
                        if not candidate.exists():
                            dest = candidate
                            break
                        i += 1
                shutil.move(str(p), str(dest))
    except Exception:
        # moving logs should not prevent logger setup; ignore errors
        pass

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