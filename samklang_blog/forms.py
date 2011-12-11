from django.forms import ModelForm
from samklang_blog.models import Entry
from samklang_utils.forms import MarkdownTextarea

class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'body', 'group', 'pub_date', 'pub_enddate')
        widgets = {'body': MarkdownTextarea()}


