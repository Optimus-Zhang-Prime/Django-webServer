#站点配置

from django.contrib import admin
from .models import Classes,Students #自己加的
# Register your models here.

class ClassesAdmin(admin.ModelAdmin):
    list_display = ['pk','class_name','stu_number','isDelete']#显示的字段
    list_filter = ['isDelete']#过滤器
    search_fields = ['class_name']#搜索
    list_per_page = 5 #每页五条


admin.site.register(Classes,ClassesAdmin)#自己加
admin.site.register(Students)