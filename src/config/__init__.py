from config.dev import DevConfig
from config.pro import ProdConfig
import os


def load_config(env="dev"):
    configs = {"dev": DevConfig, "pro": ProdConfig}
    return configs[env]


CONFIG = load_config(os.environ.get("WEB_ENV", "dev"))()