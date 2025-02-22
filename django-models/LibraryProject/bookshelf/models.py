from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author =models.CharField(max_length=100 ,null=False)
    publication_year = models.IntegerField(null=False)

