from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms
from django.shortcuts import render, redirect
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth import authenticate  # 用户验证
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TrainActivity, TrainJoinedUserList, TrainSignupUserList
from users.models import User


def homePage(request):
    return render(request, "yingjian.html")


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


def seeActivity(request):
    if request.user.is_authenticated:
        username = request.user.username
    TrainActivity = models.TrainActivity.objects.all().filter(enable=True).order_by('-createDate')
    tdic = {}  # 显示培训活动
    for tr in TrainActivity:
        t = tr.User.all().filter(type=1)[0]
        tdic[tr] = t.username
    RecruitActivity = models.RecruitActivity.objects.all().filter(enable=True).order_by('-createDate')
    rdic = {}  # 显示招募活动
    for rc in RecruitActivity:
        r = rc.User.all().filter(type=1)[0]
        rdic[rc] = r.username
    return render(request, "SeeActivity.html", locals())


@login_required()
def manageTrainActivity(request, id):
    trainActivity = models.TrainActivity.objects.get(pk=id)
    if request.user.is_authenticated:
        username = request.user.username
        manager = User.objects.filter(trainactivity=trainActivity)[0]
        if request.user.type == 1 and manager.username == username:
            list = TrainSignupUserList.objects.get(Activity=trainActivity)
            allsignupUserlist = User.objects.filter(trainsignupuserlist=list)
        else:
            messages.add_message(request, messages.INFO, "您没有权限对该活动进行管理")
    return render(request, "manageTrainActivity.html", {"allsignupUserlist": allsignupUserlist})


@login_required()
def signUpTrain(request, id):
    trainActivity = models.TrainActivity.objects.get(pk=id)
    if request.user.is_authenticated:
        username = request.user.username
    try:
        user = User.objects.get(username=username)
        signuplist = TrainSignupUserList.objects.get(Activity=trainActivity)
        signuplist.SignUser.add(user)
        messages.add_message(request, messages.INFO, "报名成功,请等待主办方审核，完善您的个人资料将有利于审核通过")
    except:
        messages.add_message(request, messages.INFO, "报名失败")
    return redirect('/1')


@login_required()
def signUpRecruit(request, id):
    recruitActivity = models.TrainActivity.objects.get(pk=id)
    if request.user.is_authenticated:
        username = request.user.username
    try:
        user = User.objects.get(username=username)
        recruitActivity.User.add(user)
        messages.add_message(request, messages.INFO, "报名成功,请等待招募方审核，完善您的个人资料将有利于审核通过")
    except:
        messages.add_message(request, messages.INFO, "报名失败")
    return redirect('/1')


@login_required(login_url='/login/')
def logout(request):
    if request.user.is_authenticated:
        username = request.user.username
    auth.logout(request)
    messages.add_message(request, messages.INFO, "退出登录成功")
    return redirect("/login/")


def login(request):
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
                    return redirect('/')
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


@login_required(login_url='/login/')
def writeRecruitActivity(request):
    if request.user.is_authenticated:
        username = request.user.username
    messages.get_messages(request)
    if request.method == 'POST':
        user = User.objects.get(username=username)
        if user.type == 2:
            recruitActivity = models.RecruitActivity(User=user)
            form = forms.RecruitActivityForm(request.POST, instance=trainActivity)
            if form.isvalid():
                messages.add_message(request, messages.INFO, "招募活动已发布")
                form.save()
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.INFO, "内容不完整")
        else:
            messages.add_message(request, messages.INFO, "权限错误")
    else:
        form = forms.TrainActivityForm()
    return render(request, 'write.html', locals())


@login_required(login_url='/login/')
def writeTrainActivity(request):
    if request.user.is_authenticated:
        username = request.user.username
    messages.get_messages(request)
    if request.method == 'POST':
        user = User.objects.get(username=username)
        if user.type == 1:
            trainActivity = models.TrainActivity.objects.create()
            trainActivity.User.add(user)
            form = forms.TrainActivityForm(request.POST, instance=trainActivity)
            if form.is_valid():
                signList = TrainSignupUserList.objects.create(Activity=trainActivity)
                messages.add_message(request, messages.INFO, "培训活动已发布")
                form.save()
                signList.save()
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.INFO, "内容不完整")
        else:
            messages.add_message(request, messages.INFO, "权限错误")
    else:
        form = forms.TrainActivityForm()

    return render(request, 'write.html', locals())


'''
def homePage(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        ans = 0
        if user.type == 2:
            ans = 1
    messages.get_messages(request)
    return render(request, "homePage.html", locals())
'''

