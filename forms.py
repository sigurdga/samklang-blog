from django.forms import ModelForm, HiddenInput
from blog.models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'body', 'pub_date', 'pub_enddate', 'slug')
        
        