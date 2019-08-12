from django.db import models

# Create your models here.
class Classes(models.Model):#对应数据库中的表
    class_name=models.CharField(max_length=20)
    stu_number=models.IntegerField()
    isDelete=models.BooleanField()
class Students(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=4)
    stu_class=models.ForeignKey("Classes",on_delete=models.CASCADE)#关联外键
