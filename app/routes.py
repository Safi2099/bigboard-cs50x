import logging
from flask import Blueprint, render_template

main = Blueprint("main", __name__)

log = logging.getLogger(__name__)

@main.route("/")
def index():
    log.warning("Example warning message")
    log.debug("Example debug message")
    log.info("Example info message")
    log.error("Example error message")
    log.critical("Example critical message")
    return render_template("index.html")