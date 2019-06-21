# coding=utf-8
from django.core.paginator import Paginator
def list_menu(child_menu):
    article_menu = dict()
    article_menu['active'] = True
    article_menu[child_menu] = True
    return article_menu