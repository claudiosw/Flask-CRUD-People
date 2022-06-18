
from .adapter.request_adapter import request_adapter
from .composer.registry_person_composer import registry_person_composer
from .composer.delete_person_composer import delete_person_composer
from .composer.find_person_composer import find_person_composer
from .composer.update_person_composer import update_person_composer
from flask import Blueprint, request, jsonify
person_routes_bp = Blueprint("api_routes", __name__)


@person_routes_bp.route("/person", methods=["POST"])
def registry_person():
    http_response = request_adapter(request, registry_person_composer())
    return jsonify(http_response.body), http_response.status_code


@person_routes_bp.route("/person", methods=["GET"])
def find_person():
    http_response = request_adapter(request, find_person_composer())
    return jsonify(http_response.body), http_response.status_code


@person_routes_bp.route("/person", methods=["PUT"])
def update_person():
    http_response = request_adapter(request, update_person_composer())
    return jsonify(http_response.body), http_response.status_code


@person_routes_bp.route("/person", methods=["DELETE"])
def delete_person():
    http_response = request_adapter(request, delete_person_composer())
    return jsonify(http_response.body), http_response.status_code
