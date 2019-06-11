from django.db import models

# Create your models here.
class Post(models.Model):    
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
    
    
