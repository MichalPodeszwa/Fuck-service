import os
from . import config


def config_init():
    config.MONGO_URL = os.environ.get("MONGO_URL", None)
    config.DEBUG = os.environ.get("DEBUG", False)
