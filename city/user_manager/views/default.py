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
from user_manager.models import CityAuthUser
from user_manager.forms import UserCreateForm
from utils import EasyAndDateTimeConversion
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from utils import CommonMixin
import time


class UserManagerUserListView(CommonMixin, ListView):
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


class UserManagerUserCreateView(CommonMixin, CreateView):
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
        is_superuser = request.POST.get('is_superuser', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        qq = request.POST.get('qq', '')
        is_staff = request.POST.get('is_staff', '')
        is_active = request.POST.get('is_active', '')
        date_joined = request.POST.get('date_joined', '')
        date_joined = EasyAndDateTimeConversion.easy_to_datetime(date_joined)
        description = request.POST.get('description', '')
        last_login = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        CityAuthUser.objects.create(username=username, password=password, is_superuser=is_superuser, first_name=first_name, last_name=last_name, email=email, phone=phone, qq=qq, is_staff=is_staff, is_active=is_active, date_joined=date_joined, description=description, last_login=last_login)
        return HttpResponseRedirect(self.success_url)


class UserManagerUserDetailView(CommonMixin, DetailView):
    """用户详情展示."""

    model = CityAuthUser
    page_title = '用户详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/user_manager_user_detail.html"
    context_object_name = "user_manager_user_obj"


class UserManagerUserUpdateView(CommonMixin, View):
    """用户数据更新."""

    page_title = '用户详情'
    template_name = "default/user_manager_user_update.html"
    success_url = reverse_lazy('usermanagerdefault:user_manager_user_list')

    def get(self, request, *args, **kwargs):
        print("========get start========================")
        id = self.kwargs.get('id')
        user_manager_user_obj = CityAuthUser.objects.filter(id=id).first()
        print("========get end=============================")
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        print("========post start========================")
        id = self.kwargs.get('id')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        is_superuser = request.POST.get('is_superuser', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        qq = request.POST.get('qq', '')
        is_staff = request.POST.get('is_staff', '')
        is_active = request.POST.get('is_active', '')
        date_joined = request.POST.get('date_joined', '')
        date_joined = EasyAndDateTimeConversion.easy_to_datetime(date_joined)
        description = request.POST.get('description', '')
        last_login = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        CityAuthUser.objects.filter(id=id).update(username=username, password=password, is_superuser=is_superuser, first_name=first_name, last_name=last_name, email=email, phone=phone, qq=qq, is_staff=is_staff, is_active=is_active, date_joined=date_joined, description=description, last_login=last_login)
        print(is_active)
        print("========get end========================")
        return HttpResponseRedirect(self.success_url)
