from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from samklang.core.response import JSONResponse

from s7n.blog.models import Entry, Image
from s7n.blog.forms import EntryForm

def new_entry(request):
    """Create a new entry"""
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return HttpResponseRedirect('/')
    else:
        entry = Entry()
        form = EntryForm(instance=entry)

    return render_to_response(
        'blog/new_entry.html',
        {'form': form},
        context_instance=RequestContext(request))

def images_json(request):
    """Return json data of images"""
    images = Image.objects.all()
    data = [{'slug': img.slug, 'url': img.get_image_url()} for img in images]
    return JSONResponse(data)