#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pathlib import Path
from pelican_jupyter import markup as nb_markup
import math
from loguru import logger

HOME_URL = "https://www.legendu.net"
SITEURL = f"{HOME_URL}/cn"
SITESUBTITLE = "山不在高，有仙则名；水不在深，有龙则灵。"
AUTHOR = "Ben Chuanlong Du"
SITENAME = "Ben Chuanlong Du's Blog"
DEFAULT_DATE_FORMAT = "%b %d, %Y"
TIMEZONE = "US/Pacific"
DEFAULT_LANG = "en"
USE_FOLDER_AS_CATEGORY = False
DELETE_OUTPUT_DIRECTORY = True
logger.debug("Site URL: {}", SITEURL)

# pages
PAGE_PATHS = ["pages"]
DISPLAY_PAGES_ON_MENU = False

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
    ("Home", HOME_URL),
    ("Blog", SITEURL),
    ("Archives", f"{SITEURL}/archives.html"),
    ("About", f"{HOME_URL}/pages/about"),
]
NEWEST_FIRST_ARCHIVES = True
ARTICLE_ORDER_BY = "reversed-modified"

# tag cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 100
JINJA_FILTERS = {
    "count_to_font_size": lambda c: "{p:.1f}%".format(p=100 + 25 * math.log(c, 2)),
}

# github include settings
GITHUB_USER = "legendu-net"
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/ben-chuanlong-du-1239b221/"),
    ("Docker Hub", "https://hub.docker.com/u/dclong"),
    (
        "Stack Overflow",
        "https://stackoverflow.com/users/7808204/benjamin-du?tab=profile",
    ),
    ("Twitter", "https://twitter.com/longendu"),
)

DEFAULT_PAGINATION = 6

STATIC_PATHS = [
    "images",
    "figures",
    "downloads",
    "favicon.png",
    "media",
    "CNAME",
    "readme.md",
]
CODE_DIR = "downloads/code"
NOTEBOOK_DIR = "downloads/notebooks"

# theme
BLOG_DIR = Path(__file__).resolve().parent.parent
CSS_FILE = "main_2.css"
THEME = BLOG_DIR / "themes/octopress_2"

# plugins
PLUGINS = ["render_math"]
## mathjax
MATH_JAX = {"auto_insert": True, "tex_extensions": ["color.js", "mhchem.js"]}

# disqus comment
DISQUS_SITENAME = "dclong"

# Sharing
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
MODERN_GOOGLE_ANALYTICS = "G-3STS9BVPF6"
