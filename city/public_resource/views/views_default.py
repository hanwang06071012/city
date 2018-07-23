# -*- coding:utf-8 -*-
"""数据库管理通用视图."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库公共资源管理模块
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from utils.common_lib import CommonMixin, LoginRequiredMixin
from public_resource.models import ReginoanlManagement
from django.db.models import Q
from public_resource.forms import ReginoanlCreateForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


class PublicResourceReginoanlListView(LoginRequiredMixin, CommonMixin, ListView):
    """行政区划列表"""

    model = ReginoanlManagement
    template_name = "default/public_resource_reginoanl_list.html"
    page_title = "行政区划列表"
    paginate_by = '10'
    context_object_name = 'public_resource_reginoanl_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        user_manager_reginoanl_objs = ReginoanlManagement.objects
        if name:
            user_manager_reginoanl_objs = user_manager_reginoanl_objs.filter(Q(province__contains=name) | Q(city__contains=name) | Q(county__contains=name))
        return user_manager_reginoanl_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(PublicResourceReginoanlListView, self).get_context_data(**kwargs)
        return context


class PublicResourceReginoanlCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """行政区划创建."""

    template_name = 'default/public_resource_reginoanl_create.html'
    page_title = '行政区划创建'
    form_class = ReginoanlCreateForm
    success_url = reverse_lazy('publicresourcedefault:public_resource_reginoanl_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(PublicResourceReginoanlCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            province = request.POST.get('province')
            city = request.POST.get('city')
            county = request.POST.get('county')
            people = request.POST.get('people', '0')
            description = request.POST.get('description', '')
            ReginoanlManagement.objects.create(province=province, city=city, county=county, people=people, description=description)
        except Exception as e:
            raise e
        return HttpResponseRedirect(self.success_url)
