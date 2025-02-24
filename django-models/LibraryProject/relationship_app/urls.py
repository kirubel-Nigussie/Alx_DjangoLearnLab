from django.urls import path
from .views import list_books, LibraryDetailView


urlpatterns = [
    path("books/", view = list_books, name= "book_list"),
    path("details/", view = LibraryDetailView.as_view(), name="LibraryDetailView")

] 