
from flask import Blueprint

from app.services.menuservice import *
menu_index = Blueprint('menu_index', __name__)

@menu_index.route('/platos', methods=['GET'])
def verMenu():
    return get_platos()

