from django.contrib import admin

# Register your models here.
from books.models import Cart, Book

admin.site.register(Cart)
admin.site.register(Book)