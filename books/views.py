from .models import Book
from django.shortcuts import render, redirect
from .forms import BookForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def book_list(request):
    # GET method - retrieve the list of books
    books = Book.objects.all()
    form = BookForm()

    # POST method - handle form submission to add a new book
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = BookForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return render(request, 'books_list.html', {'books': books, 'form': form})