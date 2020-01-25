from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User


# Create your models here.
class test(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id', auto_created=True)
    do = models.FloatField(db_column='do')

    class Meta:
        db_table = 'test'


class yali(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id', auto_created=True)
    press = models.FloatField(db_column='press')

    class Meta:
        db_table = 'yali'


class message(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    sender = models.CharField(max_length=40)


class TrainActivity(models.Model):
    User = models.ManyToManyField(User)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=True)
    ActivityDate = models.DateField(null=True)
    createDate = models.DateField(auto_now_add=True)  # 创建活动的时间
    enable = models.BooleanField(default=True)  # 是否可用
    isAttest = models.BooleanField(default=False)  # 是否被认证


class TrainSignupUserList(models.Model):
    Activity = models.OneToOneField(TrainActivity, on_delete=models.CASCADE)
    SignUser = models.ManyToManyField(User)


class TrainJoinedUserList(models.Model):
    Activity = models.OneToOneField(TrainActivity, on_delete=models.CASCADE)
    SignUser = models.ManyToManyField(User)


class RecruitActivity(models.Model):
    User = models.ManyToManyField(User)
    title = models.CharField(max_length=50, null=False)
    ActivityDate = models.DateField(null=True)
    description = models.CharField(max_length=200, null=True)
    createDate = models.DateField(auto_now_add=True)  # 创建活动的时间
    enable = models.BooleanField(default=True)  # 是否可用
    isAttest = models.BooleanField(default=False)  # 是否被认证


class RecruitSignupUserList(models.Model):
    Activity = models.OneToOneField(RecruitActivity, on_delete=models.CASCADE)
    SignUser = models.ManyToManyField(User)


class RecruitJoinedUserList(models.Model):
    Activity = models.OneToOneField(TrainActivity, on_delete=models.CASCADE)
    SignUser = models.ManyToManyField(User)


class UserSignupTrainList(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    TrainActivity = models.ManyToManyField(TrainActivity)


class UserSignupRecruitList(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    RecruitActivity = models.ManyToManyField(RecruitActivity)
