from django.template.loader import render_to_string
from samklang_pages.pagewidgets import Widget
from samklang_blog.models import Entry

class Latest(Widget):
    """Widget listing latest entries"""

    def render(self):
        limit = self.options.get('limit', 5)
        entries = Entry.live.all()[:limit]

        return render_to_string(
            'samklang_blog/latest_entries.html',
            {'object_list': entries,}
        )

class BlogFront(Widget):
    """For inclusion in main page space"""

    def render(self, request):
        limit = self.options.get('limit', 6)
        entries = Entry.live.all()[:limit]

        return render_to_string(
            'samklang_blog/blog.html',
            {'object_list': entries,}
        )

