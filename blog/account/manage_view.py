# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import User, UserPermission
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from common.utils.little_func import list_menu  # 帮助manage_platform左侧显示正在访问的menu
from django.contrib.auth import authenticate, login, logout  #默认的用户认证和管理应用
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
# Create your views here.


@login_required(login_url='/account/login/')
def list_users(request):
    all_users = User.objects.all()
    account_menu = list_menu('manage_user')
    return render(request, "account/manage_user/users_list.html", {"all_users": all_users, "account_menu": account_menu})


@login_required(login_url='/account/login/')
@csrf_exempt
def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        sex = request.POST.get('user_sex')
        # mobile = request.POST.get('mobile')

        user = User.objects.create(username=username)
        user.set_password(password)
        user.email = email
        user.sex = sex
        user.save()
        return HttpResponseRedirect(reverse("account:list-users"))
    if request.method == "GET":
        account_menu = list_menu('create')
        return render(request, "account/manage_user/user_create.html", {'account_menu': account_menu})


@login_required(login_url='/account/login/')
def del_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect(reverse("account:list-users"))


def account_login(request):
    if request.method == "POST":
        user_name = request.POST.get('username', None)
        user_passwd = request.POST.get('passwd', None)
        if user_name and user_passwd:
            user = authenticate(username=user_name, password=user_passwd)
            if user:
                login(request, user)
                print('{} login'.format(user.username))
                return HttpResponseRedirect(reverse('index'))
            else:
                print('{} login failed'.format(user_name))
                return render(request, "account/manage_user/login.html")
        else:
            return render(request, "account/manage_user/login.html")
    if request.method == "GET":
        return render(request, "account/manage_user/login.html")


def account_logout(request):
    if request.user:
        logout(request)
    return HttpResponseRedirect(reverse('account:login'))


@permission_required('account.user_manage', login_url='/account/deny_perm/')
def manage_perm(request):
    account_menu = list_menu('manage_perm')
    users_obj = User.objects.all()
    users = []
    for user in users_obj:
        user_info = dict()
        user_groups = user.groups.all()
        user_info['user_groups_num'] = user_groups.count()
        user_info['user_name'] = user.username
        user_info['user_groups'] = [i_tuple[0] for i_tuple in user_groups.values_list('name')]
        users.append(user_info)

    groups_obj = Group.objects.all()
    groups = []
    for group in groups_obj:
        group_info = dict()
        group_perms = group.permissions.all()
        group_info['group_perms_num'] = group_perms.count()
        group_info['group_name'] = group.name
        group_info['group_perms'] = [i_tuple[0] for i_tuple in group_perms.values_list('codename')]
        groups.append(group_info)
    permissions = UserPermission._meta.permissions
    re_context = dict()
    re_context["account_menu"] = account_menu
    re_context["groups_obj"] = groups_obj
    re_context["perms"] = permissions
    re_context["users"] = users
    re_context["groups"] = groups
    return render(request, 'account/manage_permission/permission_manage.html', re_context)


@permission_required('account.user_manage', login_url='/account/deny_perm/')
def add_group(request):
    name = request.POST.get('group_name', '')
    if not Group.objects.filter(name=name).exists():
        Group.objects.create(name=name)
    return HttpResponseRedirect(reverse('account:manage-perm'))


@permission_required('account.user_manage', login_url='/account/deny_perm/')
def group_add_perm(request):
    group_name = request.POST.get('group_name', '')
    perm_code = request.POST.get('perm_code', '')
    group = Group.objects.get(name=group_name)
    perm = Permission.objects.get(codename=perm_code)
    group.permissions.add(perm)
    group.save()
    return HttpResponseRedirect(reverse('account:manage-perm'))


@permission_required('account.user_manage', login_url='/account/deny_perm/')
def group_add_user(request):
    group_name = request.POST.get('group_name', '')
    user_name = request.POST.get('user_name', '')
    print(group_name,user_name)
    user = User.objects.get(username=user_name)
    group = Group.objects.get(name=group_name)
    user.groups.add(group)
    user.save()
    return HttpResponseRedirect(reverse('account:manage-perm'))
