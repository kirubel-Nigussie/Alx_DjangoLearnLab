from django.urls import path
from .views import BookList

urlpatterns = [
    path("BookList/", view= BookList, name= "BookList")
]