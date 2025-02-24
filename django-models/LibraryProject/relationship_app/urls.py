from django.urls import path
from .views import book_list
from .views import BookDetailView


urlpatterns = [
    path("books/", view = book_list, name= "book_list"),
    path("details/", view = BookDetailView.as_view(), name="BookDetailView")

] 