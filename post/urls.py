from django.urls import path
from .views import\
    hello_world_view, date_view, blog_view, post_detail, create_comment


urlpatterns = [
    path("hello", hello_world_view),
    path("date/", date_view),
    path("", blog_view),
    path("<int:pk>/", post_detail, name="post-detail"),
    path("<int:pk>/comment/", create_comment),
]
