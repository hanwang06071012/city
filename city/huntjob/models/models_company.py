# -*- coding:utf-8 -*-
"""数据库管理模块模型."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库公司模块
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.

from django.db import models
import django.utils.timezone as timezone


class CompanyScale(models.Model):
    """公司规模模型."""

    name = models.CharField("规模名称", max_length=64, blank=False)
    value_max = models.CharField("最大数", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "公司规模"
        db_table = "company_scale"
        verbose_name_plural = verbose_name


class CompanyStyle(models.Model):
    """公司性质模型."""

    name = models.CharField("公司性质", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "公司性质"
        db_table = "company_style"
        verbose_name_plural = verbose_name


class CompanyIndustry(models.Model):
    """公司行业模型."""

    name = models.CharField("行业名称", max_length=64, blank=False)
    parent_node = models.CharField("父节点", max_length=5, default=0)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "公司行业"
        db_table = "company_industry"
        verbose_name_plural = verbose_name


class CompanyInformation(models.Model):
    """公司信息模型."""

    name = models.CharField("公司名称", max_length=256, blank=False)
    scale = models.ForeignKey(CompanyScale, related_name='company_scale')
    industry = models.ForeignKey(CompanyIndustry, related_name='company_industry')
    style = models.ForeignKey(CompanyStyle, related_name='company_style')
    address = models.CharField("公司地址", max_length=256, blank=False)
    contact = models.CharField("联系方式", max_length=128, blank=False)
    introduction = models.TextField("公司简介", default=None)
    description = models.TextField("备注", default=None)
    established = models.DateTimeField("公司成立时间", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "公司信息"
        db_table = "company_information"
        verbose_name_plural = verbose_name
