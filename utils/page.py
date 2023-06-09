from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "max_page"
    max_page_size = 5
    page_query_param = 'page'
