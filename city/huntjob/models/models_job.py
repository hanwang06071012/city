# -*- coding:utf-8 -*-
"""数据库管理模块模型."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库工作模块
# 版本: v 0.0.0.1_alpha
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.

from django.db import models
import django.utils.timezone as timezone
from .models_company import CompanyInformation


class ReleaseDate(models.Model):
    """职位发布日期模型."""

    name = models.CharField("发布日期名称", max_length=64, blank=False)
    value_max = models.CharField("最大数", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "月薪范围"
        db_table = "release_date"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class MonthlySalaryRange(models.Model):
    """职位月薪范围模型."""

    name = models.CharField("月薪范围", max_length=64, blank=False)
    value_max = models.CharField("最大数", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "月薪范围"
        db_table = "monthly_salary_range"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class WorkingYears(models.Model):
    """工作年限模型."""

    name = models.CharField("工作年限", max_length=64, blank=False)
    value_max = models.CharField("最大数", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "工作年限"
        db_table = "working_years"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class Academic_Requirements(models.Model):
    """学历要求模型."""

    name = models.CharField("学历要求", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "学历要求"
        db_table = "academic_requirements"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class SalaryBenefits(models.Model):
    """薪资福利模型."""

    name = models.CharField("薪资福利", max_length=64, blank=False)
    value_max = models.CharField("最大数", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "薪资福利"
        db_table = "salary_benefits"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class JobType(models.Model):
    """工作类型模型."""

    name = models.CharField("工作类型", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "工作类型"
        db_table = "job_type"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class JobFunctions(models.Model):
    """职业类别模型."""

    name = models.CharField("职业类别名称", max_length=64, blank=False)
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "职业类别"
        db_table = "job_functions"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class JobInformation(models.Model):
    """职位信息模型."""

    name = models.CharField("职位名称", max_length=64, blank=False)
    recruitment_number = models.IntegerField("招聘人数")
    company_information = models.ForeignKey(CompanyInformation, related_name='company_information_job')
    work_place = models.CharField("工作地点", max_length=64, blank=False)
    monthly_salary_range = models.ForeignKey(MonthlySalaryRange, related_name='Monthly_salary_range_job')
    release_date = models.ForeignKey(ReleaseDate, related_name='release_date_job')
    job_responsibilities = models.TextField("岗位职责", default=None)
    job_requirements = models.TextField("岗位要求", default=None)
    job_type = models.ForeignKey(JobType, related_name='job_type_job')
    working_years = models.ForeignKey(WorkingYears, related_name='working_years_job')
    academic_requirements = models.ForeignKey(Academic_Requirements, related_name='academic_requirements_job')
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "职位信息"
        db_table = "job_information"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class JobSalaryBenefitsRelationship(models.Model):
    """工作与薪资福利关联模型."""

    job_information = models.ForeignKey(JobInformation, related_name='job_information_relationship')
    salary_benefits = models.ForeignKey(SalaryBenefits, related_name='salary_benefits_relationship')
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "工作与薪资福利关联模型"
        db_table = "job_salary_benefits_relationship"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name


class JobInformationFunctionsRelationship(models.Model):
    """工作与类别关联模型."""

    job_information = models.ForeignKey(JobInformation, related_name='job_information_funtions_relationship')
    job_functions = models.ForeignKey(JobFunctions, related_name='job_functions_information_relationship')
    description = models.TextField("备注", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "工作与类别关联模型"
        db_table = "job_information_functions_relationship"
        ordering = ['-create_time']
        verbose_name_plural = verbose_name
