
from .adapter.request_adapter import request_adapter
from .composer.person_composer import person_composer, find_person_composer
from flask import Blueprint, request, jsonify
person_routes_bp = Blueprint("api_routes", __name__)


@person_routes_bp.route("/person", methods=["POST"])
def person():
    http_response = request_adapter(request, person_composer())
    return jsonify(http_response.body), http_response.status_code


@person_routes_bp.route("/person", methods=["GET"])
def find_person():
    http_response = request_adapter(request, find_person_composer())
    return jsonify(http_response.body), http_response.status_code
