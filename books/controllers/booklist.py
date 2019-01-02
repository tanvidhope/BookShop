import json

from django.http import HttpResponse
from django.shortcuts import render

from books.views import BookList


def list_books(request, **kwargs):
    if request.method=='GET':
        query_set_json = BookList().get(request)
        print (query_set_json)
        return HttpResponse(query_set_json)
        #return render(request,'book.html',{'booklist':query_set_json})
    else:
        pass


