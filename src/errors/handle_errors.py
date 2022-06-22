from typing import Type, Dict
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.errors.http_not_found import HttpNotFound


def handle_errors(error: Type[Exception]) -> Dict:
    """ Handler to treat Exception cases
    :param - error: Exception
    :return - Dict with data and status_code
    """
    if isinstance(error, HttpUnprocessableEntityError):
        return {
            "data": {"error": error.message},
            "status_code": error.status_code
        }
    elif isinstance(error, HttpNotFound):
        return {
            "data": {"error": error.message},
            "status_code": error.status_code
        }
    else:
        return {
            "data": {"error": str(error)},
            "status_code": 500
        }
