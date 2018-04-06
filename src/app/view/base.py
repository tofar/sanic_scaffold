# -*- coding: utf-8 -*-

from functools import wraps
from sanic.response import json
from config import CONFIG

import jwt


def authorized():
    def decorator(func):
        @wraps(func)
        async def decorated_function(request, *args, **kwargs):
            # run some method that checks the request
            # for the client's authorization status
            token = request.token
            payload = jwt.decode(
                token, CONFIG.JWT_SECRET, algorithms=[CONFIG.JWT_ALGORITHM])
            if payload.get("auth", False):
                # the user is authorized.
                # run the handler method and return the response
                print("auth ok")
                response = await func(request, payload, *args, **kwargs)
                return response
            else:
                # the user is not authorized.
                return json({'status': 'not_authorized'}, 403)

        return decorated_function

    return decorator
