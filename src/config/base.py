# -*- coding : utf-8 -*-


class BaseConfig(object):
    def __init__(self):

        self.DEBUG = False

        self.JWT_SECRET = 'dfasdfasdfasdfas'
        self.JWT_ALGORITHM = 'HS256'

        self.REDIS_PORT = 6379
        self.DEFAULT_HOST = 'localhost'
