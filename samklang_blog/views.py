from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DateDetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.sites.models import Site

from samklang_blog.models import Entry
from samklang_blog.forms import EntryForm

from datetime import datetime

MONTH_FORMAT = '%m'

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    initial = {'pub_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    month_format = MONTH_FORMAT

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if hasattr(self.request, 'site'):
            self.object.site = self.request.site
        else:
            self.object.site = Site.objects.get(pk=1)
        self.object.save()
        return HttpResponseRedirect(self.object.get_absolute_url())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EntryCreateView, self).dispatch(*args, **kwargs)

class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    month_format = MONTH_FORMAT

    #def form_valid(self, form):
    #    self.object = form.save()
    #    return HttpResponseRedirect(self.object.get_absolute_url())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EntryUpdateView, self).dispatch(*args, **kwargs)

class EntryArchiveIndexView(ArchiveIndexView):
    model = Entry
    date_field = 'pub_date'
    month_format = MONTH_FORMAT
    allow_empty = True

    def get_queryset(self):
        return Entry.live.all()

class EntryYearArchiveView(YearArchiveView):
    model = Entry
    date_field = 'pub_date'
    month_format = MONTH_FORMAT
    allow_empty = True

class EntryMonthArchiveView(MonthArchiveView):
    model = Entry
    date_field = 'pub_date'
    month_format = MONTH_FORMAT
    allow_empty = True

class EntryDateDetailView(DateDetailView):
    model = Entry
    date_field = 'pub_date'
    month_format = MONTH_FORMAT
