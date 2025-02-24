from django.urls import path
from .views import list_books, LibraryDetailView , register , LoginView, LogoutView


urlpatterns = [
    path("books/", view = list_books, name= "book_list"),
    path("details/", view = LibraryDetailView.as_view(), name="LibraryDetailView"),

    path('register/', view = register.as_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),


] 