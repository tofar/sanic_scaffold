from config.base import BaseConfig


class ProdConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        self.DEBUG = False

        self.SECRET = 'mysecret'

        # mongo
        self.MONGO_HOST = 'mongo'
        self.MONGO_PORT = 27017
        self.DB_USER = 'user'
        self.DB_PW = 'mongo'
        self.DB_NAME = 'scaffold_for_python'
        # redis
        self.REDIS_HOST = 'localhost'
        self.REDIS_PORT = 6379
