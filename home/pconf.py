#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pathlib import Path
from pelican_jupyter import markup as nb_markup
from loguru import logger
SITEURL = "http://www.legendu.net"
SITESUBTITLE = "And let it direct your passion with reason."
AUTHOR = "Ben Chuanlong Du"
SITENAME = "Ben Chuanlong Du's Blog"
DEFAULT_DATE_FORMAT = "%b %d, %Y"
TIMEZONE = "US/Pacific"
DEFAULT_LANG = "en"
USE_FOLDER_AS_CATEGORY = False
DELETE_OUTPUT_DIRECTORY = True
PAGE_PATHS = ["pages"]
DISPLAY_PAGES_ON_MENU = False
logger.debug("Site URL: {}", SITEURL)

# Set the article URL
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

# Title menu options
MENUITEMS = [
        ("Home", SITEURL),
        ("English", f"{SITEURL}/en"),
        ("中文", f"{SITEURL}/cn"),
        ("Miscellanea", f"{SITEURL}/misc"),
        ("Outdated", f"{SITEURL}/outdated"),
        ("About", f"{SITEURL}/pages/about"),
    ]
NEWEST_FIRST_ARCHIVES = True
ARTICLE_ORDER_BY = "reversed-modified"

# tag cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100

# github include settings
GITHUB_USER = "dclong"
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/ben-chuanlong-du-1239b221/"),
    ("Twitter", "https://twitter.com/longendu"),
    ("Facebook", "https://www.facebook.com/chuanlong.du")
)

DEFAULT_PAGINATION = 6

STATIC_PATHS = [
            "images", 
            "figures", 
            "downloads", 
            "favicon.png", 
            "media",
            "CNAME",
        ]
CODE_DIR = "downloads/code"


# theme 
BLOG_DIR = Path(__file__).resolve().parent.parent
CSS_FILE = "main.css"
THEME = BLOG_DIR / "themes/octopress_0"

# plugins
PLUGINS = ["render_math"]
## mathjax
MATH_JAX = {"auto_insert": True,
        "tex_extensions": ["color.js", "mhchem.js"]
    }

# disqus comment
DISQUS_SITENAME = "dclong"

# sharing
TWITTER_USER = "longendu"
GOOGLE_PLUS_USER = "duchuanlong"
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = "false"
TWITTER_SHOW_FOLLOWER_COUNT = "true"

# rss/atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = "atom.xml"

SITESEARCH = "https://www.bing.com/search"

# google analytics
GOOGLE_ANALYTICS = "UA-30259661-1"
