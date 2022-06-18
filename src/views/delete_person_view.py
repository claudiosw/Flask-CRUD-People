from typing import Type
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controllers.interface.delete_person_interface import DeletePersonInterface


class DeletePersonView(ViewInterface):
    def __init__(self, controller: Type[DeletePersonInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        try:
            query_params = http_request.query_params
            response = self.__controller.run(query_params["name"])

            return HttpResponse(status_code=200, body={"response": response})
        except Exception as exception:
            return HttpResponse(status_code=500, body={"error": str(exception)})
