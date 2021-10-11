from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.ice_and_fire_api import IceAndFireAPI


@api_view()
def get_books_from_api(request):
    """
    Retrieve book/books from Fire and Ice API.
    """
    ice_and_fire_api = IceAndFireAPI()
    books_from_api = ice_and_fire_api.get_books(request.GET)
    return Response({"status_code": 200,
                     "status": "success",
                     "data": books_from_api})
