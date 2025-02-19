from django.contrib import admin

# Register your models here.
from .models import BlogPost
# premiere facon de faire
# admin.site.register(BlogPost);

#deuxieme facon de faire
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display =(
        "title", "author","date","publish","word_count"
    )

    list_editable = ("publish",)
    empty_value_display ="UNKNOWN"
    search_fields =("title","slug")
    list_filter =("publish", "author")
    autocomplete_fields =("author",)
    list_per_page =50



