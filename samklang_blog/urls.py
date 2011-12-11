from django.conf.urls.defaults import *
from samklang_blog.views import EntryCreateView, EntryUpdateView, EntryArchiveIndexView
from samklang_blog.views import EntryYearArchiveView, EntryMonthArchiveView, EntryDateDetailView

urlpatterns = patterns('',
    url(r'^new/$', EntryCreateView.as_view(), name='blog-entry-new'),
    url(r'^edit/(?P<pk>\d+)/$', EntryUpdateView.as_view(), name='blog-entry-edit'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', EntryDateDetailView.as_view(), name='blog-entry-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', EntryMonthArchiveView.as_view(), name='blog-entry-archive-month'),
    url(r'^(?P<year>\d{4})/$', EntryYearArchiveView.as_view(), name='blog-entry-archive-year'),
    url(r'^$', EntryArchiveIndexView.as_view(), name='blog-entry-archive-index'),
)
