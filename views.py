from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext

from blog.models import Entry
from blog.forms import EntryForm

def new_entry(request):
    """Create a new entry"""
    entry = Entry()
    form = EntryForm(instance=entry)
    
    return render_to_response(
        'blog/new_entry.html', 
        {'form': form}, 
        context_instance=RequestContext(request))
