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
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json
from public_resource.models import (
    ReginoanlManagement,
    ChineseUniversities,
)


class PublicResourceReginoanlManagementView(View):
    """公共资源接口函数API."""

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.ret = {'code': 0, 'message': '', 'data': []}
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        return super(PublicResourceReginoanlManagementView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """区划查询接口."""
        try:
            pk = self.kwargs.get('pk', None)
            province = request.GET.get('province', None)
            city = request.GET.get('city', None)
            county = request.GET.get('county', None)
            public_resource_reginoanl_objs = ReginoanlManagement.objects.all()
            if pk:
                pk = int(pk)
                public_resource_reginoanl_objs = public_resource_reginoanl_objs.filter(id=pk)
            if province:
                province = province.strip()
                public_resource_reginoanl_objs = public_resource_reginoanl_objs.filter(Q(province__icontains=province))
            if city:
                city = city.strip()
                public_resource_reginoanl_objs = public_resource_reginoanl_objs.filter(Q(city__icontains=city))
            if county:
                county = county.strip*()
                public_resource_reginoanl_objs = public_resource_reginoanl_objs.filter(Q(county__icontains=county))
            data = serializers.serialize('json', public_resource_reginoanl_objs)
            self.ret['data'] = json.loads(data)
        except Exception as e:
            self.ret['data'] = str(e)
        return JsonResponse(self.ret)

    def put(self, request, *args, **kwargs):
        """区划更新接口."""
        try:
            pk = self.kwargs.get('pk', None)
            request_put = json.loads(request.body)
            province = request_put.get('province', None)
            city = request_put.get('city', None)
            county = request_put.get('county', None)
            public_resource_reginoanl_objs = ReginoanlManagement.objects.all()
            if pk:
                pk = int(pk)
                public_resource_reginoanl_objs = public_resource_reginoanl_objs.filter(id=pk)
            if province:
                province = province.strip()
                for public_resource_reginoanl_obj in public_resource_reginoanl_objs:
                    public_resource_reginoanl_obj.province = province
                    public_resource_reginoanl_obj.save()
            if city:
                city = city.strip()
                for public_resource_reginoanl_obj in public_resource_reginoanl_objs:
                    public_resource_reginoanl_obj.city = city
                    public_resource_reginoanl_obj.save()
            if county:
                county = county.strip()
                for public_resource_reginoanl_obj in public_resource_reginoanl_objs:
                    public_resource_reginoanl_obj.county = county
                    public_resource_reginoanl_obj.save()
            data = serializers.serialize('json', public_resource_reginoanl_objs)
            self.ret['data'] = json.loads(data)
        except Exception as e:
            self.ret['data'] = str(e)
        return JsonResponse(self.ret)

    def post(self, request, *args, **kwargs):
        """区划创建接口."""
        try:
            request_post = json.loads(request_body)
            province = request_post.get('province', None)
            city = request_post.get('city', None)
            county = request_post.get('county', None)
            province = province.strip()
            city = city.strip()
            county = county.strip()
            ReginoanlManagement.objects.create(province=province, city=city, county=county)
            public_resource_reginoanl_objs = ReginoanlManagement.objects.filter(Q(province__icontains=province) & Q(city__icontains=city) & Q(county__icontains=county))
            data = serializers.serialize('json', public_resource_reginoanl_objs)
            self.ret['data'] = json.loads(data)
        except Exception as e:
            self.ret['data'] = str(e)
        return JsonResponse(self.ret)

    def delete(self, request, *args, **kwargs):
        """区划删除接口."""
        try:
            pk = self.kwargs.get('pk', None)
            request_delete = json.loads(request_body)
            public_resource_reginoanl_objs = ReginoanlManagement.objects.filter(id=pk)
            data = serializers.serialize('json', public_resource_reginoanl_objs)
            public_resource_reginoanl_objs.delete()
            self.ret['data'] = json.loads(data)
        except Exception as e:
            self.ret['data'] = str(e)
        return JsonResponse(self.ret)


class PublicResourceChineseUniversitiesView(View):
    """公共资源接口高校名录API."""

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.ret = {'code': 0, 'message': '', 'data': []}
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        return super(PublicResourceChineseUniversitiesView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """高校查询接口."""
        try:
            pk = self.kwargs.get('pk', None)
            name = request.GET.get('name', None)
            competent_authority = request.GET.get('competent_authority', None)
            location = request.GET.get('location', None)
            level = request.GET.get('level', None)
            style = request.GET.get('style', None)
            public_resource_chinese_universities_objs = ChineseUniversities.objects.all()
            if pk:
                pk = int(pk)
                public_resource_chinese_universities_objs = public_resource_chinese_universities_objs.filter(id=pk)
            if name:
                name = name.strip()
                public_resource_chinese_universities_objs = public_resource_chinese_universities_objs.filter(Q(name__icontains=name))
            if competent_authority:
                competent_authority = competent_authority.strip()
                public_resource_chinese_universities_objs = public_resource_chinese_universities_objs.filter(Q(competent_authority__icontains=competent_authority))
            if location:
                location = location.strip*()
                public_resource_chinese_universities_objs = public_resource_chinese_universities_objs.filter(Q(location__icontains=location))
            if level:
                level = level.strip*()
                public_resource_chinese_universities_objs = public_resource_chinese_universities_objs.filter(Q(level__icontains=level))
            if style:
                style = style.strip*()
                public_resource_chinese_universities_objs = public_resource_chinese_universities_objs.filter(Q(style__icontains=style))
            data = serializers.serialize('json', public_resource_chinese_universities_objs)
            self.ret['data'] = json.loads(data)
        except Exception as e:
            self.ret['data'] = str(e)
        return JsonResponse(self.ret)

    def put(self, request, *args, **kwargs):
        """中国高校更新接口."""
        try:
            pk = self.kwargs.get('pk', None)
            request_put = json.loads(request.body)
            name = request_put.get('name', None)
            competent_authority = request_put.get('competent_authority', None)
            location = request_put.get('location', None)
            level = request_put.get('level', None)
            style = request_put.get('style', None)
            public_resource_chinese_universities_objs = ChineseUniversities.objects.all()
            if pk:
                pk = int(pk)
                public_resource_chinese_universities_objs = public_resource_chinese_universities_objs.filter(id=pk)
            if name:
                name = name.strip()
                for public_resource_chinese_universities_obj in public_resource_chinese_universities_objs:
                    public_resource_chinese_universities_obj.name = name
                    public_resource_chinese_universities_obj.save()
            if competent_authority:
                competent_authority = competent_authority.strip()
                for public_resource_chinese_universities_obj in public_resource_chinese_universities_objs:
                    public_resource_chinese_universities_obj.competent_authority = competent_authority
                    public_resource_chinese_universities_obj.save()
            if location:
                location = location.strip()
                for public_resource_chinese_universities_obj in public_resource_chinese_universities_objs:
                    public_resource_chinese_universities_obj.location = location
                    public_resource_chinese_universities_obj.save()
            if level:
                level = level.strip()
                for public_resource_chinese_universities_obj in public_resource_chinese_universities_objs:
                    public_resource_chinese_universities_obj.level = level
                    public_resource_chinese_universities_obj.save()
            if style:
                style = style.strip()
                for public_resource_chinese_universities_obj in public_resource_chinese_universities_objs:
                    public_resource_chinese_universities_obj.style = style
                    public_resource_chinese_universities_obj.save()
            data = serializers.serialize('json', public_resource_chinese_universities_obj)
            self.ret['data'] = json.loads(data)
        except Exception as e:
            self.ret['data'] = str(e)
        return JsonResponse(self.ret)

    def post(self, request, *args, **kwargs):
        """区划创建接口."""
        try:
            request_post = json.loads(request_body)
            name = request_post.get('name', None)
            competent_authority = request_post.get('competent_authority', None)
            location = request_post.get('location', None)
            level = request_post.get('level', None)
            style = request_post.get('style', None)
            description = request_post.get('description', None)
            name = name.strip()
            competent_authority = competent_authority.strip()
            location = location.strip()
            level = level.strip()
            style = style.strip()
            ChineseUniversities.objects.create(name=name, competent_authority=competent_authority, location=location, level=level, style=style)
            public_resource_chinese_universities_objs = ChineseUniversities.objects.filter(Q(name__icontains=name) & Q(competent_authority__icontains=competent_authority) & Q(location__icontains=location) & Q(level__icontains=level) & Q(style__icontains=style))
            data = serializers.serialize('json', public_resource_chinese_universities_objs)
            self.ret['data'] = json.loads(data)
        except Exception as e:
            self.ret['data'] = str(e)
        return JsonResponse(self.ret)

    def delete(self, request, *args, **kwargs):
        """中国高校删除接口."""
        try:
            pk = self.kwargs.get('pk', None)
            public_resource_chinese_universities_objs = ChineseUniversities.objects.filter(id=pk)
            data = serializers.serialize('json', public_resource_chinese_universities_objs)
            public_resource_chinese_universities_objs.delete()
            self.ret['data'] = json.loads(data)
        except Exception as e:
            self.ret['data'] = str(e)
        return JsonResponse(self.ret)
