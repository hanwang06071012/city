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
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from public_resource.models import (
    ReginoanlManagement,
)


class PublicResourceReginoanlManagementView(View):
    """公共资源接口函数API."""

    ret = {'code': 0, 'message': '', 'data': []}

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        return super(PublicResourceReginoanlManagementView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """区划查询接口."""
        public_resource_reginoanl_objs = ReginoanlManagement.objects.all()
        data = serializers.serialize('json', public_resource_reginoanl_objs)
        self.ret['data'] = json.loads(data)
        return JsonResponse(self.ret)

    def post(self, request, *args, **kwargs):
        """区划创建接口."""
        return JsonResponse(self.ret)

    def put(self, request, *args, **kwargs):
        """区划更新接口."""
        return JsonResponse(self.ret)

    def delete(self, request, *args, **kwargs):
        """区划删除接口."""
        return JsonResponse(self.ret)
