# -*- coding:utf-8 -*-
"""数据库管理通用视图."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库通用视图
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from user_manager.models import CityAuthUser, CityAuthGroup, CityAuthRole, CityAuthPermission
from user_manager.forms import UserCreateForm, GroupCreateForm, RoleCreateForm, PermissionCreateForm
from user_manager.forms import PermissionCreateForm
from utils.common_lib import EasyAndDateTimeConversion, LoginRequiredMixin
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from utils.common_lib import CommonMixin
import time
import logging

_log = logging.getLogger(__name__)


class UserManagerOverView(LoginRequiredMixin, CommonMixin, View):
    """用户概况"""

    template_name = "default/user_manager_overview.html"
    page_title = "用户概况"

    def get(self, request, *args, **kwargs):
        """重写."""
        user_num = CityAuthUser.objects.all().count()
        group_num = CityAuthGroup.objects.all().count()
        role_num = CityAuthRole.objects.all().count()
        permission_num = CityAuthPermission.objects.all().count()
        return render(request, self.template_name, locals())


class UserManagerUserListView(LoginRequiredMixin, CommonMixin, ListView):
    """用户列表"""

    model = CityAuthUser
    template_name = "default/user_manager_user_list.html"
    page_title = "用户列表"
    paginate_by = '10'
    context_object_name = 'user_manager_user_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        user_manager_user_objs = CityAuthUser.objects
        if name:
            user_manager_user_objs = user_manager_user_objs.filter(Q(username__contains=name) | Q(last_name__contains=name) | Q(first_name__contains=name))
        return user_manager_user_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(UserManagerUserListView, self).get_context_data(**kwargs)
        return context


class UserManagerUserCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """用户创建."""

    template_name = 'default/user_manager_user_create.html'
    page_title = '用户创建'
    form_class = UserCreateForm
    success_url = reverse_lazy('usermanagerdefault:user_manager_user_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(UserManagerUserCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        is_superuser = int(request.POST.get('is_superuser', '0'))
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        qq = request.POST.get('qq', '')
        is_staff = int(request.POST.get('is_staff', '0'))
        is_active = int(request.POST.get('is_active', '0'))
        date_joined = request.POST.get('date_joined', '')
        date_joined = EasyAndDateTimeConversion.easy_to_datetime(date_joined)
        description = request.POST.get('description', '')
        last_login = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        CityAuthUser.objects.create(username=username, password=password, is_superuser=is_superuser, first_name=first_name, last_name=last_name, email=email, phone=phone, qq=qq, is_staff=is_staff, is_active=is_active, date_joined=date_joined, description=description, last_login=last_login)
        return HttpResponseRedirect(self.success_url)


class UserManagerUserDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """用户详情展示."""

    model = CityAuthUser
    page_title = '用户详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/user_manager_user_detail.html"
    context_object_name = "user_manager_user_obj"


class UserManagerUserUpdateView(LoginRequiredMixin, CommonMixin, View):
    """用户数据更新."""

    page_title = '用户详情'
    template_name = "default/user_manager_user_update.html"
    success_url = reverse_lazy('usermanagerdefault:user_manager_user_list')

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user_manager_user_obj = CityAuthUser.objects.filter(id=id).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        is_superuser = int(request.POST.get('is_superuser', '0'))
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        qq = request.POST.get('qq', '')
        is_staff = int(request.POST.get('is_staff', '0'))
        is_active = int(request.POST.get('is_active', ''))
        date_joined = request.POST.get('date_joined', '')
        date_joined = EasyAndDateTimeConversion.easy_to_datetime(date_joined)
        description = request.POST.get('description', '')
        last_login = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        CityAuthUser.objects.filter(id=id).update(username=username, password=password, is_superuser=is_superuser, first_name=first_name, last_name=last_name, email=email, phone=phone, qq=qq, is_staff=is_staff, is_active=is_active, date_joined=date_joined, description=description, last_login=last_login)
        return HttpResponseRedirect(self.success_url)


class UserManagerGroupListView(LoginRequiredMixin, CommonMixin, ListView):
    """组列表"""

    model = CityAuthGroup
    template_name = "default/user_manager_group_list.html"
    page_title = "组列表"
    paginate_by = '10'
    context_object_name = 'user_manager_group_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        user_manager_group_objs = CityAuthGroup.objects
        if name:
            user_manager_group_objs = user_manager_group_objs.filter(Q(name__contains=name))
        return user_manager_group_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(UserManagerGroupListView, self).get_context_data(**kwargs)
        return context


class UserManagerGroupCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """组创建."""

    template_name = 'default/user_manager_group_create.html'
    page_title = '组创建'
    form_class = GroupCreateForm
    success_url = reverse_lazy('usermanagerdefault:user_manager_group_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(UserManagerGroupCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            is_active = int(request.POST.get('is_active', '0'))
            description = request.POST.get('description', '')
            CityAuthGroup.objects.create(name=name, is_active=is_active, description=description)
        except Exception as e:
            print(e)
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class UserManagerGroupDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """组详情展示."""

    model = CityAuthGroup
    page_title = '组详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/user_manager_group_detail.html"
    context_object_name = "user_manager_group_obj"


class UserManagerGroupUpdateView(LoginRequiredMixin, CommonMixin, View):
    """组数据更新."""

    page_title = '组更新'
    template_name = "default/user_manager_group_update.html"
    success_url = reverse_lazy('usermanagerdefault:user_manager_group_list')

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user_manager_group_obj = CityAuthGroup.objects.filter(id=id).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        name = request.POST.get('name')
        is_active = int(request.POST.get('is_active', '0'))
        description = request.POST.get('description', '')
        CityAuthGroup.objects.filter(id=id).update(name=name, is_active=is_active, description=description)
        return HttpResponseRedirect(self.success_url)


class UserManagerRoleListView(LoginRequiredMixin, CommonMixin, ListView):
    """角色列表"""

    model = CityAuthGroup
    template_name = "default/user_manager_role_list.html"
    page_title = "角色列表"
    paginate_by = '10'
    context_object_name = 'user_manager_role_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        user_manager_role_objs = CityAuthRole.objects
        if name:
            user_manager_role_objs = user_manager_role_objs.filter(Q(name__contains=name))
        return user_manager_role_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(UserManagerRoleListView, self).get_context_data(**kwargs)
        return context


class UserManagerRoleCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """角色创建."""

    template_name = 'default/user_manager_role_create.html'
    page_title = '角色创建'
    form_class = RoleCreateForm
    success_url = reverse_lazy('usermanagerdefault:user_manager_role_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(UserManagerRoleCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            description = request.POST.get('description', '')
            CityAuthRole.objects.create(name=name, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class UserManagerRoleUpdateView(LoginRequiredMixin, CommonMixin, View):
    """角色更新."""

    page_title = '角色更新'
    template_name = "default/user_manager_role_update.html"
    success_url = reverse_lazy('usermanagerdefault:user_manager_role_list')

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user_manager_role_obj = CityAuthRole.objects.filter(id=id).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            id = self.kwargs.get('id')
            name = request.POST.get('name')
            description = request.POST.get('description', '')
            CityAuthRole.objects.filter(id=id).update(name=name, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class UserManagerPermissionListView(LoginRequiredMixin, CommonMixin, ListView):
    """权限列表"""

    model = CityAuthPermission
    template_name = "default/user_manager_permission_list.html"
    page_title = "权限列表"
    paginate_by = '10'
    context_object_name = 'user_manager_permission_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        user_manager_permission_objs = CityAuthPermission.objects
        if name:
            user_manager_permission_objs = user_manager_permission_objs.filter(Q(name__contains=name))
        return user_manager_permission_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(UserManagerPermissionListView, self).get_context_data(**kwargs)
        return context


class UserManagerPermissionCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """权限创建."""

    template_name = 'default/user_manager_permission_create.html'
    page_title = '权限创建'
    form_class = PermissionCreateForm
    success_url = reverse_lazy('usermanagerdefault:user_manager_permission_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(UserManagerPermissionCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        """重新加入点内容."""
        context = super(UserManagerPermissionCreateView, self).get_context_data(**kwargs)
        user_manager_permission_objs = CityAuthPermission.objects.all()
        context['user_manager_permission_objs'] = user_manager_permission_objs
        return context

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            url = request.POST.get('url', '')
            parent_node = request.POST.get('parent_node')
            description = request.POST.get('description', '')
            CityAuthPermission.objects.create(name=name, url=url, parent_node=parent_node, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class UserManagerPermissionUpdateView(LoginRequiredMixin, CommonMixin, View):
    """权限更新."""

    page_title = '权限更新'
    template_name = "default/user_manager_permission_update.html"
    success_url = reverse_lazy('usermanagerdefault:user_manager_permission_list')

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user_manager_permission_objs = CityAuthPermission.objects.all()
        user_manager_permission_obj = user_manager_permission_objs.filter(id=id).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            id = self.kwargs.get('id')
            name = request.POST.get('name')
            url = request.POST.get('url', '')
            parent_node = request.POST.get('parent_node')
            description = request.POST.get('description', '')
            CityAuthPermission.objects.filter(id=id).update(name=name, url=url, parent_node=parent_node, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class UserManagerPermissionDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """权限详情展示."""

    model = CityAuthPermission
    page_title = '权限详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/user_manager_permission_detail.html"
    context_object_name = "user_manager_permission_obj"

    def get_context_data(self, **kwargs):
        """重新加入点内容."""
        context = super(UserManagerPermissionDetailView, self).get_context_data(**kwargs)
        try:
            pid = self.kwargs.get('id')
            user_manager_permission_obj = CityAuthPermission.objects.filter(id=pid).first()
            parent_node = user_manager_permission_obj.parent_node
            user_manager_permission_parent_obj = CityAuthPermission.objects.filter(id=parent_node).first()
            context['user_manager_permission_parent_obj'] = user_manager_permission_parent_obj
        except Exception as e:
            context['user_manager_permission_parent_obj'] = 0
            _log.info(e)
        return context
