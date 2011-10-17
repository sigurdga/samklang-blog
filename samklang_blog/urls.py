from django.conf.urls.defaults import *
from samklang_blog.views import EntryCreateView, EntryArchiveIndexView
from samklang_blog.views import EntryYearArchiveView, EntryMonthArchiveView, EntryDateDetailView
from samklang_blog.models import Entry

urlpatterns = patterns('',
    (r'^new/$', EntryCreateView.as_view(), {}, 'blog_entry_new'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', EntryDateDetailView.as_view(), {}, 'blog_entry_detail'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', EntryMonthArchiveView.as_view(), {}, 'blog_entry_archive_month'),
    (r'^(?P<year>\d{4})/$', EntryYearArchiveView.as_view(), {}, 'blog_entry_archive_year'),
    (r'^$', EntryArchiveIndexView.as_view(), {}, 'blog_entry_archive_index'),
)
