#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Dane Collins'
SITENAME = 'exploring data'
SITESUBTITLE = 'Thinking about and analyzing data'
SITEURL = ''

PATH = 'content'
THEME = 'themes/pelican-alchemy/alchemy'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('twitter', 'https://twitter.com/danecollins/'),
         ('linkedin', 'https://www.linkedin.com/in/danec/'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/danecollins/'),
          ('linkedin', 'https://www.linkedin.com/in/danec/'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

STATIC_PATHS = ['images']
IGNORE_FILES = ['.ipynb_checkpoints', '__pycache__']
EXTRA_PATH_METADATA = {'images/favicon.ico': {'path': 'favicon.ico'}, }
