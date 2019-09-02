from django import forms
class Contactform(forms.Form):
    user_name=forms.CharField(label="你的姓名",max_length=30,initial="匿名网友")
    user_work=forms.CharField(label="你的职业",max_length=50,initial="未知")
    user_email=forms.EmailField(label="电子邮件")
    user_message=forms.CharField(label="你的意见",widget=forms.Textarea)
