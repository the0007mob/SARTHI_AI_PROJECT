from django_filters.rest_framework import FilterSet, CharFilter, NumberFilter

from books.models import Book


class BooksFilter(FilterSet):
    """
    Custom filter for filtering on Book model.
    """
    name = CharFilter(field_name='name')
    publisher = CharFilter(field_name='publisher', lookup_expr='name')
    release_date = NumberFilter(field_name='released_date', lookup_expr='year')

    class Meta:
        model = Book
        fields = ['name']
