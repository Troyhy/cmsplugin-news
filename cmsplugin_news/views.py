from django.views.generic import ListView

from . import models
from . import settings


class ArchiveIndexView(ListView):
    """
    A simple archive view that exposes following context:

    * latest
    * date_list
    * paginator
    * page_obj
    * object_list
    * is_paginated

    The first two are intended to mimic the behaviour of the
    date_based.archive_index view while the latter ones are provided by
    ListView.
    """
    paginate_by = settings.ARCHIVE_PAGE_SIZE
    queryset = models.News.published.all()
    template_name = 'cmsplugin_news/news_archive.html'
    include_yearlist = True

    def get_context_data(self, **kwargs):
        context = super(ArchiveIndexView, self).get_context_data(**kwargs)
        context['latest'] = context['object_list']
        if self.include_yearlist:
            date_list = self.get_queryset().dates('pub_date', 'year')[::-1]
            context['date_list'] = date_list
        return context

