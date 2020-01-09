from django.db import models

# from django.utils import timezone     timezone.now可以获取当前
# Create your models here.

class ClassesManager(models.Manager):
    def get_queryset(self):  # 修改查询
        return super(ClassesManager, self).get_queryset().filter(
            isDelete=False)  # 过滤掉被删除的班级，过滤器可以写多重， .filter(键=值，键=值).filter()




def createClass(self, name, number, isd=False):  # 创建对象
    aClass = self.model()
    aClass.class_name = name
    aClass.stu_number = number
    aClass.isDelete = isd
    return aClass
    # 在views.py中：aClass=Classes.classobj.createClass("", , )


class Classes(models.Model):  # 班级类，一个类对应数据库中的一个表
    class_name = models.CharField(max_length=20)  # 字符串
    stu_number = models.IntegerField()
    isDelete = models.BooleanField()  # 可设置default

    classobj = ClassesManager()

    def __str__(self):
        return self.class_name

    # class Meta:
    #   db_table=""  设置表名
    #   ordering=['id']升序    ['-id']降序

    # 可以定义一个类方法用于创建对象，而不能使用__init__
    @classmethod
    def createClass(cls, name, number, isd=False):
        aClass = cls(class_name=name, stu_number=number, isDelete=isd)
        return aClass
    # 也可以在重写Manager类时添加一个createClass方法


class Students(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=4)
    stu_class = models.ForeignKey("Classes", on_delete=models.CASCADE)  # 关联外键
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
