from django.shortcuts import render
from .models import Classes
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def showClasses(request):
    classList=Classes.objects.all()
    return render(request,"testApp1html.html",{"AllClasses":classList}  )
