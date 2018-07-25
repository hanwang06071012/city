# -*- coding:utf-8 -*-
"""数据库管理通用视图."""

# =========================================================
# 作者：韩望
# 时间：2018-07-22
# 功能：数据库公共视图函数
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.
from django.views.generic.base import View
from django.http import HttpResponse
import json
from user_manager.models import (
    CityAuthUser,
    CityAuthGroup,
    CityAuthRole,
    CityAuthPermission,
)
from public_resource.models import (
    ReginoanlManagement,
    ChineseUniversities,
)
from huntjob.models import (
    CompanyScale,
    CompanyStyle,
)


class CommonViewsUpdateView(View):
    """数据更新."""

    def post(self, request, *args, **kwargs):
        """重写接收处理函数."""
        ret = {'state': 0, 'msg': '', 'code': 0}
        id = self.kwargs.get('id')
        dat = json.loads(request.POST.get('dat'))
        # print("=========post end============================")
        # print(id)
        # print(dat)
        # print(type(dat))
        tablename = dat['tablename']
        types = dat['types']
        colname = json.loads(dat['colname'])
        if tablename == "user":
            if types == "update_staff":
                is_staff = (colname['is_staff'])
                CityAuthUser.objects.filter(id=id).update(is_staff=is_staff, is_active=1)
            elif types == "update_active":
                is_active = (colname['is_active'])
                CityAuthUser.objects.filter(id=id).update(is_active=is_active)
            else:
                pass
        elif tablename == "group":
            if types == "update_active_group":
                is_active = (colname['is_active'])
                CityAuthGroup.objects.filter(id=id).update(is_active=is_active)
        else:
            pass
        return HttpResponse(json.dumps(ret))


class CommonViewsDeleteView(View):
    """数据删除."""

    def post(self, request, *args, **kwargs):
        """重写接收处理函数."""
        ret = {'state': 0, 'msg': '', 'code': 0}
        id = self.kwargs.get('id')
        dat = json.loads(request.POST.get('dat'))
        # print(id)
        # print(dat)
        # print(type(dat))
        tablename = dat['tablename']
        types = dat['types']
        if (tablename == "user") and (types == "delete_user"):
            CityAuthUser.objects.filter(id=id).delete()
        elif (tablename == "group") and (types == "delete_group"):
            CityAuthGroup.objects.filter(id=id).delete()
        elif (tablename == "role") and (types == "delete_role"):
            CityAuthRole.objects.filter(id=id).delete()
        elif (tablename == "permission") and (types == "delete_permission"):
            CityAuthPermission.objects.filter(id=id).delete()
        elif (tablename == "reginoanlmanagment") and (types == "delete_reginoanl"):
            ReginoanlManagement.objects.filter(id=id).delete()
        elif (tablename == "chinese_universities") and (types == "delete_universities"):
            ChineseUniversities.objects.filter(id=id).delete()
        elif (tablename == "company_scale") and (types == "delete_company_scale"):
            CompanyScale.objects.filter(id=id).delete()
        elif (tablename == "company_style") and (types == "delete_company_style"):
            CompanyStyle.objects.filter(id=id).delete()
        else:
            pass
        return HttpResponse(json.dumps(ret))
