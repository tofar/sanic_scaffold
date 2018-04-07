# sanic_scaffold

Running via command

`python -m sanic main.app --host=0.0.0.0 --port=3031 --workers=4`

### 测试过程：

##### 启动服务：

首先cd到项目目录下，之后运行docker-compose

`docker-compose up`

##### 启动nginx（可选）：

+ 在 cd /etc/nginx/sites-avaiable目录下添加 sanic_scaffold.conf
+ 之后在/etc/nginx/sites-enable目录下设置软连接：sudo ln -s ../sites-avaiable/sanic_scaffold.conf sanic_scaffold
+ 重启openresty/nginx，若是openresty则为 sudo openresty -s reload

##### 测试：

+ 测试是否可用：

  `curl -X GET http://localhost/api/v1/health`

  返回：{"successful": True, "data": "healthy"}

+ 测试register：

  `curl -H "Accept: application/json" -H "Content-type: application/json" -X POST http://localhost/api/v1/register -d '{"email": "example@gmail.com", "pw": "123456789", "nickname": "molscar" }'`

  返回：{"successful": True}

+ 测试login:

  `curl -H "Accept: application/json" -H "Content-type: application/json" -X POST http://localhost/api/v1/login -d '{"email": "example@gmail.com", "pw": "123456789" }'`

  返回：{"successful": True, "data": {"token": token, "user_info": {"nickname": nicknaame, "email": email}}}

+ 测试 add_email:

  `curl -H "Accept: application/json" -H "Content-type: application/json" -X POST http://localhost/api/v1/user/add_email -d '{"email": "add_email@gmail.com" }'`

  返回：{ "successful": True, "data":  { "email_list": email_list} }



