# -*- coding:utf-8 -*-
"""数据库管理表单库.

# =========================================================
# 作者：韩望、秦海荣
# 时间：2018-04-05
# 功能：数据库管理表单库
# 版本: v 0.0.0.1
# 公司：中化能源互联科技组
# 更新：2018-06-26,重新架构forms表单系统，拆分文件模块化
# 备注：无
# =========================================================
"""
from __future__ import absolute_import, unicode_literals

from django import forms

from huntjob.models import (
    ReleaseDate,
    MonthlySalaryRange,
    WorkingYears,
    AcademicRequirements,
    SalaryBenefits,
    JobType,
    JobFunctions,
)


class ReleaseDateCreateForm(forms.ModelForm):
    """职位发布日期创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(ReleaseDateCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = ReleaseDate
        fields = ('name', 'value_max', 'description')


class MonthlySalaryRangeCreateForm(forms.ModelForm):
    """职位月薪创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(MonthlySalaryRangeCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = MonthlySalaryRange
        fields = ('name', 'value_max', 'description')


class WorkingYearsCreateForm(forms.ModelForm):
    """工作年限创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(WorkingYearsCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = WorkingYears
        fields = ('name', 'value_max', 'description')


class AcademicRequirementsCreateForm(forms.ModelForm):
    """学历要求创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(AcademicRequirementsCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = AcademicRequirements
        fields = ('name', 'value_max', 'description')


class SalaryBenefitsCreateForm(forms.ModelForm):
    """薪资福利创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(SalaryBenefitsCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = SalaryBenefits
        fields = ('name', 'value_max', 'description')


class JobTypeCreateForm(forms.ModelForm):
    """工作类型创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(JobTypeCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = JobType
        fields = ('name', 'value_max', 'description')


class JobFunctionsCreateForm(forms.ModelForm):
    """职业类别创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(JobFunctionsCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = JobFunctions
        fields = ('name', 'value_max', 'description')
