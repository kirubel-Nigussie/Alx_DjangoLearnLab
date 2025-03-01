from logging import raiseExceptions
from django.shortcuts import render
from .models import Book
from .forms import ExampleForm

def book_list(request):
  books = Book.objects.all() 
  
  context = {
    'Book' : "books"
  }
  if  request.user.has_perm('bookshelf.can_create'):
     return render(request, "index,html", context)  
  else:
    raiseExceptions("raise_exception")


query = "SELECT * FROM bookshelf_book WHERE title = '%s'" % user_input
books = Book.objects.raw(query)

from django.db.models import Q
from django.shortcuts import render
from .models import Book

def search_books(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, "bookshelf/book_list.html", {"books": books})


def search_books(request):
    form = ExampleForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data["query"]
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none()
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})

