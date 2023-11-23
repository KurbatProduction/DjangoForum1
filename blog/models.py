from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    full_text = models.TextField()
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    pubdate = models.DateTimeField()
    # is_published = models.BooleanField() #TODO
    # slug = models.CharField(max_length=255) #TODO
