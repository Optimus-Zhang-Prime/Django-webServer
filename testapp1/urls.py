from django.conf.urls import url
from . import views

# url管理器将网址信息与url配置逐个匹配
urlpatterns = [url(r'^$', views.homePage),
               url(r'^(\d+)$', views.classStu),  # views的方法不接括号
               url(r'^addClass/$', views.addClass), ]
