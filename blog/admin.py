from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "is_published", "view_count")
    search_fields = ("title",)
    list_filter = ("is_published", "created_at")
    ordering = ("-created_at",)
