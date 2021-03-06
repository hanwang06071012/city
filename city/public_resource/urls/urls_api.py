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
    PublicResourceReginoanlManagementView,
    PublicResourceChineseUniversitiesView,
)
urlpatterns = [
    url(r'^/reginoanls$', PublicResourceReginoanlManagementView.as_view(), name='public_resource_reginoanls'),
    url(r'^/reginoanls/(?P<pk>\d+)$', PublicResourceReginoanlManagementView.as_view(), name='public_resource_reginoanl'),
    url(r'^/chinese/universites$', PublicResourceChineseUniversitiesView.as_view(), name='public_resource_chinese_universities'),
    url(r'^/chinese/universites/(?P<pk>\d+)$', PublicResourceChineseUniversitiesView.as_view(), name='public_resource_chinese_university'),

]
