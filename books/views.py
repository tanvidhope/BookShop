from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from books.forms import UserForm
from books.models import Book, Cart
from books.serializers import BookSerializer, UserSerializer, CartSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer

    def post_save(self,obj, created=False):
        if created:
            cart =Cart(user=obj)
            cart.save()

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user.username)


class BookList(APIView):

    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
        	serializer.save()
        	return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartView(APIView):
    # class CartView(viewsets.ModelViewSet):
    # model = Cart
    # serializer_class = CartSerializer
    def get(self,request):
        # user = authenticate(username=request.username, password=request.password)
        # if request.user.is_authenticated:
        # if user is not None:
        cart = Cart.objects.filter(id=1)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    def post(self):
        pass

    '''''''''''
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def add(self, request,pk):
        return Response({"success":True})

    def pre_save(self, obj):
        obj.user = self.request.user

'''''''''''


class UserApi(APIView):
    def post(self,request):
        json_data = json.loads(request.body)
        if "username" in json_data:
            if "password" in json_data:
                user = authenticate(username=json_data["username"],password=json_data["password"])
                if user is not None:
                    user = User.objects.filter(username=json_data["username"])
                    serializer = UserSerializer(user)
                    return Response({"user": serializer.data,"login":"success"},status=200)
                else:
                    return Response({"login":"fail"},status=401)
            else:
                return Response({"login": "fail"}, status=401)
        else:
            return Response({"login": "fail"}, status=401)

        '''
        def get(request):
            if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
'''


class AddToCart(APIView):
    def post(self,request,pk):
        book = Book.objects.get(id=pk)
        # book = Book.objects.get(pk=id)
        cart = Cart.objects.get(id=1)
        print(cart)
        cart.books.add(book)
        # cart.save()
        # serializer = CartSerializer(cart, many=True)
        # return Response(serializer.data,status=200)

    def get(self,request, pk):
        book = Book.objects.filter(id=pk)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    #def addCartView(self):

