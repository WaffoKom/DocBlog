from django.urls import path
from .views import BlogIndexView,BlogPostDetailView,blog_post_,blog_post_create


urlpatterns = [
    # path("", blog_posts, name="blog-posts"),
    path("", BlogIndexView.as_view(), name="blog-index"),
    path("test/", blog_post_, name="test"),
    path("article/<str:slug>/", BlogPostDetailView.as_view(), name="blog-post"),
    path("create/", blog_post_create, name="blog-post-create")
]