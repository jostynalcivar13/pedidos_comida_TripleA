from flask import Blueprint

from app.services.menuservice import *
order_index = Blueprint('order_index', __name__)

@order_index.route('/order', methods=['POST'])
def create_order():
    return post_order()

