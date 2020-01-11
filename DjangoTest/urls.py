
# url声明
"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from AID import views
import video
# django2.0一般不用正则


urlpatterns = [


    url(r'^aid/',include('AID.urls')),
    url(r'^admin/', admin.site.urls),  # 管理员
    url(r'^captcha/',include('captcha.urls')),#验证码
    url('login/',views.login),
    url('accounts/',include('registration.backends.default.urls')),
    url('video/', include('video.urls')),
    url(r'^myadmin/', include('myadmin.urls')),
    url('users/', include('users.urls')),
    url('comment/', include('comment.urls')),
    url('^calculater/',include('calculater.urls')),
 ]
