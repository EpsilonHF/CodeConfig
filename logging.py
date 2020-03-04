import logging 
from logging.config import dictConfig


# logging config
dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
        "loggers": {
            "log_name.log": {
                "level": "INFO",
                "handlers": ["info_handler", "error_handler"],
                "propagate": 1,
                "qualname": "log_name.log",
            }
        },
        "handlers": {
            "info_handler": {
                "level": "INFO",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "./logs/info.log",
                "when": "midnight",
                "backupCount": 3,
                "formatter": "default",
            },
            "error_handler": {
                "level": "ERROR",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "./logs/error.log",
                "when": "midnight",
                "backupCount": 3,
                "formatter": "detail",
            },
        },
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s: %(message)s",
                "datefmt": "[%Y-%m-%d %H:%M:%S]",
                "class": "logging.Formatter",
            },
            "detail": {
                "format": "[%(asctime)s] %(levelname)s in %(pathname)s %(lineno)s: %(message)s",
                "datefmt": "[%Y-%m-%d %H:%M:%S]",
                "class": "logging.Formatter",
            },
        },
    }
)

logger = logging.getLogger("log_name.log")
