# coding=utf-8
from django.conf.urls import url
from . import show_view, manage_view

urlpatterns = [
    url(r'^$', show_view.index, name='article-index'),
    url(r'^article-detail/(?P<article_id>\d+)/$', show_view.article_detail, name='article-detail'),

    # 文章管理
    url(r'^create-article/$', manage_view.create_article, name="create-article"),
    url(r'^edit-article/(?P<article_id>\d)/$', manage_view.edit_article, name="edit-article"),
    url(r'^list-article/$', manage_view.list_articles, name="list-articles"),
    url(r'^del-article/(?P<article_id>\d+)$', manage_view.del_article, name="del-article"),
]