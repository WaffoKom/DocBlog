from django.urls import path
from .views import BlogIndexView, blog_post, blog_posts,blog_post_


urlpatterns = [
    # path("", blog_posts, name="blog-posts"),
    path("", BlogIndexView.as_view, name="blog-index"),
    path("test/", blog_post_, name="test"),
    path("article/<str:slug>/", blog_post, name="blog-post")
]
