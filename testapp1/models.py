from django.db import models

# from django.utils import timezone     timezone.now可以获取当前时间
'''
关于models：
TextField：大文本字段
DecimalField(max_digits=总位数，decimal_places=小数点后位数):小数
DateField(auto_now=True记录最后一次修改,auto_now_add=True记录创建时间)
FileField文件
ImageField图片

字段选项：
db_column=''指定字段名，默认为属性名
db_index=True 以此为索引
primary_key=True 以此为主键
unique=True 必须唯一

关系：
ForeignKey：一对多，将字段放在多的端中
ManyToManyField：多对多，放两端
OneToOneField：一对一，放任一一端
'''


# Create your models here.

class ClassesManager(models.Manager):
    def get_queryset(self):  # 修改查询
        return super(ClassesManager, self).get_queryset().filter(
            isDelete=False)  # 过滤掉被删除的班级，过滤器可以写多重， .filter(键=值，键=值).filter()


'''
其它过滤器：
all()全部，返回的是对象
exclude()过滤掉符合条件的数据
order_by()排序
values()全部，返回到是详细信息列表，每个对象是一个字典

'''


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
