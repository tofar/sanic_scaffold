# -*- coding : utf-8 -*-

from config.base import BaseConfig


class DevConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        self.DEBUG = True

        # mongo
        self.MONGO_HOST = 'mongo'
        self.MONGO_PORT = 27017
        self.DB_USER = 'user'
        self.DB_PW = 'mongo'
        self.DB_NAME = 'scaffold_for_python'
        # redis
        self.REDIS_HOST = 'localhost'
        self.REDIS_PORT = 6379

        self.LOG_PATH = "/app/log/"
