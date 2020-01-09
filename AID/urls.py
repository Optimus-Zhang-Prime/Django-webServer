from django.conf.urls import re_path
from . import views

urlpatterns = [re_path('read/', views.showdata),
               re_path('seeActivity/', views.seeActivity),
               re_path('writeTrainActivity/', views.writeTrainActivity),
               re_path('writeRecruitActivity/', views.writeRecruitActivity),
               re_path('signuptrain(\d+)/', views.signUpTrain),
               re_path('signuprecruit(\d+)/', views.signUpRecruit),
               re_path('manageActivity(\d+)/',views.manageTrainActivity),
               re_path('userinfo/', views.userinfo),
               re_path('logout/', views.logout),
               re_path(r'', views.homePage),
               ]
