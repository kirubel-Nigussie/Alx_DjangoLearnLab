# from django.urls import path
# from .views import list_books, LibraryDetailView , RegisterView , UserLoginView, UserLogoutView


# urlpatterns = [
#     path("books/", view = list_books, name= "book_list"),
#     path("details/", view = LibraryDetailView.as_view(), name="LibraryDetailView"),

#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', UserLoginView.as_view(), name='login'),
#     path('logout/', UserLogoutView.as_view(), name='logout'),
 
 

# ] 

from django.urls import path
from .views import register, user_login, user_logout, admin_view, librarian_view , member_view ,  add_book, edit_book, delete_book

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
     path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
    path('delete-book/', delete_book, name='delete_book'),

]



