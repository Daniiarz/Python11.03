from datetime import datetime

from django.http import HttpResponse

from .models import BlogPost


def hello_world_view(request):
    return HttpResponse("Hello, World!")


def date_view(request):
    now = datetime.now()
    return HttpResponse(str(now))


def blog_view(request):
    posts: list = BlogPost.objects.all()
    post_info = f"Post tile {posts[0].title} " \
                f"Post description {posts[0].description} " \
                f"Post likes {posts[0].likes} "
    return HttpResponse(post_info)
