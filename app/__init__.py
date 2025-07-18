from flask import Flask


def create_app():
    
    app = Flask(__name__)
    
    from app.routes.index import index

    app.register_blueprint(index)

    return app
