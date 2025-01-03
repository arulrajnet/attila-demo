#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pelican'
SITENAME = u'Attila Demo'
SITESUBTITLE = u'Blog description here.'
SITEURL = 'http://localhost:8000'

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
          ('Twitter', 'http://twitter.com/getpelican'),
          ('Github', 'https://github.com/getpelican/pelican')
          )

# Pagination
DEFAULT_PAGINATION = 5
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
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_URL = '{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# Author
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'author/'
AUTHORS_SAVE_AS = 'author/index.html'

#Archives
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'

# Markdown settings
# Refer - https://github.com/DataDog/Python-Markdown/tree/master/markdown/extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.tables": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {
            "title": "Table of Contents",
            # empty marker to generate only header ids
            "marker": "[TOC]",
            "permalink": "false",
        },
    },
    "output_format": "html5",
}

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
    "pelican.plugins.image_process",
    "pelican.plugins.minify",
    "pelican.plugins.neighbors",
    "pelican.plugins.obsidian",
    "pelican.plugins.related_posts",
    "pelican.plugins.seo",
    "pelican.plugins.sitemap",
    "pelican.plugins.webassets",
    "post_stats",
]

# Minify settings
CSS_MIN = True
JS_MIN = False
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True

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

# Settings for image_process
IMAGE_PROCESS = {
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("4x", ["scale_in 3200 2400 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}

try:
    import attila
    THEME = attila.get_path()
except ImportError:
    THEME = 'attila'

### Theme specific settings

# To set background image for the home page.
# HOME_COVER = 'https://images.unsplash.com/photo-1600884877875-065ed42abbd1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2582&q=80'

# Custom Header

TAG_META = {
  "cupcake": {
    "cover": "assets/images/rainbow_cupcake_cover.png",
    "description": "Cupcake ipsum dolor sit amet. Topping",
  },
  "general": {
    "cover": "https://images.unsplash.com/photo-1486427944299-d1955d23e34d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    "description": "General ipsum dolor sit amet. Topping"
  },
  "getting started": {
    "color": "MediumSeaGreen",
    "description": "Getting Started ipsum dolor sit amet. Topping"
  }
}

CATEGORY_META = {
  "examples": {
    "cover": "https://images.unsplash.com/photo-1645113720391-279a153b4f53?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2073&q=80",
    "description": "Examples ipsum dolor sit amet. Topping"
  },
  "misc": {
    "color": "SlateBlue",
    "description": "Misc ipsum dolor sit amet. Topping"
  }
}

AUTHOR_META = {
  "pelican": {
    "name": "Some Writer",
    "cover": "https://images.unsplash.com/photo-1510146758428-e5e4b17b8b6a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    "image": "assets/images/avatar.png",
    "website": "https://getpelican.com/",
    "linkedin": "arulrajnet",
    "github": "arulrajnet",
    "twitter": "arulrajnet",
    "instagram": "arulrajnet",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

MENUITEMS = (('Home', '/'),
             ('Tag', '/tag/getting-started/'),
             ('Author', '/author/pelican/'),
             ('Category', '/category/examples/'),
             ('Archives','/2015/11/'),
             ('Plugins', 'https://github.com/pelican-plugins'))

SHOW_ARTICLE_MODIFIED_TIME = False
SHOW_AUTHOR_BIO_IN_ARTICLE = False
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = True
SHOW_CREDITS = True
SHOW_FULL_ARTICLE_IN_SUMMARY = False
SHOW_PAGES_ON_MENU = True
SHOW_SITESUBTITLE_IN_HTML_TITLE = False
SHOW_TAGS_IN_ARTICLE_SUMMARY = False

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
