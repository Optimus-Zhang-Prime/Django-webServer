from django import forms
#from captcha.fields import CaptchaField
from .models import User, TrainActivity, RecruitActivity


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['gender', 'work', 'signature', "age","type"]

    type = forms.fields.ChoiceField(
        choices=((0, "志愿者"), (1, "培训方"), (2, "招募方"),),
        label="身份",
        widget=forms.widgets.Select()
    )
    gender = forms.fields.ChoiceField(
        choices=((0, "女生"), (1, "男生")),
        label="性别",
        widget=forms.widgets.Select()
    )
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['work'].label = "职业"
        self.fields['age'].label = "年龄"


        self.fields['signature'].label = "自我介绍"


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(label="密码", widget=forms.PasswordInput)


class Date(forms.DateInput):
    input_type = 'date'


class TrainActivityForm(forms.ModelForm):
    class Meta:
        model = TrainActivity
        fields = ['title', 'description', 'ActivityDate']
        widgets = {'ActivityDate': Date()}

    def __init__(self, *args, **kwargs):
        super(TrainActivityForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "主题"
        self.fields['description'].label = "详细介绍"
        self.fields['ActivityDate'].label = "日期"

class RecruitActivityForm(forms.ModelForm):
    class Meta:
        model = TrainActivity
        fields = ['title', 'description', 'ActivityDate']
        widgets = {'ActivityDate': Date()}

    def __init__(self, *args, **kwargs):
        super(RecruitActivityForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "主题"
        self.fields['description'].label = "详细介绍"
        self.fields['ActivityDate'].label = "日期"
