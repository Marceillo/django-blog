from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    # to filter the posts with the status of Publisher
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"
    #queryset = Post.objects.all().order_by("created_on")
    #queryset = Post.objects.all().order_by("-created_on") reverses the order
    #queryset = Post.objects.filter(author=2)
     # template_name = "post_list.html"


