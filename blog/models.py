from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    full_text = models.TextField()
    author = models.CharField(max_length=50, default='')
    source = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=50)
    pubdate = models.DateTimeField()
    # is_published = models.BooleanField() #TODO
    # slug = models.CharField(max_length=255) #TODO

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
