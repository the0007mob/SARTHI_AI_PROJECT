from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from books.api.v1.views import BooksViewSet

router = DefaultRouter()
router.register(r'books', BooksViewSet, base_name='books')

urlpatterns = [
    url(r'^', include(router.urls)),

]