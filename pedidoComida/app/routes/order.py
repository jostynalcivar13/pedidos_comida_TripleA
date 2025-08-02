from flask import Blueprint
from app.utils.auth import require_api_key 
from app.services.menuservice import *
order_index = Blueprint('order_index', __name__)

@order_index.route('/order', methods=['POST'])
@require_api_key
def create_order():
    return post_order()

