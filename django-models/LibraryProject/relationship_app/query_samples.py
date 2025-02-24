import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # Ensure this matches the expected query
    return books

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Example usage:
if __name__ == "__main__":
    # Replace with actual names present in the database
    print("Books by Author:", list(books_by_author("J.K. Rowling")))
    print("Books in Library:", list(books_in_library("Central Library")))
    print("Librarian of Library:", librarian_of_library("Central Library"))
