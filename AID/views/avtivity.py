from django.http import HttpResponseRedirect
from AID import models, forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from AID.models import TrainActivity, TrainJoinedUserList, TrainSignupUserList
from users.models import User


def seeActivity(request):  # 显示培训和招募活动
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
def manageTrainActivity(request, id):  # 培训活动发布者管理报名人员
    trainActivity = models.TrainActivity.objects.get(pk=id)
    if request.user.is_authenticated:
        username = request.user.username
        manager = User.objects.filter(trainactivity=trainActivity)[0]
        if request.user.type == 1 and manager.username == username:
            list = TrainSignupUserList.objects.get(Activity=trainActivity)
            allsignupUserlist = User.objects.filter(trainsignupuserlist=list)
        else:
            messages.add_message(request, messages.INFO, "您没有权限对该活动进行管理")
    return render(request, "manageTrainActivity.html", locals())


@login_required()
def manageRecruitActivity(request, id):  # 招募活动发布者管理报名人员
    recruitActivity = models.RecruitActivity.objects.get(pk=id)
    if request.user.is_authenticated:
        username = request.user.username
        manager = User.objects.filter(recruitactivity=recruitActivity)[0]
        if request.user.type == 1 and manager.username == username:
            list = TrainSignupUserList.objects.get(Activity=recruitActivity)
            allsignupUserlist = User.objects.filter(recruitsignupuserlist=list)
        else:
            messages.add_message(request, messages.INFO, "您没有权限对该活动进行管理")
    return render(request, "manageTrainActivity.html", locals())


@login_required()
def signUpTrain(request, id):  # 志愿者报名培训活动
    trainActivity = models.TrainActivity.objects.get(pk=id)
    username = request.user.username
    user = User.objects.get(username=username)
    Trainsignuplist = TrainSignupUserList.objects.get(Activity=trainActivity)
    Trainsignuplist.SignUser.add(user)
    try:
        Usersignuplist = models.UserSignupTrainList.objects.get(User=user)
    except:
        Usersignuplist = models.UserSignupTrainList()
        Usersignuplist.User = user
    #messages.add_message(request, messages.INFO, "报名失败1")
    Usersignuplist.TrainActivity.add(trainActivity)
    #messages.add_message(request, messages.INFO, "报名成功,请等待主办方审核，完善您的个人资料将有利于审核通过")
    #messages.add_message(request, messages.INFO, "报名失败")
    return redirect('/aid/seeActivity/')


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
    return redirect('/aid/seeActivity/')


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


@login_required(login_url='/login/')
def writeRecruitActivity(request):
    if request.user.is_authenticated:
        username = request.user.username
    messages.get_messages(request)
    if request.method == 'POST':
        user = User.objects.get(username=username)
        if user.type == 2:
            recruitActivity = models.RecruitActivity(User=user)
            form = forms.RecruitActivityForm(request.POST, instance=recruitActivity)
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
