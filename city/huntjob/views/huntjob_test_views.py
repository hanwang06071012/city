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

# Create your views here.
from django.views.generic import View


class HuntJobTestView(View):
    """测试"""

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        """测试代码"""
        return render(request, self.template_name, locals())
