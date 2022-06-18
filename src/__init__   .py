from flask import Flask


def create_app():
    """ Construct the core application """
    app = Flask(__name__)

    with app.app_context():
        from src.main.routes import person_routes_bp
        app.register_blueprint(person_routes_bp)
        return app
