from django.shortcuts import render
from .models import Classes
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# 以下各函数在urls.py中使用
def showClasses(request):
    classList = Classes.classobj.all()
    return render(request, "allClasses.html", {"AllClasses": classList})


def classStu(request, num):
    Oneclass = Classes.classobj.get(pk=num)
    stuList = Oneclass.students_set.all()
    return render(request, "stuInClass.html", {"stulist": stuList})


def addClass(request):
    aClass = Classes.createClass("实验班", 19)
    aClass.save()
    return HttpResponse("保存成功")
