from django.shortcuts import render
from django.http import JsonResponse
from models import Article
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request, "article/show_article/article_list.html", {'articles': articles})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "article/show_article/article-detail.html", {"article": article})


