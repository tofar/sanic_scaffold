# -*- coding: utf-8 -*-

import re

# 以字母开头，长度在6-18之间， 只能包含字符、数字和下划线
pw_pattern = r'^[a-zA-Z]w{5,17}$'
# 由数字/大写字母/小写字母/标点符号组成，四种都必有，8位以上
strict_pw_pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*\W+)(?=.*[A-Z])(?=.*[a-z])(?!.*\n).*$'
# url
url_pattern = r'^(http|https)+://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$'
# 中国手机号匹配
phone_num_pattern = r'^1[3458][0-9]{9}$'
# 中国大陆身份证号(15位或18位)
id_card_pattern = r'\d{15}(\d\d[0-9xX])?'
# 用户昵称的正则匹配, 合法的字符有 0-9, A-Z, a-z, _,  [空格],汉字
# 字符 '_' 只能出现在中间且不能重复, 如 "__"
nickname_pattern = r'^[a-z0-9A-Z \p{Han}]+(_[a-z0-9A-Z\p{Han}]+)*$'
# 用户名的正则匹配, 合法的字符有 0-9, A-Z, a-z, _, [空格]
# 第一个字母不能为 _, 0-9
# 最后一个字母不能为 _, 且 _ 不能连续
name_pattern = r'^[a-zA-Z][a-z0-9A-Z ]*(_[a-z0-9A-Z]+)*$'
# 电子邮箱的正则匹配, 考虑到各个网站的 mail 要求不一样, 这里匹配比较宽松
# 邮箱用户名可以包含 0-9, A-Z, a-z, -, _, .
# 开头字母不能是 -, _, .
# 结尾字母不能是 -, _, .
# -, _, . 这三个连接字母任意两个不能连续, 如不能出现 --, __, .., -_, -., _.
# 邮箱的域名可以包含 0-9, A-Z, a-z, -
# 连接字符 - 只能出现在中间, 不能连续, 如不能 --
# 支持多级域名, x@y.z, x@y.z.w, x@x.y.z.w.e
mail_pattern = r'^[a-z0-9A-Z]+([\-_\.][a-z0-9A-Z]+)*@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)*\.)+[a-zA-Z]+$'


def match_pw(string):
    return re.match(pw_pattern, string)


def match_strict_pw(string):
    return re.match(strict_pw_pattern, string)


def match_url(string):
    return re.match(url_pattern, string)


def match_phone_num(string):
    return re.match(phone_num_pattern, string)


def match_id_card(string):
    return re.match(id_card_pattern, string)


def match_nickname(string):
    return re.match(nickname_pattern, string)


def match_name(string):
    return re.match(name_pattern, string)


def match_mail(string):
    return re.match(mail_pattern, string)
