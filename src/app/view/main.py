# -*- coding: utf-8 -*-

from sanic import Blueprint
from sanic.response import json
from app.handler.user import login
from app.handler.user import register
from app.handler.user import add_email
from app.view.base import authorized
main = Blueprint("main")


@main.route("/health", methods=["GET"])
async def health(request):
    return json({"successful": True, "data": "healthy"})


@main.route("/login", methods=["POST"])
async def login_view(request):
    data = request.json
    result = login(data.get("email", ""), data.get("pw", ""))
    return json(result)


@main.route("/register", methods=["POST"])
async def register_view(request):
    data = request.json
    result = register(
        data.get("email", ""), data.get("pw", ""), data.get("nickname", ""))
    return json(result)


@main.route("/user/add_email", methods=["POST"])
@authorized()
async def add_email_view(request, payload):
    data = request.json
    result = add_email(payload.get("user_id", ""), data.get("email", ""))
    return json(result)