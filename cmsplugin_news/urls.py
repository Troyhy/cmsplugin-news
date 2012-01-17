from django.conf.urls.defaults import *

from cmsplugin_news.models import News

from . import feeds


news_info_dict = {
    'queryset': News.published.all(),
    'date_field': 'pub_date',
}

news_info_month_dict = {
    'queryset': News.published.all(),
    'date_field': 'pub_date',
    'month_format': '%m',
}

urlpatterns = patterns('django.views.generic.date_based',
    url(r'^$', 
        'archive_index', news_info_dict, name='news_archive_index'),
    
    url(r'^(?P<year>\d{4})/$', 
        'archive_year', news_info_dict, name='news_archive_year'),
    
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 
        'archive_month', news_info_month_dict, name='news_archive_month'),
    
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 
        'archive_day', news_info_month_dict, name='news_archive_day'),
    
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
        'object_detail', news_info_month_dict, name='news_detail'),

    url(r'^feed/$', feeds.NewsFeed())
)

