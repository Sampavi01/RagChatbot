"""
logger.py
---------
Provides a reusable logger setup for RagBot 2.0 server modules.
Configures a console logger with timestamp, log level, and message formatting.
"""

import logging

def setup_logger(name="ragbot"):
    """
    Set up and return a logger with the specified name.

    Args:
        name (str): Name of the logger. Defaults to "ragbot".

    Returns:
        logging.Logger: Configured logger instance with console output and formatting.
    """
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler
    ch=logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # formatter
    formatter=logging.Formatter("[%(asctime)s] [%(levelname)s] -  %(message)s ")
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(ch)
    return logger

logger=setup_logger()