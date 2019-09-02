from django import forms
class Contactform(forms.Form):
    user_name=forms.CharField(label="您的姓名",max_length=30,initial="填写您的昵称")
    user_work=forms.CharField(label="您的职业",max_length=50)
    user_email=forms.EmailField(label="电子邮件")
    user_message=forms.CharField(label="您的意见",widget=forms.Textarea)
