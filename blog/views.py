from django.views.generic import ListView, DetailView

from blog.models import Article
from services.general.view_mixins import CachedQuerySetMixin, ActiveUrlMixin


class IndexActiveUrlMixin(ActiveUrlMixin):
    active_url = "index"


class ArticleListView(CachedQuerySetMixin, IndexActiveUrlMixin, ListView):
    cache_lifetime = 600
    model = Article
    template_name = "blog/list.html"

    def get_queryset(self):
        return self.model.objects.all().order_by("?")[:3]


class ArticleDetailView(IndexActiveUrlMixin, DetailView):
    model = Article
    template_name = "blog/detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_amount += 1
        obj.save()
        return obj
