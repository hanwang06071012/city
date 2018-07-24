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
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from utils.common_lib import CommonMixin, LoginRequiredMixin
from public_resource.models import ReginoanlManagement, ChineseUniversities
from django.db.models import Q
from public_resource.forms import ReginoanlCreateForm, ChineseUniversitiesCreateForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import logging

_log = logging.getLogger(__name__)


class PublicResourceOverView(LoginRequiredMixin, CommonMixin, View):
    """公共资源概况"""

    template_name = "default/public_resource_overview.html"
    page_title = "公共资源概况"

    def get(self, request, *args, **kwargs):
        """重写."""
        province_num = len(set(ReginoanlManagement.objects.values_list('province', flat=True)))
        city_num = len(set(ReginoanlManagement.objects.values_list('city', flat=True)))
        county_num = len(set(ReginoanlManagement.objects.values_list('county', flat=True)))
        return render(request, self.template_name, locals())


class PublicResourceReginoanlListView(LoginRequiredMixin, CommonMixin, ListView):
    """行政区划列表"""

    model = ReginoanlManagement
    template_name = "default/public_resource_reginoanl_list.html"
    page_title = "行政区划列表"
    paginate_by = '30'
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
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class PublicResourceReginoanlUpdateView(LoginRequiredMixin, CommonMixin, View):
    """行政区划更新."""

    template_name = 'default/public_resource_reginoanl_update.html'
    page_title = '行政区划更新'
    success_url = reverse_lazy('publicresourcedefault:public_resource_reginoanl_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        public_resource_reginoanl_obj = ReginoanlManagement.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            province = request.POST.get('province')
            city = request.POST.get('city')
            county = request.POST.get('county')
            people = request.POST.get('people', '0')
            description = request.POST.get('description', '')
            ReginoanlManagement.objects.filter(id=pid).update(province=province, city=city, county=county, people=people, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class PublicResourceReginoanlDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """行政区划详情展示."""

    model = ReginoanlManagement
    page_title = '行政区划详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/public_resource_reginoanl_detail.html"
    context_object_name = "public_resource_reginoanl_obj"


class PublicResourceChineseUniversitiesListView(LoginRequiredMixin, CommonMixin, ListView):
    """中国大学列表"""

    model = ChineseUniversities
    template_name = "default/public_resource_chinese_universities_list.html"
    page_title = "中国大学列表"
    paginate_by = '30'
    context_object_name = 'public_resource_chinese_universities_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        user_manager_chinese_universities_objs = ChineseUniversities.objects
        if name:
            user_manager_chinese_universities_objs = user_manager_chinese_universities_objs.filter(Q(name__contains=name) | Q(competent_authority__contains=name) | Q(location__contains=name) | Q(style__contains=name))
        return user_manager_chinese_universities_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(PublicResourceChineseUniversitiesListView, self).get_context_data(**kwargs)
        return context


class PublicResourceChineseUniversitiesCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """中国高校创建."""

    template_name = 'default/public_resource_chinese_universities_create.html'
    page_title = '中国高校创建'
    form_class = ChineseUniversitiesCreateForm
    success_url = reverse_lazy('publicresourcedefault:public_resource_chinese_universities_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(PublicResourceChineseUniversitiesCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            competent_authority = request.POST.get('competent_authority')
            location = request.POST.get('location')
            level = request.POST.get('level', '0')
            style = request.POST.get('style', '0')
            description = request.POST.get('description', '')
            ChineseUniversities.objects.create(name=name, competent_authority=competent_authority, location=location, level=level, style=style, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class PublicResourceChineseUniversitiesUpdateView(LoginRequiredMixin, CommonMixin, View):
    """中国高校更新."""

    template_name = 'default/public_resource_chinese_universities_update.html'
    page_title = '中国高校更新'
    success_url = reverse_lazy('publicresourcedefault:public_resource_chinese_universities_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        public_resource_chinese_universities_obj = ChineseUniversities.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            competent_authority = request.POST.get('competent_authority')
            location = request.POST.get('location')
            level = request.POST.get('level', '0')
            style = request.POST.get('style', '0')
            description = request.POST.get('description', '')
            ChineseUniversities.objects.filter(id=pid).update(name=name, competent_authority=competent_authority, location=location, level=level, style=style, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class PublicResourceChineseUniversitiesDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """中国高校详情展示."""

    model = ChineseUniversities
    page_title = '中国高校详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/public_resource_chinese_universities_detail.html"
    context_object_name = "public_resource_chinese_universities_obj"
