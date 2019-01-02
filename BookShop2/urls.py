"""BookShop2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views
from books.controllers.login import *
from books.controllers.booklist import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', log_in, name='home'),
    path('books/', list_books, name="books"), # views.BookList.as_view() for api view(json object)
    path('cart', views.CartView.as_view(),name="cart"),
    path('login/',log_in,name="login"),
     path('logout/',log_out, name='logout'),
    path('add/', views.AddToCart.as_view(),name="addbook"),
]
