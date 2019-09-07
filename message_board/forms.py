from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    user_name = forms.CharField(label="您的姓名", max_length=30, initial="填写您的昵称")
    user_work = forms.CharField(label="您的职业", max_length=50)
    user_email = forms.EmailField(label="电子邮件")
    user_message = forms.CharField(label="您的意见", widget=forms.Textarea)
    cap = CaptchaField(label="验证码")


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
