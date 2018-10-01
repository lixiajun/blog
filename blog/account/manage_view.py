# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from common.utils.little_func import list_menu  # 帮助manage_platform左侧显示正在访问的menu
from django.contrib.auth import authenticate, login, logout  #默认的用户认证和管理应用
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/account/login/')
def list_users(request):
    all_users = User.objects.all()
    account_menu = list_menu('manage')
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
                print '{} login'.format(user.username)
                return HttpResponseRedirect(reverse('first_index'))
            else:
                print '{} login failed'.format(user.username)
                return render(request, "account/manage_user/login.html")
        else:
            return render(request, "account/manage_user/login.html")
    if request.method == "GET":
        return render(request, "account/manage_user/login.html")


def account_logout(request):
    if request.user:
        logout(request)
    return HttpResponseRedirect(reverse('account:login'))
