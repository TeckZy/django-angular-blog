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


ALLOWED_PROTOCOLS = ['http', 'https', 'mailto']