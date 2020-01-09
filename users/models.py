from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):

    nickname = models.CharField(blank=True, null=True, max_length=20)
    avatar = models.FileField(upload_to='avatar/')
    mobile = models.CharField(blank=True, null=True, max_length=13)
    subscribe = models.BooleanField(default=False)

    type = models.IntegerField(default=0)  # 0为志愿者，1为培训，2为招募者
    gender = models.BooleanField(null=True)  # 男为1，女为0
    signature = models.CharField(null=True, max_length=200)  # 自我介绍
    work = models.CharField(max_length=30, null=True)  # 职业
    age = models.IntegerField(null=True)  # 年龄
    enable = models.BooleanField(default=True)  # 账户是否可用
    isAttest = models.BooleanField(default=False)  # 账户是否被认证
    num = models.IntegerField(null=True)  # 备用字段
    class Meta:
        db_table = "v_user"


class Feedback(models.Model):
    contact = models.CharField(blank=True, null=True, max_length=20)
    content = models.CharField(blank=True, null=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "v_feedback"