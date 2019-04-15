from logger import setup_logging

setup_logging()

from flask import Flask
from flask.logging import default_handler
from api import api


def create_app():
    app = Flask(__name__)
    app.logger.removeHandler(default_handler)
    app.register_blueprint(api, url_prefix="/api")

    @app.route("/")
    def index():
        app.logger.warning("INDEX WARNING")
        app.logger.info("INDEX INFO")
        return "Hello"

    @app.route("/error")
    def error():
        app.logger.warning("ERR-PAGE WARNING")
        app.logger.info("ERR-PAGE INFO")
        a = 1 / 0
        return str(a)

    app.logger.error("INIT ERROR")
    app.logger.warning("INIT WARNING")
    app.logger.info("INIT INFO")

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
