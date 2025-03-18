from django.db import models

class Post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    author: models.ForeignKey



