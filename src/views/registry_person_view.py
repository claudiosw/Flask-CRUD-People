from typing import Type
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controllers.interface.registry_person_interface import RegistryPersonInterface
from src.validators.person_validator import person_validator


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
                return HttpResponse(status_code=400, body={"error": str(person_validator.errors)})

            return HttpResponse(status_code=200, body={"response": response})
        except Exception as exception:
            return HttpResponse(status_code=500, body={"error": str(exception)})
