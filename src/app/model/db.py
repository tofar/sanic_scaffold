# -*- coding: utf-8 -*-
"""

    dbOperation.dbModel
    定义Mongo操作

"""

import traceback

from pymongo import MongoClient
from config import CONFIG


class DBModel(object):
    """
        数据库操作
    """

    def __init__(self,
                 col_name,
                 db_name=CONFIG.DB_NAME,
                 host=CONFIG.MONGO_HOST,
                 port=CONFIG.MONGO_PORT):

        self._conn = MongoClient(host, port)

        self._database = self._conn[db_name]
        self.collection = self._database[col_name]
