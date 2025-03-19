from django.urls import path
from .views import register, user_login, user_logout, profile, PostListView, PostDetailView, PostCreateView,PostUpdateView, PostDeleteView
from .views import post_detail, edit_comment, delete_comment, search_posts

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('comment/<int:pk>/edit/', edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete-comment'),
    path('search/', search_posts, name='search-posts'),
]

