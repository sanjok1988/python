from django.db import models
from category.models import Category
# Create your models here.


class Posts(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    slug = models.SlugField(default='')
    link = models.URLField(default='')
    excerpt = models.TextField(blank=False, default= '')
    content = models.TextField(blank=False, default= '')
    # image = models.ImageField(default="Null")
    publish_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title
