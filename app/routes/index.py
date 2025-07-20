from flask import Blueprint
from app.utils.auth import require_api_key 
from app.services.service import *
index = Blueprint('index', __name__)


@index.route("/")
def home():
    return retornomenu()

