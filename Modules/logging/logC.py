import logging

logger = logging.getLogger("logC.py")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("log.txt")
sh = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s, file_name\"%(name)s\"[%(levelname)-8s]: %(message)s", datefmt="%D-%H:%M:%S")
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)

logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")