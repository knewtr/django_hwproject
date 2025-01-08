from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from blog.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog: article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog: article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog: article_list')
