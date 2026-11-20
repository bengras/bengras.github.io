import locale
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')  # Set to English locale

DEFAULT_LANG = 'en'
AUTHOR = 'Ben Gras'
OUTPUT_PATH = 'docs/'
PATH = 'content'
THEME = "pelican-themes/mediumfox"
SITEURL = 'https://www.shrike-systems.com'
SITENAME = 'Shrike Systems'
TIMEZONE = 'CET'
DELETE_OUTPUT_DIRECTORY = True
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
AUTHOR_TWITTER = 'bjg'
AUTHOR_GITHUB = 'bengras'
AUTHOR_LINKEDIN = 'bengras'

STATIC_PATHS = [ 'images' , 'files' , 'extra/favicon.png' ]
EXTRA_PATH_METADATA = { 'extra/favicon.png': { 'path': 'favicon.png' } }

# Single author and single category make these index pages redundant.
DIRECT_TEMPLATES = ['index', 'archives', 'tags']
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
