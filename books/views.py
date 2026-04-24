from django.shortcuts import render, get_object_or_404
from .models import Book

def home(request):
    books = Book.objects.all()
    # Cambia 'home.html' por 'books/home.html'
    return render(request, 'books/home.html', {'books': books})

def detail_book(request, id):
    book = get_object_or_404(Book, id=id)
    # Cambia 'detail_book.html' por 'books/detail_book.html'
    return render(request, 'books/detail_book.html', {'book': book})