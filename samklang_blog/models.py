from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

#from tagging.fields import TagField
#from tagging.models import Tag
from samklang_utils import markdown, slugify

from samklang_blog.managers import LiveEntryManager

class Entry(models.Model):
    """
    Blog Entry.
    Specify which image class to use in settings.
    Example:
        BLOG_IMAGE_MODEL = { 'app': 'blog', 'model': 'image' }
    """

    # core fields
    title = models.CharField(max_length=80, help_text=_("Maximum 80 characters."))
    body = models.TextField(help_text=_("Content written in markdown syntax."))
    pub_date = models.DateTimeField(blank=True, null=True, help_text=_("Date from which the entry is shown live. Blank = draft."))
    pub_enddate = models.DateTimeField(blank=True, null=True, help_text=_("Date from which the entry not longer is shown live. Blank = live forever."))
    updated_date = models.DateTimeField(auto_now=True)

	# fields to store generated html
    body_html = models.TextField(editable=False, blank=True)

	# metadata
    site = models.ForeignKey(Site, verbose_name=_('site'))
    user = models.ForeignKey(User, verbose_name=_('user'))
    group = models.ForeignKey(Group, verbose_name=_('created for'), null=True, blank=True)
    slug = models.SlugField(unique_for_date='pub_date', help_text="Suggested value generated from title. Must be unique.")

	# categorization
    #tag_list = TagField(help_text="Separate tags with spaces.", default="")

    # managers, first one is default
    objects = models.Manager()
    live = LiveEntryManager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = _("entries")
        db_table = 'samklang_blog_entry'

    def save(self, *args, **kwargs):
        # convert markdown to html and store it
        self.body_html = markdown(self.body)
        self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s, %s" % (self.title, self.body[0:50])

    @models.permalink
    def get_absolute_url(self):
        return ('blog_entry_detail', (), {
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%b").lower(),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug
        })

    #def _get_tags(self):
        #return Tag.objects.get_for_object(self)

    #def _set_tags(self, tags):
        #Tag.objects.update_tags(self, tags)

    #tags = property(_get_tags, _set_tags)
