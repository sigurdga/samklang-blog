from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.sites.models import Site

from s7n.blog.models import Entry
from s7n.blog.forms import EntryForm

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm

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

