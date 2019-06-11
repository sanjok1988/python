from django.db import models
from category.models import Category
# Create your models here.
<<<<<<< HEAD
class Post(models.Model):    
=======


class Posts(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
>>>>>>> a6ce8b22a1619803fdcae0bd19f5b0c38b57310e
    title = models.CharField(max_length = 200)
    slug = models.SlugField(default='')
    link = models.URLField(blank = True, null=False)
    excerpt = models.TextField(blank=False, default= '')
    content = models.TextField(blank=False, default= '')
    # image = models.ImageField(default="Null")
    publish_date = models.DateTimeField('date published')
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
