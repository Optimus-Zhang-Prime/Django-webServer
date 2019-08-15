from django.urls import path
from . import views

urlpatterns = [path('', views.showClasses)]  # 转到视图
