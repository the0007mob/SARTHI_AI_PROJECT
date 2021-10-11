from django.conf.urls import url
from django.urls import include

from books.views import get_books_from_api

app_name = 'api'


urlpatterns = [
    url(r'^external-books/$', get_books_from_api, name='external-books'),
    url('^v1/', include('books.api.v1.urls'), name='books'),
    ]
