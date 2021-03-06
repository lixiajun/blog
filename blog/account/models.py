# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.


class User(AbstractUser):

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    SEX_CHOICES = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )

    # Inherit fields [username, email, is_staff, is_active, is_superuser, last_login, and date_joined]

    nickname = models.CharField(max_length=20, default=None, null=True, blank=True, verbose_name='用户昵称')
    avatar = models.CharField(max_length=50, default=None, null=True, blank=True, verbose_name='用户头像')
    sex = models.IntegerField(choices=SEX_CHOICES, default=0, verbose_name='性别')
    mobile = models.CharField(max_length=20, default=None, null=True, blank=True, verbose_name='用户手机号')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username


class UserPermission(models.Model):  # 创建完以后，就会在 auth_permission里面有记录
    class Meta:
        permissions = (
            ('user_manage', u'用户管理'),
        )