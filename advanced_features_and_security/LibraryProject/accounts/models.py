from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email required')
        email = self.normalize_email(email)
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
    """Custom user model extending AbstractUser"""
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    username = None  
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "date_of_birth"]

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set", 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",  
        blank=True
    )

    def __str__(self):
        return self.email