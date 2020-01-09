from django.shortcuts import render
from .models import Cuserdata
from django.http import HttpResponse
import json
import datetime


def data(request):
    if request.method == 'POST':
        try:
            ans = json.loads(request.body)
            name = ans['username']
            name = str(name)
            op = ans['operation']
            op = int(op)
            auserdata = Cuserdata.objects.create(username=name, operation=op)
            return HttpResponse(1)
        except:
            return HttpResponse(0)
def see(requset):
    alldata=Cuserdata.objects.all().order_by('-time')
    for data in alldata:
        data.time=data.time.strftime('%m月%d日  %H:%M:%S')
    return render(requset,"see.html",locals())
def haha(request):
    return render(request, "te.html", locals())
