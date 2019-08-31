from django.db import models


class Post(models.Model):
    nickname = models.CharField(max_length=20, default="匿名网友")
    message = models.TextField(null=False)
    del_pwd = models.CharField(max_length=20)
    category=models.CharField(choices=('情感','生活','技术','新闻','幽默','其它'))
    time = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.message
