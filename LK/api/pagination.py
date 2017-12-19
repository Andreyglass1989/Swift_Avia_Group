from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class PackLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10

class PackPageNumberPagination(PageNumberPagination):
    page_size = 5