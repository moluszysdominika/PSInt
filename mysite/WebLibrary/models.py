from django.db import models

# Create your models here.
class Reader(models.Model):
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=45)
    region = models.CharField(max_length=100)
    telephone = models.CharField(max_length=45)
    postcode = models.CharField(max_length=45)
    email = models.EmailField()


class Librarian(models.Model):
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)


class Category(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField(max_length=5)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Order(models.Model):
    order_date = models.DateTimeField
    pickup_date = models.DateTimeField
    return_date = models.DateTimeField
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Administrator(models.Model):
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)