import locale
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')  # Set to English locale

DEFAULT_LANG = 'en'
AUTHOR = 'Ben Gras'
OUTPUT_PATH = 'docs/'
PATH = 'content'
THEME = "pelican-themes/papyrus"
SITEURL = 'https://www.shrike-systems.com'
SITENAME = 'Shrike Systems'
TIMEZONE = 'CET'
DELETE_OUTPUT_DIRECTORY = True
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
SUBTITLE = 'Ben Gras'
SUBTEXT = '''Security researcher: hardware and systems security —
microarchitecture, firmware, and operating systems.
More on the <a href="/pages/about-this-site.html">about page</a>.'''
COPYRIGHT = '© Ben Gras'
SOCIAL = (
    ('github', 'https://github.com/bengras'),
    ('linkedin', 'https://www.linkedin.com/in/bengras'),
)

STATIC_PATHS = [ 'images' , 'files' , 'extra/favicon.png' ]
EXTRA_PATH_METADATA = { 'extra/favicon.png': { 'path': 'favicon.png' } }

DISPLAY_PAGES_ON_MENU = True
# Papyrus's nav links Archive/Categories/Tags; no search (needs Stork).
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None, 'archives': 24}
# Single author; skip author index pages.
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors', 'pelican-toc']
TOC = {'TOC_HEADERS': '^h[1-3]', 'TOC_RUN': 'true', 'TOC_INCLUDE_TITLE': 'false'}
