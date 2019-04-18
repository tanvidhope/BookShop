from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    cost = models.IntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
