from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title =models.CharField(max_length=150)
    slug =models.SlugField()
    publish =models.BooleanField(default=False)
    date =models.DateField(blank=True)
    content =models.TextField()
