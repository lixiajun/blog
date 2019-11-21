# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from article.models import Article
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from common.utils.little_func import list_menu  # 帮助manage_platform左侧显示正在访问的menu
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/login/')
@csrf_exempt
def create_article(request):
    if request.method == "GET":
        article_menu = list_menu('create')
        return render(request, "article/manage_article/create_article.html", {"article_menu": article_menu})

    if request.method == "POST":
        title = request.POST.get('title', None)
        body = request.POST.get('body', None)

        article = Article.objects.create()
        article.title = title
        article.body = body
        article.save()
        return JsonResponse({'error_code': 0})


@login_required(login_url='/account/login/')
@csrf_exempt
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    print(article_id)
    if request.method == "GET":
        article_menu = list_menu('manage')
        return render(request, "article/manage_article/create_article.html", {"article": article, "article_menu": article_menu})

    if request.method == "POST":
        title = request.POST.get('title', None)
        body = request.POST.get('body', None)

        article.title = title
        article.body = body
        article.save()
        return JsonResponse({'error_code': 0})


@login_required(login_url='/account/login/')
def list_articles(request):
    all_articles = Article.objects.all()
    article_menu = list_menu('manage')
    return render(request, "article/manage_article/article_list.html", {'articles': all_articles, 'article_menu': article_menu})


@login_required(login_url='/account/login/')
def del_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return HttpResponseRedirect(reverse("article:list-articles"))