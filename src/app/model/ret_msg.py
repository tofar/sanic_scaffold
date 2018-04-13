# -*- coding:utf-8 -*-
"""

    app.model.res_msg
    返回消息

"""


class RetMessage(object):
    """
        返回消息
    """
    NO_ERROR = "成功"
    PW_ERROR = "密码错误失效"
    LACK_PARAMS = "参数缺失"
    PARAMS_INVALID = "参数无效"
    SERVER_ERROR = "服务出错"
