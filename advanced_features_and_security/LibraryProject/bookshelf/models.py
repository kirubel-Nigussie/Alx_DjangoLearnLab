from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

# class Book(models.Model):
#     title = models.CharField(max_length=200, null=False)
#     author =models.CharField(max_length=100 ,null=False)
#     publication_year = models.IntegerField(null=False)

class CustomUser(AbstractUser):

  email = models.EmailField(unique=True, max_length=256)
  username = models.CharField(unique=False, max_length=100)
  date_of_birth = models.DateField(),
  profile_photo = models.ImageField(),


  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []


  objects = CustomUserManager()

