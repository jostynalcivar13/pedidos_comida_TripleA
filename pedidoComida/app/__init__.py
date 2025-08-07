from flask import Flask, request, g
import time
from config.logging_config import setup_graylog_logger

def create_app():
    
    app = Flask(__name__)
    logger = setup_graylog_logger("restaurant-api")
    @app.before_request
    def before_request():
        g.start_time = time.time()
        g.request_id = request.headers.get('X-Request-ID', f"req_{int(time.time())}")
        
        logger.info("Request started", extra={
            'event': 'request_start',
            'method': request.method,
            'path': request.path,
            'remote_addr': request.remote_addr,
            'user_agent': request.headers.get('User-Agent'),
            'request_id': g.request_id
        })
    

    @app.after_request
    def after_request(response):
        duration = time.time() - g.start_time
        
        logger.info("Request completed", extra={
            'event': 'request_end',
            'method': request.method,
            'path': request.path,
            'status_code': response.status_code,
            'duration_ms': round(duration * 1000, 2),
            'request_id': g.request_id
        })
        
        return response
    from app.routes.index import index
    from app.routes.order import order_index 
    from app.routes.menu import menu_index 
    app.register_blueprint(index)
    app.register_blueprint(order_index)
    app.register_blueprint(menu_index, url_prefix='/api')

    return app
