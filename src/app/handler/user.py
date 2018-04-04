#-*- coding:utf9 -*-

from app.model.db import DBModel

User = DBModel("user")

def login(emai, pw):
    return True