# -*- coding:utf-8 -*-
"""数据库管理通用视图."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库职业公司视图
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
    CompanyScale,
    CompanyStyle,
    CompanyIndustry,
    CompanyInformation,
)
from utils.common_lib import (
    CommonMixin,
    LoginRequiredMixin,
    EasyAndDateTimeConversion,
)
from huntjob.forms import (
    CompanyScaleCreateForm,
    CompanyStyleCreateForm,
    CompanyIndustryCreateForm,
    CompanyInformationyCreateForm,
)
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
import logging

_log = logging.getLogger(__name__)


class HuntJobFrontIndexListView(LoginRequiredMixin, CommonMixin, ListView):
    """岗位搜索展示默认页"""

    model = JobInformation
    template_name = "front/huntjob_front_index.html"
    page_title = "职位列表"
    paginate_by = '30'
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
        context = super(HuntJobFrontIndexListView, self).get_context_data(**kwargs)
        return context
