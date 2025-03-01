from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.ModelAdmin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
admin.site.register(Book , BookAdmin)



class CustomUserAdmin(UserAdmin):
     list_display = ("username", "email")

admin.site.register(CustomUser , CustomUserAdmin)