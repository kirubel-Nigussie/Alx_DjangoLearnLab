from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView



def book_list(request):
    books = Book.objects.all() 
    context = {'books' : books}
    return render(request,"relationship_app/list_books.html", context)


class BookDetailView(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "Libraris"

