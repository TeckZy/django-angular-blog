from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class CustomePageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100

class CustomeLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 50
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100
    min_limit = 1
    min_offset = 0


# python markdown extension default
MARKDOWN_EXTENSIONS_DEFAULT = [
    'markdown.extensions.abbr',
    'markdown.extensions.attr_list',
    'markdown.extensions.def_list',
    'markdown.extensions.footnotes',
    'markdown.extensions.tables',
    'markdown.extensions.admonition',
    'markdown.extensions.codehilite',
    'markdown.extensions.meta',
    'markdown.extensions.nl2br',
    'markdown.extensions.sane_lists',
    'markdown.extensions.smarty',
    'markdown.extensions.toc',
    'markdown.extensions.wikilinks'
]

# python markdown extension pymdownx
# https://facelessuser.github.io/pymdown-extensions/usage_notes/
MARKDOWN_EXTENSIONS_PYMDOWNX = [
    'pymdownx.extra',
    'pymdownx.superfences',
    'pymdownx.magiclink',
    'pymdownx.tilde',
    'pymdownx.emoji',
    'pymdownx.tasklist',
    'pymdownx.superfences',
    'pymdownx.details',
    'pymdownx.highlight',
    'pymdownx.inlinehilite',
    'pymdownx.keys',
    'pymdownx.progressbar',
    'pymdownx.critic',
    'pymdownx.arithmatex'
]

MARKDOWN_EXTENSIONS = MARKDOWN_EXTENSIONS_DEFAULT + MARKDOWN_EXTENSIONS_PYMDOWNX



ALLOWED_PROTOCOLS = ['http', 'https', 'mailto']