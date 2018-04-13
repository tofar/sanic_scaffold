# -*- coding: utf-8 -*-

from sanic import Blueprint
from app.handler.user import login
from app.handler.user import register
from app.handler.user import add_email
from app.view.auth import authorized
from app.util.common import inject_json
from app.util.common import ret_json
from app.model.ret_code import RetCode
from app.model.ret_msg import RetMessage

main = Blueprint("main")


@main.route("/health", methods=["GET"])
async def health(request):
    return ret_json(ret_code=RetCode.NO_ERROR)


@main.route("/login", methods=["POST"])
@inject_json(params=["email", "pw"], can_empty=False)
async def login_view(request, data):
    result = login(data.get("email"), data.get("pw"))
    return result


@main.route("/register", methods=["POST"])
@inject_json(params=["email", "pw", "nickname"], can_empty=False)
async def register_view(request, data):
    result = register(data.get("email"), data.get("pw"), data.get("nickname"))
    return result


@main.route("/user/add_email", methods=["POST"])
@authorized()
async def add_email_view(request, payload):
    data = request.json
    result = add_email(payload.get("user_id"), data.get("email", ""))
    return result