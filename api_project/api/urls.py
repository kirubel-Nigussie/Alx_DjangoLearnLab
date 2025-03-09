from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    # path("BookList/", view= BookList, name= "BookList"),
    path("BookList/",BookList.as_view , name="BookList" ),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]




