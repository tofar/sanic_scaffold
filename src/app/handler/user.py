# -*- coding: utf-8 -*-

from pymongo import ReturnDocument
from app.model.db import DBModel
from app.util.regex import match_mail
from app.model.log import Logger
import bcrypt
import jwt
import bson
from config import CONFIG
# collection为user的数据表
user = DBModel("user").collection
user_logger = Logger(dir_name="handler/user", file_name="app.handler.user")


def login(email, pw):
    if match_mail(email) is None:
        return {"successful": False, "error": "email is invalid."}
    item = user.find_one(filter={"email": email})

    # 核对密码是否正确
    if bcrypt.checkpw(pw.encode("utf-8"), item.get("pw")) is False:
        user_logger.error("password is invalid")
        return {"successful": False, "error": "password is invalid."}

    token = jwt.encode(
        {
            "user_id": str(item["_id"]),
            "email": item["email"],
            "auth": True
        },
        key=CONFIG.JWT_SECRET,
        algorithm=CONFIG.JWT_ALGORITHM)
    # 删除相应字段
    item.pop("pw")
    item.pop("_id")
    return {"successful": True, "data": {"token": token, "user_info": item}}


def register(email, pw, nickname):
    if match_mail(email) is None:
        return {"successful": False, "error": "email is invalid."}
    # if match_pw(pw) is None:
    #     return {"successful": False, "error": "password is invalid."}
    if not nickname:
        user_logger.error("empty nickname")
        return {"successful": False, "error": "empty nickname."}

    email_list = [email]
    pw = bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt())
    print(email_list)
    print(email)
    print(pw)
    print(nickname)
    result = user.insert_one({
        "email": email,
        "pw": pw,
        "nickname": nickname,
        "email_list": email_list
    })
    print(result.inserted_id)
    return {"successful": True}


def add_email(user_id, email):
    if not user_id:
        user_logger.error("user is invalid")
        return {"successful": False, "error": "user is invalid."}
    if match_mail(email) is None:
        user_logger.error("email is invalid")
        return {"successful": False, "error": "email is invalid."}
    email_list = user.find_one_and_update(
        {
            "_id": bson.ObjectId(user_id)
        }, {"$push": {
            "email_list": email
        }},
        projection={"email_list": True},
        return_document=ReturnDocument.AFTER)
    return {
        "successful": True,
        "data": {
            "email_list": email_list["email_list"]
        }
    }
