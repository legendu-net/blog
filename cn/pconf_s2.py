#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
# remove old files
os.system('rm -rf output/*')
#-------------------------------------------------------------------------
__blog_dir__ = os.environ["blog_dir"]
# !!! http:// is necessary
__home_url__ = "http://www.legendu.net"
SITEURL = os.path.join(__home_url__, "cn") 
#-------------------------------------------------------------------------
SITESUBTITLE = u"山不在高，有仙则名；水不在深，有龙则灵。"
AUTHOR = 'Ben Chuanlong Du'
SITENAME = "Ben Chuanlong Du's Blog"
# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

# pages
PAGE_PATHS = ["pages"]
DISPLAY_PAGES_ON_MENU = False

# Set the article URL
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

# Title menu options
MENUITEMS = [
        ('Home', __home_url__),
        ('Blog', SITEURL), 
        ("Archives", os.path.join(SITEURL, 'archives.html')), 
        ('About', os.path.join(SITEURL, 'pages/about.html')), 
        ('Resume', os.path.join(SITEURL, 'pages/resume.html')), 
        ]
NEWEST_FIRST_ARCHIVES = True

# tag cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100

#Github include settings
GITHUB_USER = 'dclong'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://www.linkedin.com/pub/chuanlong-ben-du/21/9b2/123/'),
            ('Twitter', 'https://twitter.com/longendu'),
            ('Facebook', 'https://www.facebook.com/chuanlong.du'))

DEFAULT_PAGINATION = 6

# STATIC_OUT_DIR requires https://github.com/jakevdp/pelican/tree/specify-static
#STATIC_OUT_DIR = ''
#FILES_TO_COPY = [('favicon.png', 'favicon.png')]

# This requires Pelican 3.3+
STATIC_PATHS = [
            'images', 
            'figures', 
            'downloads', 
            'favicon.png', 
            'media',
            'CNAME',
            'readme.md',
        ]

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'


# theme and plugins
CSS_FILE = 'main_2.css'
THEME = os.path.join(__blog_dir__, "themes/octopress_2")
# plugins
PLUGIN_PATHS = [os.path.join(__blog_dir__, 'plugins')]
PLUGINS = [
        'render_math',
        'summary', 
    ]

# disqus comment
DISQUS_SITENAME = "dclong"

# Sharing
TWITTER_USER = 'longendu'
GOOGLE_PLUS_USER = 'duchuanlong'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'
# FEED_RSS = 


# Search
# SEARCH_BOX = True
# SITESEARCH = "http://www.google.com/search"
# SITESEARCH = "https://search.yahoo.com"
SITESEARCH = "https://www.bing.com/search"

# google analytics
GOOGLE_ANALYTICS = 'UA-30259661-1'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
