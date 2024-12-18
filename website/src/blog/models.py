from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, SET_NULL
from django.template.defaultfilters import title
from django.utils.text import slugify


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ManyToManyField(Categories)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    publish = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    def content_word(self):
        if not self.content:
            return "Le blog ne contient aucun article"
        else:
            article = len(self.content.split())
            return  f"L'article contient f{article} mot(s)"

    def publish_string(self):
        if self.publish:
            return "L'article a ete publier"
        return "L'article n'as pas ete publier"

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
