import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("logC.py")

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")