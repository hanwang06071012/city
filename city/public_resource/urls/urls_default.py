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
from public_resource.views import (
    PublicResourceReginoanlListView,
    PublicResourceReginoanlCreateView,
    PublicResourceReginoanlUpdateView,
    PublicResourceReginoanlDetailView,
    PublicResourceChineseUniversitiesListView,
    PublicResourceChineseUniversitiesCreateView,
    PublicResourceChineseUniversitiesUpdateView,
    PublicResourceChineseUniversitiesDetailView,
    PublicResourceOverView,
)
urlpatterns = [
    url(r'^overview/', PublicResourceOverView.as_view(), name='public_resource_overview'),
    url(r'^reginoanl/list/', PublicResourceReginoanlListView.as_view(), name='public_resource_reginoanl_list'),
    url(r'^reginoanl/create/', PublicResourceReginoanlCreateView.as_view(), name='public_resource_reginoanl_create'),
    url(r'^reginoanl/(?P<id>[0-9]+)/update/', PublicResourceReginoanlUpdateView.as_view(), name='public_resource_reginoanl_update'),
    url(r'^reginoanl/(?P<id>[0-9]+)/detail/', PublicResourceReginoanlDetailView.as_view(), name='public_resource_reginoanl_detail'),
    url(r'^chinese/universities/list/', PublicResourceChineseUniversitiesListView.as_view(), name='public_resource_chinese_universities_list'),
    url(r'^chinese/universities/create/', PublicResourceChineseUniversitiesCreateView.as_view(), name='public_resource_chinese_universities_create'),
    url(r'^chinese/universities/(?P<id>[0-9]+)/update/', PublicResourceChineseUniversitiesUpdateView.as_view(), name='public_resource_chinese_universities_update'),
    url(r'^chinese/universities/(?P<id>[0-9]+)/detail/', PublicResourceChineseUniversitiesDetailView.as_view(), name='public_resource_chinese_universities_detail'),
]
