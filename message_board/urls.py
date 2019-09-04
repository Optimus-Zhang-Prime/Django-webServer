from django.conf.urls import re_path
from . import views

# url管理器将网址信息与url配置逐个匹配
urlpatterns = [re_path('write/', views.write),
               re_path('delete(\d+)/', views.dele),
               re_path('read/', views.read),
               re_path('contact/', views.contact),

               ]
