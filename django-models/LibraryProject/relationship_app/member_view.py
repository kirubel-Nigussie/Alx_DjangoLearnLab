from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Helper function to check if user is Member
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
