# -*- coding: utf-8 -*-

from pymongo import ReturnDocument
from app.model.db import DBModel
from app.util.regex import match_mail
from app.model.log import Logger
import bcrypt
import jwt
import bson
from config import CONFIG
from app.util.common import ret_json
from app.model.ret_code import RetCode
from app.model.ret_msg import RetMessage

# collection为user的数据表
user_col = DBModel("user").collection
user_logger = Logger(dir_name="app/handler/user", file_name="app.handler.user")


def login(email, pw):
    if not match_mail(email):
        user_logger.error(RetMessage.LACK_PARAMS)
        return ret_json(
            ret_code=RetCode.LACK_PARAMS, error_msg=RetMessage.LACK_PARAMS)

    item = user_col.find_one(filter={"email": email})

    # 核对密码是否正确
    if not bcrypt.checkpw(pw.encode("utf-8"), item.get("pw")):
        user_logger.error(RetMessage.PW_ERROR)
        return ret_json(
            ret_code=RetCode.PW_ERROR, error_msg=RetMessage.PW_ERROR)

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
    return ret_json(
        ret_code=RetCode.NO_ERROR, data={
            "token": token,
            "user_info": item
        })


def register(email, pw, nickname):
    if not match_mail(email):
        user_logger.error(RetMessage.LACK_PARAMS)
        return ret_json(
            ret_code=RetCode.LACK_PARAMS, error_msg=RetMessage.LACK_PARAMS)
    if not nickname:
        user_logger.error(RetMessage.LACK_PARAMS)
        return ret_json(
            ret_code=RetCode.LACK_PARAMS, error_msg=RetMessage.LACK_PARAMS)

    email_list = [email]
    pw = bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt())
    result = user_col.insert_one({
        "email": email,
        "pw": pw,
        "nickname": nickname,
        "email_list": email_list
    })
    print(result.inserted_id)
    return ret_json(ret_code=RetCode.NO_ERROR)


def add_email(user_id, email):
    if not user_id:
        user_logger.error(RetMessage.LACK_PARAMS)
        return ret_json(
            ret_code=RetCode.LACK_PARAMS, error_msg=RetMessage.LACK_PARAMS)
    if match_mail(email) is None:
        user_logger.error(RetMessage.PARAMS_INVALID)
        return ret_json(
            ret_code=RetCode.PARAMS_INVALID,
            error_msg=RetMessage.PARAMS_INVALID)
    email_list = user_col.find_one_and_update(
        {
            "_id": bson.ObjectId(user_id)
        }, {"$push": {
            "email_list": email
        }},
        projection={"email_list": True},
        return_document=ReturnDocument.AFTER)
    return ret_json(
        ret_code=RetCode.NO_ERROR,
        data={"email_list": email_list["email_list"]})
