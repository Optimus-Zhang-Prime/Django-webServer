from django.shortcuts import render
from .models import Classes
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def showClasses(request):
    classList = Classes.objects.all()
    return render(request, "allClasses.html", {"AllClasses": classList})


def classStu(request, num):
    Oneclass = Classes.objects.get(pk=num)
    stuList = Oneclass.students_set.all()
    return render(request, "stuInClass.html", {"stulist": stuList})
