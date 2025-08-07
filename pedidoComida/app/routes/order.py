from flask import Blueprint, request
from app.utils.auth import require_api_key
from app.services.menuservice import *
import logging

order_index = Blueprint('order_index', __name__)
logger = logging.getLogger("restaurant-api")

@order_index.route('/order', methods=['POST'])
@require_api_key
def create_order():
    try:
        order_data = request.get_json()
        
        logger.info("Creating new order", extra={
            'event': 'order_create_start',
            'endpoint': '/order',
            'order_items': len(order_data.get('items', [])) if order_data else 0,
            'order_total': order_data.get('total') if order_data else None
        })
        
        result = post_order()
        
        logger.info("Order created successfully", extra={
            'event': 'order_create_success',
            'endpoint': '/order',
            'order_id': result.get('order_id') if isinstance(result, dict) else None
        })
        
        return result
        
    except Exception as e:
        logger.error("Error creating order", extra={
            'event': 'order_create_error',
            'endpoint': '/order',
            'error': str(e),
            'error_type': type(e).__name__
        })
        raise
