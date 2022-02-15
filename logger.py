from loguru import logger

logger.add("logger/debug.log", format="{time} {level} {message}",
level="DEBUG", rotation="1024 MB", compression="zip")

for _ in range(1000000):
    logger.debug("Hello, World (debug)!")
    logger.info("Hello, World (info)!")
    logger.error("Hello, World (error)!")