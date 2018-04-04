from sanic import Sanic
from app.view.main import main


def configure_blueprints(app):
    blueprints = {main, "/api/v1"}
    for key, value in blueprints:
        app.register_blueprint(key, url_prefix=value)


app = Sanic("myapp")
configure_blueprints(app)
