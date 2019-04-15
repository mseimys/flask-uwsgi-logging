import logging.config

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
    "root": {"level": "DEBUG", "handlers": ["console"]},
}


def setup_logging():
    logging.config.dictConfig(DEFAULT_LOGGING)

