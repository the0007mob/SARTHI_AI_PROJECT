from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.api.v1.utils import transform_response
from books.filters import BooksFilter
from books.models import Book
from books.serializers import BookModelSerializer


VALID_FILTERS = {'name', 'country', 'publisher', 'release_date'}


class BooksViewSet(ModelViewSet):
    """
    Viewset based on Book model. Provides create,
    retrieve, update and delete functionality.
    """
    lookup_field = 'pk'
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BooksFilter

    def list(self, request, *args, **kwargs):
        """
        Retrieve list of books with/without query_params.
        """
        if bool(set(request.GET).difference(VALID_FILTERS)):
            return Response(data=transform_response(status="failure", status_code=400,
                                                    data=[], message="Provided query_params are not valid."))
        response = super(BooksViewSet, self).list(request, *args, **kwargs)
        return Response(data=transform_response(status="success", status_code=response.status_code,
                                                data=response.data, message=None))

    def create(self, request, *args, **kwargs):
        """
        Creates new book for arguments passed in POST request.
        """
        response = super(BooksViewSet, self).create(request, *args, **kwargs)
        return Response(data=transform_response(status="success", status_code=response.status_code,
                                                data={'book': response.data}, message=None))

    def update(self, request, *args, **kwargs):
        """
        Updates book instance with arguments passed in PATCH request.
        """
        book_name = self.get_object().name
        response = super(BooksViewSet, self).update(request, *args, **kwargs)
        return Response(data=transform_response(status="success", status_code=response.status_code, data=response.data,
                                                message="The book {} was updated successfully".format(book_name)))

    def destroy(self, request, *args, **kwargs):
        """
        Deletes book for specified id from URL params.
        """
        book_name = self.get_object().name
        response = super(BooksViewSet, self).destroy(request, *args, **kwargs)
        return Response(data=transform_response(status="success", status_code=response.status_code, data=[],
                                                message="The book {} was deleted successfully".format(book_name)))

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves book for specified id from URL params.
        """
        response = super(BooksViewSet, self).retrieve(request, *args, **kwargs)
        return Response(data=transform_response(status="success", status_code=response.status_code,
                                                data={'book': response.data}, message=None))
