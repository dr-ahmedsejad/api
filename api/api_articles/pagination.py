from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 10

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 20





from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 6
    max_limit = 10
class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 6

