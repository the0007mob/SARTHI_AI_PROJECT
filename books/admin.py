from django.contrib import admin
from books.models import *

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Country)
admin.site.register(Book)
