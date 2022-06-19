from typing import Type
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controllers.interface.find_person_interface import FindPersonInterface
from src.validators.person_name_validator import person_name_validator


class FindPersonView(ViewInterface):
    def __init__(self, controller: Type[FindPersonInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        try:
            query_params = http_request.query_params
            validation_result = person_name_validator.validate(query_params)
            if validation_result:
                response = self.__controller.run(query_params["name"])
                return HttpResponse(status_code=200, body={"response": response})
            else:
                return HttpResponse(status_code=400, body={"error": str(person_name_validator.errors)})
        except Exception as exception:
            return HttpResponse(status_code=500, body={"error": str(exception)})
