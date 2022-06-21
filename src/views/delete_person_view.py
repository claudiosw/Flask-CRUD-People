from typing import Type
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controllers.interface.delete_person_interface import DeletePersonInterface
from src.validators.person_name_validator import person_name_validator
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.errors.handle_errors import handle_errors


class DeletePersonView(ViewInterface):
    def __init__(self, controller: Type[DeletePersonInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        try:
            query_params = http_request.query_params
            validation_result = person_name_validator.validate(query_params)
            if validation_result:
                response = self.__controller.run(query_params["name"])
                return HttpResponse(status_code=200, body={"response": response})
            else:
                raise HttpUnprocessableEntityError(person_name_validator.errors)
        except Exception as exception:
            error = handle_errors(exception)
            return HttpResponse(status_code=error['status_code'], body={"response": error['data']})
