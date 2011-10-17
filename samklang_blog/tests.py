"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from samklang_blog.models import Entry, Category
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from datetime import datetime

class EntryTest(TestCase):
    def test_live_entry(self):
        u = User()
        u.username = "testuser"
        u.save()
        c = Category()
        c.slug = "cat"
        c.title = "Cat"
        c.save()
        e = Entry()
        e.title = "test"
        e.slug = "test"
        e.body = "jadda"
        e.category = c
        e.user = u
        e.pub_date = datetime.now()
        e.save()

        f = Entry.live.get(title="test")
        self.assertEqual(e, f)

