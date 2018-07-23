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
from user_manager.views import UserManagerOverView
from user_manager.views import UserManagerUserListView, UserManagerUserCreateView
from user_manager.views import UserManagerUserDetailView, UserManagerUserUpdateView
from user_manager.views import UserManagerGroupListView, UserManagerGroupCreateView
from user_manager.views import UserManagerGroupUpdateView, UserManagerGroupDetailView
from user_manager.views import UserManagerRoleListView, UserManagerRoleCreateView, UserManagerRoleUpdateView
from user_manager.views import UserManagerPermissionListView, UserManagerPermissionCreateView
from user_manager.views import UserManagerPermissionUpdateView, UserManagerPermissionDetailView


urlpatterns = [
    url(r'^user/manager/overview/', UserManagerOverView.as_view(), name='user_manager_overview'),
    url(r'^user/list/', UserManagerUserListView.as_view(), name='user_manager_user_list'),
    url(r'^user/create/', UserManagerUserCreateView.as_view(), name='user_manager_user_create'),
    url(r'^user/(?P<id>[a-z-\d]+)/detail/$', UserManagerUserDetailView.as_view(), name='user_manager_user_detail'),
    url(r'^user/(?P<id>[a-z-\d]+)/update/$', UserManagerUserUpdateView.as_view(), name='user_manager_user_update'),
    url(r'^group/list/', UserManagerGroupListView.as_view(), name='user_manager_group_list'),
    url(r'^group/create/', UserManagerGroupCreateView.as_view(), name='user_manager_group_create'),
    url(r'^group/(?P<id>[a-z-\d]+)/detail/$', UserManagerGroupDetailView.as_view(), name='user_manager_group_detail'),
    url(r'^group/(?P<id>[a-z-\d]+)/update/$', UserManagerGroupUpdateView.as_view(), name='user_manager_group_update'),
    url(r'^role/list/', UserManagerRoleListView.as_view(), name='user_manager_role_list'),
    url(r'^role/create/', UserManagerRoleCreateView.as_view(), name='user_manager_role_create'),
    url(r'^role/(?P<id>[a-z-\d]+)/update/$', UserManagerRoleUpdateView.as_view(), name='user_manager_role_update'),
    url(r'^permission/list/', UserManagerPermissionListView.as_view(), name='user_manager_permission_list'),
    url(r'^permission/create/', UserManagerPermissionCreateView.as_view(), name='user_manager_permission_create'),
    url(r'^permission/(?P<id>[a-z-\d]+)/update/$', UserManagerPermissionUpdateView.as_view(), name='user_manager_permission_update'),
    url(r'^permission/(?P<id>[a-z-\d]+)/detail/$', UserManagerPermissionDetailView.as_view(), name='user_manager_permission_detail'),
]
