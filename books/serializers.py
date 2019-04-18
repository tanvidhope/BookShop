from django.contrib.auth.models import User
from rest_framework import serializers

from books.models import Book, Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name','author','cost')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('books',)
