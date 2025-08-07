from flask import Blueprint, current_app
from app.utils.auth import require_api_key
from app.services.menuservice import *
import logging

menu_index = Blueprint('menu_index', __name__)
logger = logging.getLogger("restaurant-api")

@menu_index.route('/platos', methods=['GET'])
def verMenu():
    try:
        logger.info("Getting menu items", extra={
            'event': 'menu_request',
            'endpoint': '/platos'
        })
        
        result = get_platos()
        
        logger.info("Menu items retrieved successfully", extra={
            'event': 'menu_success',
            'endpoint': '/platos',
            'items_count': len(result) if isinstance(result, list) else None
        })
        
        return result
        
    except Exception as e:
        logger.error("Error retrieving menu items", extra={
            'event': 'menu_error',
            'endpoint': '/platos',
            'error': str(e),
            'error_type': type(e).__name__
        })
        raise
@menu_index.route('/platosGet', methods=['GET'])
def verMenuCurl():
    return get_platosCurl()