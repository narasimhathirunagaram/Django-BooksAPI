# books/management/commands/fetch_books.py

import requests
from django.core.management.base import BaseCommand
from books.models import Book  # Adjust the import path based on your project structure

class Command(BaseCommand):
    help = 'Fetches book data from Google Books API and saves it to the database'

    def handle(self, *args, **options):
        api_url = 'https://www.googleapis.com/books/v1/volumes?q=python'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json().get('items', [])

            for item in data:
                volume_info = item.get('volumeInfo', {})
                title = volume_info.get('title', '')
                authors = volume_info.get('authors', [])

                # Create or update the Book model
                book, created = Book.objects.update_or_create(
                    title=title,
                    author=', '.join(authors),
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created book: {book}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated book: {book}'))

        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data from the API. Status code: {response.status_code}'))
