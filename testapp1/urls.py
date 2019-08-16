from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.showClasses),
               url(r'^(\d+)$',views.classStu),]
