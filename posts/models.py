from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField
    excerpt = models.TextField
    content = models.TextField
    publish_date = models.DateTimeField('date published')
