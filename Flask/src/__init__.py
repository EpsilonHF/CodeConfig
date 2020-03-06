import os
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
from logging.config import dictConfig


dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
        "loggers": {
            "log.log": {
                "level": "INFO",
                "handlers": ["info_handler", "error_handler"],
                "propagate": 1,
                "qualname": "log.log",
            }
        },
        "handlers": {
            "info_handler": {
                "level": "INFO",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "./logs/log_info.log",
                "when": "midnight",
                "backupCount": 3,
                "formatter": "default",
            },
            "error_handler": {
                "level": "ERROR",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "./logs/log_error.log",
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


def create_app():
    # 初始化应用
    app = Flask(__name__)
    logger = logging.getLogger("radar.log")
    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["60000 per minute", "1000 per second"],
    )

    # 环境配置
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # 注册blueprint
    from src.api.api import model_blueprint

    app.register_blueprint(model_blueprint)

    return app
