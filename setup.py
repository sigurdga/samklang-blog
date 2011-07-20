#!/usr/bin/env python
from distutils.core import setup

setup(
        name = 's7n-blog',
        version = "1a1",
        packages = ['s7n', 's7n.blog', 's7n.blog.migrations'],
        package_data = {'s7n.blog': ['templates/blog/*.html', 'locale/*/LC_MESSAGES/django.*o']},
        )
