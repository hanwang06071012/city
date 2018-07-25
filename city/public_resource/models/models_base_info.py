# -*- coding:utf-8 -*-
"""数据库管理模块模型."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库基础信息模块
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.

from django.db import models
import django.utils.timezone as timezone


class ReginoanlManagement(models.Model):
    """中国区划管理模型."""

    province = models.CharField("省", max_length=128, blank=False)
    city = models.CharField("市区", max_length=128, blank=False)
    county = models.CharField("区县", max_length=128, blank=False)
    people = models.CharField("人口数量", max_length=128, blank=False)
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        """类型."""

        app_label = 'public_resource'
        verbose_name = "中国区划管理"
        db_table = "reginoanl_management"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class ChineseUniversities(models.Model):
    """中国全国高校模型."""

    name = models.CharField("高校名称", max_length=128, blank=False)
    competent_authority = models.CharField("管辖部门", max_length=128, blank=False)
    location = models.CharField("所在地", max_length=128, blank=False)
    level = models.IntegerField("办学层次")  # 0：专科，1：本科
    style = models.IntegerField("办学类型")  # 0：民办，1：公办，2：合作办学
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        """类型."""

        app_label = 'public_resource'
        verbose_name = "中国全国高校"
        db_table = "chinese_universities"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name
