import logging

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Verifică dacă logger-ul are deja handler-e
    if not logger.hasHandlers():
        consol_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f"{name}.log")

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        consol_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(consol_handler)

    logger.propagate = False
    return logger
