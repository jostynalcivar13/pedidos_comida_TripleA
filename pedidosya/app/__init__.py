from flask import Flask


def create_app():
    
    app = Flask(__name__)
    
    from app.routes.index import index
    from app.routes.order import order_index 
    from app.routes.menu import menu_index 
    app.register_blueprint(index)
    app.register_blueprint(order_index)
    app.register_blueprint(menu_index, url_prefix='/api')

    return app
