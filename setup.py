#!/usr/bin/env python
#coding: utf8

from distutils.core import setup

setup(
        name='samklang-blog',
        version="0.2.4",
        author='Jørgen Bergquist',
        author_email='gismos@gmail.com',
        url='http://github.com/sigurdga/samklang-blog',
        description='News and blog app for Samklang',
        long_description=open('README.txt').read(),
        license="AGPL",
        packages = ['samklang_blog', 'samklang_blog.templatetags', 'samklang_blog.migrations'],
        package_data = {'samklang_blog': ['templates/samklang_blog/*.html', 'locale/*/LC_MESSAGES/django.*o']},
        classifiers=[
                "Development Status :: 3 - Alpha",
                "License :: OSI Approved :: GNU Affero General Public License v3",
                "Intended Audience :: Developers",
                "Framework :: Django",
                "Environment :: Web Environment",
                "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
                ]
        )

