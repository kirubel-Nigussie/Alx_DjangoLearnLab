from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author =models.CharField(max_length=100 ,null=False)
    publication_year = models.IntegerField(null=False)
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email required')
        User =  self.model(email = self.normalize_email(email))
        User.set_password(password)
        User.save(using = self._db)
        return User
    
    def create_superuser(self, email, password=None):
        User = self.create_user(email, password)

        User.is_staff = True
        User.is_superuser = True
        User.save(using = self._db)

        return User
    
class CustomUser(AbstractUser):

  email = models.EmailField(unique=True, max_length=256)
  username = models.CharField(unique=False, max_length=100)
  date_of_birth = models.DateField(),
  profile_photo = models.ImageField(),


  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []


  objects = CustomUserManager()


  class Meta:
      permissions = [
          ("can_create","can create a bookshelf "),
          ("can_delete", "can delete a bookshelf"),
      ]
      

