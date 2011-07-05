from django.template.loader import render_to_string
from s7n.pages.pagewidgets import Widget
from s7n.blog.models import Entry

class Latest(Widget):
    """Widget listing latest entries"""

    def render(self):
        limit = self.options.get('limit', 5)
        entries = Entry.live.all()[:limit]

        return render_to_string(
            'blog/widgets/latest.html',
            {'object_list': entries,}
        )