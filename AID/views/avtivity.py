from django.http import HttpResponseRedirect
from AID import models, forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
        try:
            r = rc.User.all().filter(type=2)[0]
            rdic[rc] = r.username
        except:
            rdic[rc] = "活动已失效"
    return render(request, "SeeActivity.html", locals())


@login_required()
def myActivity(request):  # 已报名的活动
    username = request.user.username
    try:
        trainlist = models.UserSignupTrainList.objects.get(User=request.user)
        trainActivity = trainlist.TrainActivity.all()
    except:
        messages.add_message(request, messages.INFO, "您还没有报名培训活动")
    try:
        recruitlist = models.UserSignupRecruitList.objects.get(User=request.user)
        recruitActivity = recruitlist.RecruitActivity.all()
    except:
        messages.add_message(request, messages.INFO, "您还没有报名招募活动")
    return render(request, "myActivity.html", locals())


@login_required()
def manageTrainActivity(request, id):  # 培训活动发布者管理报名人员
    trainActivity = models.TrainActivity.objects.get(pk=id)
    username = request.user.username
    manager = User.objects.filter(trainactivity=trainActivity)[0]
    if request.user.type == 1 and manager.username == username:  # 判断是否是该活动的发起者
        list = models.TrainSignupUserList.objects.get(Activity=trainActivity)
        userlist = list.SignUser.all()
        # allsignupUserlist = User.objects.filter(trainsignupuserlist=list)
    else:
        messages.add_message(request, messages.INFO, "您没有权限对该活动进行管理")
    return render(request, "manageTrainActivity.html", locals())


@login_required()
def manageRecruitActivity(request, id):  # 招募活动发布者管理报名人员
    recruitActivity = models.RecruitActivity.objects.get(pk=id)
    username = request.user.username
    manager = User.objects.filter(recruitactivity=recruitActivity)[0]
    if request.user.type == 2 and manager.username == username:
        list = models.RecruitSignupUserList.objects.get(Activity=recruitActivity)
        allsignupUserlist = User.objects.filter(recruitsignupuserlist=list)
    else:
        messages.add_message(request, messages.INFO, "您没有权限对该活动进行管理")
    return render(request, "manageTrainActivity.html", locals())


def trainRatify(request, actID, userID):
    try:
        joinUser = User.objects.get(pk=userID)
        activity = models.TrainActivity.objects.get(pk=actID)
        try:
            joinedList = models.TrainJoinedUserList.objects.get(Activity=activity)
        except:
            joinedList = models.TrainJoinedUserList.objects.create(Activity=activity)
        joinedList.SignUser.add(joinUser)
        messages.add_message(request, messages.INFO, "成功")
        return HttpResponseRedirect("../../../aid/seeActivity/")
    except:
        messages.add_message(request, messages.INFO, "失败")
        return HttpResponseRedirect("../../../aid/seeActivity/")


def recruitRatify(request, actID, userID):
    try:
        joinUser = User.objects.get(pk=userID)
        activity = models.RecruitActivity.objects.get(pk=actID)
        try:
            joinedList = models.RecruitJoinedUserList.objects.get(Activity=activity)
        except:
            joinedList = models.RecruitJoinedUserList.objects.create(Activity=activity)
        joinedList.SignUser.add(joinUser)
        messages.add_message(request, messages.INFO, "成功")
        return HttpResponseRedirect("../../../aid/seeActivity/")
    except:
        messages.add_message(request, messages.INFO, "失败")
        return HttpResponseRedirect("../../../aid/seeActivity/")


@login_required()
def signUpTrain(request, id):  # 志愿者报名培训活动
    username = request.user.username
    try:
        trainActivity = models.TrainActivity.objects.get(pk=id)
        Trainsignuplist = models.TrainSignupUserList.objects.get(Activity=trainActivity)
        Trainsignuplist.SignUser.add(request.user)
        try:
            Usersignuplist = models.UserSignupTrainList.objects.get(User=request.user)
        except:
            Usersignuplist = models.UserSignupTrainList.objects.create(User=request.user)
        Usersignuplist.TrainActivity.add(trainActivity)
        messages.add_message(request, messages.INFO, "报名成功,请等待主办方审核，完善您的个人资料将有利于审核通过")
    except:
        messages.add_message(request, messages.INFO, "报名失败")
    return redirect('/aid/seeActivity/')


@login_required()
def signUpRecruit(request, id):
    username = request.user.username
    try:
        recruitActivity = models.RecruitActivity.objects.get(pk=id)
        Recruitsignuplist = models.RecruitSignupUserList.objects.get(Activity=recruitActivity)
        Recruitsignuplist.SignUser.add(request.user)
        try:
            Usersignuplist = models.UserSignupRecruitList.objects.get(User=request.user)
        except:
            # 没有则重新创建
            Usersignuplist = models.UserSignupRecruitList.objects.create(User=request.user)
        Usersignuplist.RecruitActivity.add(recruitActivity)
        messages.add_message(request, messages.INFO, "报名成功,请等待主办方审核，完善您的个人资料将有利于审核通过")
    except:
        messages.add_message(request, messages.INFO, "报名失败")
    return redirect('/aid/seeActivity/')


@login_required(login_url='/login/')
def writeTrainActivity(request):
    username = request.user.username
    messages.get_messages(request)
    if request.method == 'POST':
        user = request.user
        if user.type == 1:
            trainActivity = models.TrainActivity.objects.create()
            trainActivity.User.add(user)
            form = forms.TrainActivityForm(request.POST, instance=trainActivity)
            if form.is_valid():
                signList = models.TrainSignupUserList.objects.create(Activity=trainActivity)
                messages.add_message(request, messages.INFO, "培训活动已发布")
                form.save()
                signList.save()
                return HttpResponseRedirect('../../aid/seeActivity/')
            else:
                messages.add_message(request, messages.INFO, "内容不完整")
        else:
            messages.add_message(request, messages.INFO, "权限不足")
    else:
        form = forms.TrainActivityForm()
    return render(request, 'write.html', locals())


@login_required(login_url='/login/')
def writeRecruitActivity(request):
    username = request.user.username
    messages.get_messages(request)
    if request.method == 'POST':
        user = request.user
        if user.type == 2:
            recruitActivity = models.RecruitActivity.objects.create()
            recruitActivity.User.add(user)
            form = forms.RecruitActivityForm(request.POST, instance=recruitActivity)
            if form.is_valid():
                signList = models.RecruitSignupUserList.objects.create(Activity=recruitActivity)
                messages.add_message(request, messages.INFO, "招募活动已发布")
                form.save()
                signList.save()
                return HttpResponseRedirect('../../aid/seeActivity/')
            else:
                messages.add_message(request, messages.INFO, "内容不完整")
        else:
            messages.add_message(request, messages.INFO, "权限不足")
    else:
        form = forms.RecruitActivityForm()
    return render(request, 'write.html', locals())
