from typing import Type
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controllers.interface.registry_person_interface import RegistryPersonInterface
from src.validators.person_validator import person_validator
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.errors.handle_errors import handle_errors


class RegistryPersonView(ViewInterface):
    def __init__(self, controller: Type[RegistryPersonInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        try:
            body = http_request.body
            validation_result = person_validator.validate(body)
            if validation_result:
                response = self.__controller.run(body)
            else:
                raise HttpUnprocessableEntityError(person_validator.errors)

            return HttpResponse(status_code=200, body={"response": response})
        except Exception as exception:
            error = handle_errors(exception)
            return HttpResponse(status_code=error['status_code'], body={"response": error['data']})
