from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Country(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=256)
    isbn = models.CharField(max_length=20)
    authors = models.ManyToManyField(Author, related_name='authors')
    publisher = models.ForeignKey(Publisher, related_name='publisher', on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    country = models.ForeignKey(Country, related_name='country', on_delete=models.CASCADE)
    released_date = models.DateTimeField()
