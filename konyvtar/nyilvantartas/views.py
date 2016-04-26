from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Book, User, Lending
from datetime import datetime


def index(request):
	latest_lending_list = Lending.objects.order_by('-lending_date')[:10]
	context = {
		'latest_lending_list': latest_lending_list,
	}
	return render(request, 'nyilvantartas/index.html', context)


def lending(request):
	if request.POST and request.POST['book'] and request.POST['user']:# and request.POST['lending_date']:
		user = User.objects.get(pk=request.POST['user'])
		book = Book.objects.get(pk=request.POST['book'])
		if user and book:
			lending = Lending(
				user=user,
				book=book,
				lending_date=datetime.utcnow().isoformat(' ')[:-7]
				#lending_date=request.POST['lending_date']
			)
			lending.save()
		return HttpResponseRedirect(reverse('nyilvantartas:index'))
	else:
		users = User.objects.all()
		books = Book.objects.all()
		context = {
			'users': users,
			'books': books
		}
		return render(request, 'nyilvantartas/lending.html', context)


def detail(request, lending_id):
	lending = Lending.objects.get(pk=lending_id)
	context = {
		'lending': lending,
	}
	return render(request, 'nyilvantartas/detail.html', context)