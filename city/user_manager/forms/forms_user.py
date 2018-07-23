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

from user_manager.models import CityAuthUser, CityAuthGroup, CityAuthPermission


class UserCreateForm(forms.ModelForm):
    """定义用户创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = CityAuthUser
        fields = ('username', 'password', 'is_superuser', 'first_name', 'last_name', 'email', 'phone', 'qq', 'is_staff', 'is_active', 'date_joined', 'description')


class GroupCreateForm(forms.ModelForm):
    """组创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(GroupCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = CityAuthGroup
        fields = ('name', 'is_active', 'description')


class RoleCreateForm(forms.ModelForm):
    """角色创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(RoleCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = CityAuthGroup
        fields = ('name', 'description')


class PermissionCreateForm(forms.ModelForm):
    """角色创建表单."""

    def __init__(self, request, *args, **kwargs):
        """初始化函数."""
        super(PermissionCreateForm, self).__init__(*args, **kwargs)
        self.request_ = request

    class Meta:
        """定义规则字段."""

        model = CityAuthPermission
        fields = ('name', 'url', 'parent_node','description')
