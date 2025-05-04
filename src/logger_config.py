# src/logger_config.py
import logging

def setup_logger(log_filename="log_analise_facial.log"):
    with open(log_filename, "w"):  # Limpa o arquivo
        pass

    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)