from django.http import HttpResponseRedirect
from AID import models, forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate  # 用户验证
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import User


def homePage(request):
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "homePage.html", locals())


# Create your views here.
def showdata(request):
    if request.user.is_authenticated:
        username = request.user.username
    allpress = models.yali.objects.all()[1:120]
    allfrequency = models.test.objects.all()
    pressArr = []
    for apress in allpress:
        pressArr.append(pow(apress.press / 100, 0.5))
    return render(request, "chart.html", locals())

def detail(request):
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "detail.html", locals())

@login_required(login_url='/login/')
def logout(request):
    if request.user.is_authenticated:
        username = request.user.username
    auth.logout(request)
    messages.add_message(request, messages.INFO, "退出登录成功")
    return redirect("/login/")


def login(request):
    next = request.GET.get('next', '')
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            entername = request.POST['username']
            enterpassword = request.POST['password']
            user = authenticate(username=entername, password=enterpassword)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '登录成功')
                    if next == "":
                        return HttpResponseRedirect("/aid")
                    else:
                        return HttpResponseRedirect(next)
                else:
                    messages.add_message(request, messages.WARNING, '账号未启用')
            else:
                messages.add_message(request, messages.WARNING, '登陆失败,请确认账户密码正确')
        else:
            messages.add_message(request, messages.INFO, '请输入完整有效的信息')
    else:
        login_form = forms.LoginForm()
    return render(request, "login.html", locals())


@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
    user = User.objects.get(username=username)
    if user.type == 0:
        ty = "志愿者"
    elif user.type == 1:
        ty = "培训方"
    else:
        ty = "招募方"
    if request.method == "POST":
        profile_form = forms.ProfileForm(request.POST, instance=user)
        if profile_form.is_valid():
            messages.add_message(request, messages.INFO, "个人资料已储存")
            profile_form.save()
            return HttpResponseRedirect('../userinfo/')
        else:
            messages.add_message(request, messages.INFO, '请填入完整信息')
    else:
        profile_form = forms.ProfileForm()
    return render(request, 'userinfo.html', locals())
