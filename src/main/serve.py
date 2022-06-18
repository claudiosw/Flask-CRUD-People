from flask import Flask
from flask_cors import CORS
from .routes import person_routes_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(person_routes_bp)
