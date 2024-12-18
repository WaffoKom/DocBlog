from django.urls import path
from .views import blog_post, blog_posts,blog_post_

urlpatterns = [
    path("", blog_post, name="blog_post"),
    path("test/", blog_post_, name="test"),
    path("article/<str:slug>/", blog_posts, name="blog-posts")
]
