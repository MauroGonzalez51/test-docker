from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    