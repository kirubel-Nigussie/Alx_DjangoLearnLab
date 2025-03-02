# from django.shortcuts import render
# from django.contrib.auth import login
# # from django.contrib.auth.models.User
# from .models import Book
# from .models import Library
# from django.views.generic.detail import DetailView


# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView

# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import path




# def list_books(request):
#     books = Book.objects.all() 
#     context = {'books' : books}
#     return render(request,"relationship_app/list_books.html", context)


# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = "relationship_app/library_detail.html"
#     context_object_name = "Libraris"


# class RegisterView(CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = 'relationship_app/register.html'
#     success_url = reverse_lazy('login')  # Redirect to login after successful registration

# # Login View (Class-Based)
# class UserLoginView(LoginView):
#     template_name = 'relationship_app/login.html'
#     authentication_form = AuthenticationForm

# # Logout View (Class-Based)
# class UserLogoutView(LogoutView):
#     template_name = 'relationship_app/logout.html'
#     next_page = reverse_lazy('login')  # Redirect to login after logout


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


# 


from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def user_is_admin(user):
    return user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'admin_page.html')

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_page.html')

@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_page.html')


from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return HttpResponse("You have permission to add a book.")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request):
    return HttpResponse("You have permission to edit a book.")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    return HttpResponse("You have permission to delete a book.")



from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return HttpResponse("You have permission to add a book.")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request):
    return HttpResponse("You have permission to edit a book.")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    return HttpResponse("You have permission to delete a book.")


from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('list_books')  # Redirect after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})







''''''''''''''''''''''''''''''''''''''''''''''''
''''''

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

