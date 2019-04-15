import logging

from flask import Blueprint

api = Blueprint("api", __name__)

log = logging.getLogger(__name__)


@api.route("/pages/", defaults={"page": "index"})
@api.route("/pages/<page>")
def show(page):
    print("STDOUT HERE I COME")
    log.error("PAGE ERROR")
    log.warning("PAGE WARNING")
    log.info("PAGE INFO")
    if page == "0":
        raise Exception("Bad idea")
    return f"THIS IS PAGE {page}"
