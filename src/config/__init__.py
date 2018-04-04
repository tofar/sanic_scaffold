from config.dev import DevConfig
from config.pro import ProdConfig


def load_config(env="dev"):
    configs = {"dev": DevConfig, "pro": ProdConfig}
    return configs[env]


CONFIG = load_config("dev")()