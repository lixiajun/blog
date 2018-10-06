from django.conf.urls import url
from . import manage_view
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', manage_view.list_users, name='list-users'),
    url(r'^login/$', manage_view.account_login, name='login'),
    url(r'^logout/$', manage_view.account_logout, name='logout'),
    url(r'^create_user/$', manage_view.create_user, name='create-user'),
    url(r'^del_user/(?P<user_id>\d+)$', manage_view.del_user, name='del-user'),
    url(r'^manage_perm/$', manage_view.manage_perm, name='manage-perm'),
    url(r'^add_group/$', manage_view.add_group, name='add-group'),
    url(r'^group_add_perm/$', manage_view.group_add_perm, name='group-add-perm'),
    url(r'^group_add_user/$', manage_view.group_add_user, name='group-add-user'),
    url(r'^deny_perm/$', TemplateView.as_view(template_name="account/manage_permission/permission_denied.html"), name='permission_denied'),
]