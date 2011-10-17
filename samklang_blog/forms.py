from django.forms import ModelForm
from samklang_blog.models import Entry

class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'pub_date', 'pub_enddate', 'group', 'body')


