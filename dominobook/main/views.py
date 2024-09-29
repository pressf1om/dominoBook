from django.shortcuts import render
from main.models import Book


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def catalog(request):
    books = Book.objects.all()
    return render(request, 'main/catalog.html', {'books': books})



def gifts(request):
    return render(request, 'main/gifts.html')








