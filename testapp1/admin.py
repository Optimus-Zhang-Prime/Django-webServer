#站点配置,都是自己加的

from django.contrib import admin
from .models import Classes,Students
# Register your models here.

class ClassAddStu(admin.TabularInline):#在classes中加student
    model = Students
class ClassesAdmin(admin.ModelAdmin):
    inlines = [ClassAddStu]
    list_display = ['pk','class_name','stu_number','isDelete']#显示的字段
    list_filter = ['isDelete']#过滤器
    search_fields = ['class_name']#搜索
    list_per_page = 5 #每页五条

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['pk','name','gender','isDelete']#显示的字段，也可以将‘’改为函数，不加（）
    list_filter = ['isDelete']#过滤器
    search_fields = ['name']#搜索
    list_per_page = 5 #每页五条


admin.site.register(Classes,ClassesAdmin)#也可以用装饰器写
admin.site.register(Students,StudentsAdmin)