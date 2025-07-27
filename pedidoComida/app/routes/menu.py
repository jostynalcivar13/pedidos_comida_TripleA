
from flask import Blueprint
from app.utils.auth import require_api_key
from app.services.menuservice import *
menu_index = Blueprint('menu_index', __name__)

@menu_index.route('/platos', methods=['GET'])
def verMenu():
    return get_platos()


@menu_index.route('/platosGet', methods=['GET'])
def verMenuCurl():
    return get_platosCurl()