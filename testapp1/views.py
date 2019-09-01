from django.shortcuts import render
from .models import Classes, Students
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from random import choice

quotes = ['真理惟一可靠的标准就是永远自相符合。 —— 欧文',
          '忠诚可以简练地定义为对不可能的情况的一种不合逻辑的信仰。 —— 门肯',
          '时间是一切财富中最宝贵的财富。 —— 德奥弗拉斯多',
          '这世界要是没有爱情，它在我们心中还会有什么意义！这就如一盏没有亮光的走马灯。 —— 歌德',
          '我读的书愈多，就愈亲近世界，愈明了生活的意义，愈觉得生活的重要。 —— 高尔基',
          '理想是人生的太阳。 —— 德莱赛',
          '把时间用在思考上是最能节省时间的事情。 —— 卡曾斯',
          '科学是到处为家的，不过，在任何不播种的地方，是决不会得到丰收的。 —— 赫尔岑',
          '成功的秘诀，在永不改变既定的目的。 —— 卢梭',
          '文明就是要造成有修养的人。 —— 罗斯金']

# 以下各函数在urls.py中使用
def homePage(request):
    return render(request, "homePage.html")


def showClasses(request):
    classList = Classes.classobj.all()
    quote=choice(quotes)
    return render(request, "allClasses.html", {"AllClasses": classList, "quote":quote})


def showStudents(request, page):
    page = int(page)
    studentsList = Students.objects.all()[(page - 1) * 5]


# render的第三个参数将数据从.py传递到.html,可以像上面用字典的形式，也可以用locals()将所有局部变量传入

def classStu(request, num):
    Oneclass = Classes.classobj.get(pk=num)  # pk代表主键
    stuList = Oneclass.students_set.all()
    return render(request, "stuInClass.html", {"stulist": stuList})


def addClass(request):
    aClass = Classes.createClass("实验班", 19)
    aClass.save()
    return HttpResponse("保存成功")

# 也可以在函数内写html，中间空出{}，然后return HttpResponse(html.format(数据字符串)) 就会将数据字符串显示在页面
