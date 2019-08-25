from django.shortcuts import render
from .models import Classes
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# 以下各函数在urls.py中使用
def homePage(request):
    return render(request, "homePage.html")


def showClasses(request):
    classList = Classes.classobj.all()
    return render(request, "allClasses.html", {"AllClasses": classList})


# render的第三个参数将数据从.py传递到.html,可以像上面用字典的形式，也可以用locals()将所有局部变量传入

def classStu(request, num):
    Oneclass = Classes.classobj.get(pk=num)
    stuList = Oneclass.students_set.all()
    return render(request, "stuInClass.html", {"stulist": stuList})


def addClass(request):
    aClass = Classes.createClass("实验班", 19)
    aClass.save()
    return HttpResponse("保存成功")
