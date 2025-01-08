from django.contrib import admin

from blog.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "preview", "created_at", "is_published", "view_count")