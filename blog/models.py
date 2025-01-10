from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog/photo", blank=True, null=True, verbose_name="Изображение"
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания записи"
    )
    is_published = models.BooleanField(verbose_name="Статус", default=True)
    view_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров", default=0
    )

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"

    def __str__(self):
        return self.title
