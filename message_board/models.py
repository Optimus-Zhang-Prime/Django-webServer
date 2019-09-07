from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    nickname = models.CharField(max_length=20, default="匿名网友")
    message = models.TextField(null=False)
    del_pwd = models.CharField(max_length=20)
    category = models.CharField(max_length=2,
                                choices=(('情感', '0'), ('生活', '1'), ('技术', '2'), ('新闻', '3'), ('幽默', 4), ('其它', '5')))
    time = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.message


class Profile(models.Model):  # 用户信息
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField(null=True)
    signature = models.CharField(max_length=100)
    work = models.CharField(max_length=30, null=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
