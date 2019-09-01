from django.db import models


class Post(models.Model):
    nickname = models.CharField(max_length=20, default="匿名网友")
    message = models.TextField(null=False)
    del_pwd = models.CharField(max_length=20)
    category=models.CharField(max_length=2,choices=(('情感','0'),('生活','1'),('技术','2'),('新闻','3'),('幽默',4),('其它','5')))
    time = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.message
