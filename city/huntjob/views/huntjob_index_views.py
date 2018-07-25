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

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView
from huntjob.models import (
    JobInformation,
    JobSalaryBenefitsRelationship,
    JobInformationFunctionsRelationship,
    CompanyInformation,
    CompanyScale,
    CompanyStyle,
    CompanyIndustry,
)
from utils.common_lib import CommonMixin, LoginRequiredMixin
from huntjob.forms import (
    CompanyScaleCreateForm,
    CompanyStyleCreateForm,
)
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
import logging

_log = logging.getLogger(__name__)


class HuntJobIndexListView(LoginRequiredMixin, CommonMixin, ListView):
    """岗位搜索展示默认页"""

    model = JobInformation
    template_name = "default/index.html"
    page_title = "职位列表"
    paginate_by = '10'
    context_object_name = 'job_infromations'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        job_infromations = JobInformation.objects
        if name:
            job_infromations = job_infromations.filter(Q(name__contains=name) | Q(work_place__contains=name) | Q(job_responsibilities__contains=name) | Q(job_requirements__contains=name))
        return job_infromations.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobIndexListView, self).get_context_data(**kwargs)
        return context


class JobInformationDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """岗位详情展示."""

    model = JobInformation
    page_title = '岗位详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/job_information_detail.html"
    context_object_name = "job_information"

    def get_context_data(self, **kwargs):
        """重写上下文函数."""
        context = super(JobInformationDetailView, self).get_context_data(**kwargs)
        name = context[self.context_object_name].name
        job_salary_benefits_relationship_objs = JobSalaryBenefitsRelationship.objects.filter(job_information=context[self.context_object_name])
        context['job_salary_benefits_relationship_objs'] = job_salary_benefits_relationship_objs
        job_information_functions_relationship_objs = JobInformationFunctionsRelationship.objects.filter(job_information=context[self.context_object_name])
        context['job_information_functions_relationship_objs'] = job_information_functions_relationship_objs
        job_information_objs = JobInformation.objects.filter(name__contains=name)
        context['job_information_objs'] = job_information_objs[:8]
        return context


class CompanyInformationDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """公司详情展示."""

    model = CompanyInformation
    page_title = '公司详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/company_information_detail.html"
    context_object_name = "company_information"

    def get_context_data(self, **kwargs):
        """重写上下文函数."""
        context = super(CompanyInformationDetailView, self).get_context_data(**kwargs)
        company_obj = context[self.context_object_name]
        job_information_objs = JobInformation.objects.filter(company_information=company_obj)
        context['job_information_objs'] = job_information_objs
        return context


class HuntJobCompanyScaleListView(LoginRequiredMixin, CommonMixin, ListView):
    """公司规模列表"""

    model = CompanyScale
    template_name = "company/huntjob_company_scale_list.html"
    page_title = "公司规模列表"
    paginate_by = '10'
    context_object_name = 'huntjob_company_scale_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_company_scale_objs = CompanyScale.objects
        if name:
            huntjob_company_scale_objs = huntjob_company_scale_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_company_scale_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobCompanyScaleListView, self).get_context_data(**kwargs)
        return context


class HuntJobCompanyScaleCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """公司规模创建."""

    template_name = 'company/huntjob_company_scale_create.html'
    page_title = '公司规模创建'
    form_class = CompanyScaleCreateForm
    success_url = reverse_lazy('huntjob:huntjob_company_scale_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobCompanyScaleCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            CompanyScale.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyScaleUpdateView(LoginRequiredMixin, CommonMixin, View):
    """公司规模更新."""

    template_name = 'company/huntjob_company_scale_update.html'
    page_title = '公司规模更新'
    success_url = reverse_lazy('huntjob:huntjob_company_scale_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_company_scale_obj = CompanyScale.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            CompanyScale.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyScaleDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """公司规模详情展示."""

    model = CompanyScale
    page_title = '公司规模详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "company/huntjob_company_scale_detail.html"
    context_object_name = "huntjob_company_scale_obj"


class HuntJobCompanyStyleListView(LoginRequiredMixin, CommonMixin, ListView):
    """性质列表"""

    model = CompanyStyle
    template_name = "company/huntjob_company_style_list.html"
    page_title = "性质列表"
    paginate_by = '10'
    context_object_name = 'huntjob_company_style_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_company_style_objs = CompanyStyle.objects
        if name:
            huntjob_company_style_objs = huntjob_company_style_objs.filter(Q(name__contains=name))
        return huntjob_company_style_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobCompanyStyleListView, self).get_context_data(**kwargs)
        return context


class HuntJobCompanyStyleCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """公司性质创建."""

    template_name = 'company/huntjob_company_style_create.html'
    page_title = '公司性质创建'
    form_class = CompanyStyleCreateForm
    success_url = reverse_lazy('huntjob:huntjob_company_style_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobCompanyStyleCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            description = request.POST.get('description', '')
            CompanyStyle.objects.create(name=name, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyStyleUpdateView(LoginRequiredMixin, CommonMixin, View):
    """公司性质更新."""

    template_name = 'company/huntjob_company_style_update.html'
    page_title = '公司性质更新'
    success_url = reverse_lazy('huntjob:huntjob_company_style_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_company_style_obj = CompanyStyle.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            description = request.POST.get('description', '')
            CompanyStyle.objects.filter(id=pid).update(name=name, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyStyleDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """公司性质详情展示."""

    model = CompanyStyle
    page_title = '公司性质详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "company/huntjob_company_style_detail.html"
    context_object_name = "huntjob_company_style_obj"
