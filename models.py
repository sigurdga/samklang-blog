from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from tagging.fields import TagField
from tagging.models import Tag
from markdown import markdown
import re

from blog.managers import LiveEntryManager

class Category(models.Model):
    """Blog category"""
    title = models.CharField(max_length=80, help_text=_('Maximum 80 characters.'))
    slug = models.SlugField(unique=True, help_text=_('Suggested value automatically generated from title. Must be unique.'))
    description = models.TextField(blank=True, null=True)
    
    class Meta:
	    ordering = ['title']
	    verbose_name_plural = _("categories")
    
    def __unicode__(self):
	    return self.title
        
    @models.permalink
    def get_absolute_url(self):
        return ('blog_category_detail', (), { 'slug': self.slug })


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
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group, verbose_name=_('created for'), null=True, blank=True)
    slug = models.SlugField(unique_for_date='pub_date', help_text="Suggested value generated from title. Must be unique.")

	# categorization
    category = models.ForeignKey(Category)
    tag_list = TagField(help_text="Separate tags with spaces.", default="")
    
    # managers, first one is default
    live = LiveEntryManager()
    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = _("entries")
	
    def save(self, *args, **kwargs):
        # add markdown for images if needed
        images = re.findall("!\[(?P<alt>[-_\w ]+)\]\[(?P<slug>[-\w]+)\]+", self.body)
        image_ref = ""
        for ref, slug in images:
            try:
                image_class = ContentType.objects.get(app_label=settings.BLOG_IMAGE_MODEL['app'], 
                                                      model=settings.BLOG_IMAGE_MODEL['model'])
                image = image_class.get_object_for_this_type(slug=slug)
                url = image.get_image_url()
            except ObjectDoesNotExist:
                url = slug
            image_ref = "%s\n[%s]: %s" % ( image_ref, slug, url )
        
        body = "%s\n%s" % ( self.body, image_ref )
      
        # convert markdown to html and store it
        self.body_html = markdown(body, ['codehilite'])
        super(Entry, self).save(*args, **kwargs)

    def __unicode__(self):
    	return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_entry_detail', (), {
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%b").lower(),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug
        })
    
    def _get_tags(self):
        return Tag.objects.get_for_object(self)
    
    def _set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    tags = property(_get_tags, _set_tags)

class Image(models.Model):
    """
    Example Image class for use with entry.
    A Slug field and a method for getting image url is needed.
    """
    
    slug = models.SlugField(unique=True, help_text=_('Must be unique'))
    image = models.ImageField(upload_to='/var/tmp')
    pub_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name, verbose_name_plural = _("image"), _("images")

    def __unicode__(self):
        return self.slug
        
    def get_image_url(self):
        return self.image.url
