from django.conf.urls import url
from . import manage_view

urlpatterns = [
    url(r'^$', manage_view.list_users, name='list-users'),
    url(r'^login/$', manage_view.account_login, name='login'),
    url(r'^logout/$', manage_view.account_logout, name='logout'),
    url(r'^create_user/$', manage_view.create_user, name='create-user'),
    url(r'^del_user/(?P<user_id>\d+)$', manage_view.del_user, name='del-user'),
]