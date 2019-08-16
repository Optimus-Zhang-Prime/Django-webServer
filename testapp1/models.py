from django.db import models


# Create your models here.
class Classes(models.Model):  # 一个类对应数据库中的一个表
    class_name = models.CharField(max_length=20)
    stu_number = models.IntegerField()
    isDelete = models.BooleanField()

    def __str__(self):
        return self.class_name


class Students(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=4)
    stu_class = models.ForeignKey("Classes", on_delete=models.CASCADE)  # 关联外键
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
