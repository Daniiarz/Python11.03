from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import BlogPost, Comment


def hello_world_view(request):
    return HttpResponse("Hello, World!")


def date_view(request):
    now = datetime.now()
    return HttpResponse(str(now))


def blog_view(request):
    posts: list = BlogPost.objects.all()
    return render(request, "blog.html", context={"posts": posts})


def post_detail(request, pk):
    post: BlogPost = BlogPost.objects.get(pk=pk)
    comments = Comment.objects.filter(post_id=pk).order_by("-date")
    return render(request, "blog_detail.html", context={"post": post, "comments": comments})


def create_comment(request, pk):
    if request.method == "POST":
        data: dict = request.POST
        post = BlogPost.objects.get(pk=pk)
        comment = Comment.objects.create(text=data["text"], post=post)
        return redirect("post-detail", pk=pk)
