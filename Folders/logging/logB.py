import logging

logging.basicConfig(level=logging.DEBUG, filename="log.txt", format="[%(asctime)s %(levelname)-8s] %(message)s", datefmt="%D %H:%M:%S")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")