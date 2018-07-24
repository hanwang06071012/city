"""city URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from huntjob.views import HuntJobTestView
from huntjob.views import (
    HuntJobIndexListView,
    JobInformationDetailView,
    CompanyInformationDetailView,
    HuntJobCompanyScaleListView,
    HuntJobCompanyScaleCreateView,
)

urlpatterns = [
    url(r'^testview/', HuntJobTestView.as_view(), name='testview'),
    url(r'^index/', HuntJobIndexListView.as_view(), name='index'),
    url(r'^job/information/(?P<id>[0-9]+)/detail/', JobInformationDetailView.as_view(), name='job_information_detail'),
    url(r'^company/information/(?P<id>[0-9]+)/detail/', CompanyInformationDetailView.as_view(), name='company_information_detail'),
    url(r'^company/scale/list/', HuntJobCompanyScaleListView.as_view(), name='huntjob_company_scale_list'),
    url(r'^company/scale/create/', HuntJobCompanyScaleCreateView.as_view(), name='huntjob_company_scale_create'),
]
