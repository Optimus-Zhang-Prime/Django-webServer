from django.conf.urls import re_path
from . import views
urlpatterns = [re_path('^$', views.data),
              re_path('haha',views.haha),
               re_path('see',views.see)]