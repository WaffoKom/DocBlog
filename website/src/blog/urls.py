from django.urls import path
from .views import blog_post, blog_posts

urlpatterns = [
    path("", blog_post, name="blog_post"),
    path("article/<str:slug>/", blog_posts, name="blog-posts")
]
