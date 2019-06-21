# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import Article
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def list_articles(request):
    request_data = request.GET.copy()
    page_n = request_data.get('page_n', 1)

    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    try:
        current_page = paginator.page(page_n)
        articles = current_page.object_list
    except PageNotAnInteger:  # 请求的页码数值不是整数
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:  # 请求的页码对应的页面为空，或者page为空
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list

    print current_page.has_next()
    print current_page.number
    return render(request, "article/show_article/article_list.html", {'articles': articles, 'page': current_page})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "article/show_article/article-detail.html", {"article": article})


