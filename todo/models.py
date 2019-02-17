from django.db import models


class Post(models.Model):
    date = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
