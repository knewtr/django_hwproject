from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog/photo", blank=True, null=True, verbose_name="Превью(изображение)"
    )
    created_at = models.DateField(
        verbose_name="Дата создания записи", blank=True, null=True
    )
    is_published = models.BooleanField(verbose_name="Статус", blank=True, null=True)
    view_count = models.IntegerField(verbose_name="Количество просмотров")

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"