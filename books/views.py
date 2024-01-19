from .models import Book
from django.shortcuts import render, redirect
from .forms import BookForm

def book_list(request):
    # GET method - retrieve the list of books
    books = Book.objects.all()
    form = BookForm()

    # POST method - handle form submission to add a new book
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')

    return render(request, 'books_list.html', {'books': books, 'form': form})