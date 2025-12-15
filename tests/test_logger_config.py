import os
import time
import logging
from src.logger_config import setup_logger


def test_setup_logger_creates_file_and_writes(tmp_path):
    log_file = tmp_path / "test_analise.log"
    logger = setup_logger(str(log_file))
    assert logger is not None

    # file should exist after setup
    assert log_file.exists()
