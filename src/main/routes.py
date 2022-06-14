
from src.main.adapter.request_adapter import request_adapter
from src.main.composer.person_composer import person_composer
from flask import Blueprint, request, jsonify
person_routes_bp = Blueprint("api_routes", __name__)


@person_routes_bp.route("/person", methods=["POST"])
def person():
    http_response = request_adapter(request, person_composer())
    return jsonify(http_response.body), http_response.status_code
