# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone   # settings中的TIME_ZONE要改为'Asia/Shanghai'
from django.core.urlresolvers import reverse
# Create your models here.


class Article(models.Model):
    # author = models.ForeignKey(User, related_name="article")  # 多对一的关系
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # 内部类，python中的内部类的作用：让实例公用同一个属性值。该处的作用类似，即每个实例都具有的行为或属性
        ordering = ("-updated",)  # 按照文章的标题来排序，作用在查询出相关的文章之后的排序。这是行为

    def __str__(self):
        return self.title