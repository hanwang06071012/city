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

from public_resource.models import ReginoanlManagement, ChineseUniversities


class ReginoanlCreateForm(forms.ModelForm):
    """行政区划创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(ReginoanlCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = ReginoanlManagement
        fields = ('province', 'city', 'county', 'description')


class ChineseUniversitiesCreateForm(forms.ModelForm):
    """行政区划创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(ChineseUniversitiesCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = ChineseUniversities
        fields = ('name', 'competent_authority', 'location', 'level', 'style', 'description')
