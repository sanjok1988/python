from django.shortcuts import render
from .models import Post
from category.models import Category
# Create your views here.
def index(request):
	posts = Post.objects.all()
	print(posts)
	return render(request, "posts/index.html", {'posts':posts})