from django.conf.urls import url
from . import views

# url管理器将网址信息与url配置逐个匹配
urlpatterns = [url(r'^school/$', views.homePage),
               url(r'^school/allclasses/$',views.showClasses),
               url('school/<int:num>', views.classStu),  # views的方法不接括号
               url(r'^school/addClass/$', views.addClass), ]
