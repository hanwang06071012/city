# -*- coding:utf-8 -*-
"""数据库管理通用视图."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：找工作通用视图
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.

from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from utils.common_lib import CommonMixin, LoginRequiredMixin
from huntjob.models import (
    CompanyScale,
    CompanyStyle,
    CompanyIndustry,
    CompanyInformation,
    ReleaseDate,
    MonthlySalaryRange,
    WorkingYears,
    AcademicRequirements,
    SalaryBenefits,
    JobType,
    JobFunctions,
    JobInformation,
    CompanyInformation,
)


class HuntJobOverView(LoginRequiredMixin, CommonMixin, View):
    """职业概况"""

    template_name = "default/huntjob_overview.html"

    def get(self, request, *args, **kwargs):
        """企业/职业概况"""
        # 企业概况
        company_scale_num = CompanyScale.objects.count()
        company_style_num = CompanyStyle.objects.count()
        company_industry_num = CompanyIndustry.objects.count()
        company_information_num = CompanyInformation.objects.count()
        # 职业概况
        release_date_num = ReleaseDate.objects.count()
        monthly_salary_range_num = MonthlySalaryRange.objects.count()
        working_years_num = WorkingYears.objects.count()
        academic_requirements_num = AcademicRequirements.objects.count()
        salary_benefits_num = SalaryBenefits.objects.count()
        job_type_num = JobType.objects.count()
        job_functions_num = JobFunctions.objects.count()
        job_information_num = JobInformation.objects.count()
        return render(request, self.template_name, locals())
