#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Zutrinken'
SITENAME = u'Attila Demo'
SITESUBTITLE = u'Blog description here.'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE = 'fs'

DEFAULT_DATE_FORMAT = '%d %b %Y'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/arulraj.net'),
          ('Twitter', 'http://twitter.com/arulrajnet')
          )

# Pagination
DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

# To show the line numbers for code blocks
# Refer https://docs.getpelican.com/en/stable/settings.html?highlight=MARKDOWN#basic-settings
# MARKDOWN = {
#   'extension_configs': {
#     'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
#     'markdown.extensions.extra': {},
#     'markdown.extensions.meta': {},
#   },
#   'output_format': 'html5',
# }
# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Comments
DISQUS_SITENAME = "attilademo"

# Analytics
GOOGLE_ANALYTICS = "UA-3546274-12"

THEME = 'attila'

### Theme specific settings

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COVER and use cover in individual articles.
# HEADER_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COLOR and use color in individual articles.
# HEADER_COLOR = 'black'

# To set background image for the home page.
HOME_COVER = 'https://images.unsplash.com/photo-1600884877875-065ed42abbd1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2582&q=80'

# Custom Header

HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png', 'general':'https://images.unsplash.com/photo-1486427944299-d1955d23e34d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'}

AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken A'Mende",
    "cover": "https://images.unsplash.com/photo-1510146758428-e5e4b17b8b6a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    "image": "assets/images/avatar.png",
    "website": "https://arulraj.net",
    "linkedin": "arulrajnet",
    "github": "arulrajnet",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/myblog.css']

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
  'extensions' :[
    'jinja2.ext.loopcontrols',
    'jinja2.ext.i18n',
    'jinja2.ext.do',
  ]
}

JINJA_FILTERS = {'max': max}
