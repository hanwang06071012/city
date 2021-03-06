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
    CompanyScale,
    CompanyStyle,
    CompanyIndustry,
    CompanyInformation,
)


class CompanyScaleCreateForm(forms.ModelForm):
    """公司规模创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(CompanyScaleCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = CompanyScale
        fields = ('name', 'value_max', 'description')


class CompanyStyleCreateForm(forms.ModelForm):
    """公司性质创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(CompanyStyleCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = CompanyStyle
        fields = ('name', 'description')


class CompanyIndustryCreateForm(forms.ModelForm):
    """行业创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(CompanyIndustryCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = CompanyIndustry
        fields = ('name', 'parent_node', 'description')


class CompanyInformationyCreateForm(forms.ModelForm):
    """公司创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(CompanyInformationyCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = CompanyInformation
        fields = ('name', 'scale', 'industry', 'style', 'address', 'contact', 'introduction', 'description', 'established')
