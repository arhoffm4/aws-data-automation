import logging
from logging import Logger

def get_logger(name: str = "datamove") -> Logger:
	logger = logging.getLogger(name)
	if logger.handlers:
		return logger
		
	logger.setLevel(logging.INFO)
	handler = logging.StreamHandler()
	fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
	handler.setFormatter(fmt)
	logger.addHandler(handler)
	return logger
