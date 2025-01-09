from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)
        return queryset

class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        object = super().get_object()
        object.view_count += 1
        object.save()
        return object

class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "content", "preview", "is_published")
    success_url = reverse_lazy("blog:article_list")


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "content", "preview", "is_published")

    def get_success_url(self):
        return reverse_lazy("blog:article_detail", kwargs={'pk':self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:article_list")
