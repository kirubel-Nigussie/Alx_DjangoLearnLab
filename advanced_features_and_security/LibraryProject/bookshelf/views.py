from logging import raiseExceptions
from django.shortcuts import render
from .models import Book

def book_list(request):
  books = Book.objects.all() 
  
  context = {
    'Book' : "books"
  }
  if  request.user.has_perm('bookshelf.can_create'):
     return render(request, "index,html", context)  
  else:
    raiseExceptions("invalid book ")
