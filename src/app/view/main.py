# -*- coding: utf-8 -*-

from sanic import Blueprint
from sanic.response import json
from app.handler.user import login
main = Blueprint("main")


@main.route("/health", methods=["GET"])
async def health(request):
    return json({"successful": True, "data": "healthy"})


@main.route("/login", methods=["POST"])
async def login(request):
    data = request.json
    result = login(data.get("email", ""), data.get("pw", ""))
    if result.get("successful", False):
        return json({"successful": result.get("successful", False)})
    else:
        return json({
            "successful": result.get("successful", False),
            "data": {
                "token": result.get("token")
            }
        })
