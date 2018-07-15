# -*- coding:utf-8 -*-
"""数据库用户与组模型."""

# =========================================================
# 作者：韩望
# 时间：2018-07-14
# 功能：数据库用户管理模块
# 版本: v 0.0.0.1_base
# 公司：天下同城
# 更新：无
# 备注：无
# =========================================================
# Create your models here.

from django.db import models
import django.utils.timezone as timezone


class CityAuthUser(models.Model):
    """用户管理模型."""

    password = models.CharField("用户密码", max_length=128, blank=False)
    username = models.CharField("市区", max_length=150, blank=False, unique=True)
    is_superuser = models.BooleanField("是否是超级管理员", default=False)
    first_name = models.CharField("姓", max_length=30, blank=False)
    last_name = models.CharField("名", max_length=30, blank=False)
    email = models.CharField("邮件", max_length=254, blank=False)
    is_staff = models.BooleanField("是否在职", default=True)
    is_active = models.BooleanField("使用还是禁用", default=False)
    last_login = models.DateTimeField("最后登录日期")
    date_joined = models.DateTimeField("入职日期", default=timezone.now)
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "用户管理"
        db_table = "city_auth_user"
        verbose_name_plural = verbose_name


class CityAuthGroup(models.Model):
    """组管理."""

    name = models.CharField("组名", max_length=80, blank=False, unique=True)
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "组管理"
        db_table = "city_auth_group"
        verbose_name_plural = verbose_name


class CityAuthRole(models.Model):
    """角色管理."""

    name = models.CharField("角色名", max_length=255)
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "角色管理"
        db_table = "city_auth_Role"
        verbose_name_plural = verbose_name


class CityAuthPermission(models.Model):
    """权限管理."""

    name = models.CharField("权限名", max_length=255)
    url = models.CharField("权限链接地址", max_length=2048)
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "角色管理"
        db_table = "city_auth_permission"
        verbose_name_plural = verbose_name


class CityAuthRolePermissionRelationship(models.Model):
    """角色与权限关系管理."""

    role = models.ForeignKey(CityAuthRole, related_name="role_permission")
    permission = models.ForeignKey(CityAuthPermission, related_name="permission_role")
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "角色与权限关系管理"
        db_table = "city_auth_role_permission_relationship"
        verbose_name_plural = verbose_name


class CityAuthUserGroupRelationship(models.Model):
    """用户与组关系管理."""

    use = models.ForeignKey(CityAuthUser, related_name="user_group")
    group = models.ForeignKey(CityAuthGroup, related_name="group_user")
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "用户与组关系管理"
        db_table = "city_auth_user_group_relationship"
        verbose_name_plural = verbose_name


class CityAuthUserRoleRelationship(models.Model):
    """用户与角色管理表."""

    use = models.ForeignKey(CityAuthUser, related_name="user_role")
    Role = models.ForeignKey(CityAuthRole, related_name="role_user")
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "用户与角色管理表"
        db_table = "city_auth_user_role_relationship"
        verbose_name_plural = verbose_name


class CityAuthGroupRoleRelationship(models.Model):
    """组角色管理表."""

    group = models.ForeignKey(CityAuthGroup, related_name="group_role")
    Role = models.ForeignKey(CityAuthRole, related_name="role_group")
    description = models.TextField("描述", default=None)
    create_time = models.DateTimeField("创建日期", default=timezone.now)
    update_time = models.DateTimeField("更新日期", auto_now=True)

    class Meta:
        app_label = 'huntjob'
        verbose_name = "组与角色管理表"
        db_table = "city_auth_group_role_relationship"
        verbose_name_plural = verbose_name
