from django.shortcuts import render, redirect

from books.models import Cart


def recievecartList(request):
	if request.user.is_authenticated():
		queryset = Cart.objects.filter(user=request.user.username)
		context = {'book_list':queryset}
		return render(request,'cart.html',context)
	else:
		return redirect("/")