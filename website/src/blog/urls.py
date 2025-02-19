from django.urls import path
from .views import (BlogIndexView,BlogPostDetailView,blog_post_,blog_post_create,
                    BlogPostCreateView,BlogPostUpdateView, BlogPostDeleteView)


urlpatterns = [
    # path("", blog_posts, name="blog-posts"),
    path("", BlogIndexView.as_view(), name="blog-index"),
    path("test/", blog_post_, name="test"),
    path("create/", BlogPostCreateView.as_view(), name="blog-post-create"),
    path("article/<str:slug>/", BlogPostDetailView.as_view(), name="blog-post"),
    path("article/<str:slug>/edit", BlogPostUpdateView.as_view(), name="blog-post-edit"),
    path("article/<str:slug>/delete", BlogPostDeleteView.as_view(), name="blog-post-delete")

]