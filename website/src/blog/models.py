from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, SET_NULL
from django.template.defaultfilters import title
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ManyToManyField(Categories)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    publish = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = "Article"
        ordering = ['-date', '-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug": self.slug})

    def content_word(self):
        if not self.content:
            return "Le blog ne contient aucun article"
        else:
            word_count = len(self.content.split())
            return f"L'article contient f{word_count} mot(s)"

    def publish_string(self):
        if self.publish:
            return "L'article a ete publier"
        return "L'article n'as pas ete publier"

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def word_count(self):
        return len(self.content.split())
