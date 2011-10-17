from django import template
from samklang_blog.models import Entry

register = template.Library()

@register.simple_tag(takes_context=True)
def latest_entries(context, number):
    """get a list, latest, of the 'numbember' latest entries"""
    latest = Entry.live.all()[:number]
    context['latest_entries'] = latest
    return ''
