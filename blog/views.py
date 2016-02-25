from django.shortcuts import render
from .models import Post
from .models import Teg

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})
