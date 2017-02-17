"""MCQ_SITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from MCQ.views import log_in,my_page,log_out,give_exam,submit_exam

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',log_in,name='log_in'),
    url(r'^my_page/$',my_page,name='my_page'),
    url(r'^log_out/$',log_out,name='log_out'),
    url(r'^exam/(\D+)/$',give_exam,name='give_exam'),
    url(r'^submit_exam/(\D+)/$',submit_exam,name='submit_exam'),
]
