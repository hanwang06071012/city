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
from huntjob.models import (
    JobInformation,
    JobSalaryBenefitsRelationship,
    JobInformationFunctionsRelationship,
    CompanyInformation,
    )
from django.db.models import Q
from utils.common_lib import CommonMixin


class HuntJobIndexListView(CommonMixin, ListView):
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


class JobInformationDetailView(CommonMixin, DetailView):
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


class CompanyInformationDetailView(CommonMixin, DetailView):
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
