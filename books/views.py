from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})
