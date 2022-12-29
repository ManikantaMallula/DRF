from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPaginaton(PageNumberPagination):
    page_size = 5
    page_query_param = 'mypage'
    page_size_query_param = 'num'
    max_page_size = 15
    last_page_strings = ('endpage',)

    ##http://127.0.0.1:8000/emp/?mypage=endpage&num=12


class MYpagination2(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 20

    ##http://127.0.0.1:8000/emp/?mylimit=25&myoffset=40


class MyPagination3(CursorPagination):
    ordering = 'esal'
    page_size = 5
