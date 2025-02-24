from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path




def list_books(request):
    books = Book.objects.all() 
    context = {'books' : books}
    return render(request,"relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "Libraris"


class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html' 

# class LoginView():
#     pass   

# class LogoutView():
#     pass

# urlpatterns = [
#     path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
# ]  

# urlpatterns = [
#     path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
# ]



