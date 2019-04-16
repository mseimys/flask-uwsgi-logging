import atexit
import queue
import logging
import logging.config
from logging.handlers import QueueHandler, QueueListener


def add_queuehandler():
    log_queue = queue.Queue(-1)
    queue_handler = QueueHandler(log_queue)

    logger = logging.getLogger()
    logger.addHandler(queue_handler)

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("QQ: %(threadName)s: %(message)s")
    console_handler.setFormatter(formatter)

    listener = QueueListener(log_queue, console_handler)
    listener.start()

    atexit.register(listener.stop)


DEFAULT_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "class": "logging.Formatter",
            "format": "CUSTOM %(asctime)s [%(levelname)s] %(name)s: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "WARNING",
            "formatter": "default",
            "mode": "a",
            "maxBytes": 500000,
            "backupCount": 5,
            "filename": "myapp.log",
        },
    },
    "root": {"level": "DEBUG", "handlers": ["console", "file"]},
}


def setup_logging():
    logging.config.dictConfig(DEFAULT_LOGGING)
    add_queuehandler()
