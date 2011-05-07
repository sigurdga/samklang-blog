from django.conf.urls.defaults import *
from s7n.blog.views import new_entry
from s7n.blog.models import Entry

entry_info_dict = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
}

entry_date_dict = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
    'allow_empty': True,
}

urlpatterns = patterns('',
    (r'^new/$', new_entry, {}, 'blog_entry_new'),
)

urlpatterns += patterns('django.views.generic.date_based',
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'blog_entry_detail'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', entry_date_dict, 'blog_entry_archive_month'),
    (r'^(?P<year>\d{4})/$', 'archive_year', entry_date_dict, 'blog_entry_archive_year'),
    (r'^$', 'archive_index', entry_info_dict, 'blog_entry_archive_index'),
)
