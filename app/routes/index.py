from flask import Blueprint

from app.services.service import *
index = Blueprint('index', __name__)


@index.route("/")
def home():
    return retornomenu()

