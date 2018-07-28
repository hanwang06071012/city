# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-25 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='学历要求')),
                ('value_max', models.IntegerField(default=0, verbose_name='最大数')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '学历要求',
                'verbose_name_plural': '学历要求',
                'db_table': 'academic_requirements',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CityAuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='组名')),
                ('is_active', models.BooleanField(default=False, verbose_name='使用还是禁用')),
                ('description', models.TextField(default=None, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '组管理',
                'verbose_name_plural': '组管理',
                'db_table': 'city_auth_group',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CityAuthGroupRoleRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '组与角色管理表',
                'verbose_name_plural': '组与角色管理表',
                'db_table': 'city_auth_group_role_relationship',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CityAuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='权限名')),
                ('url', models.CharField(max_length=2048, verbose_name='权限链接地址')),
                ('parent_node', models.IntegerField(default=0)),
                ('description', models.TextField(default=None, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '角色管理',
                'verbose_name_plural': '角色管理',
                'db_table': 'city_auth_permission',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CityAuthRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='角色名')),
                ('description', models.TextField(default=None, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '角色管理',
                'verbose_name_plural': '角色管理',
                'db_table': 'city_auth_Role',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CityAuthRolePermissionRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permission_role', to='huntjob.CityAuthPermission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_permission', to='huntjob.CityAuthRole')),
            ],
            options={
                'verbose_name': '角色与权限关系管理',
                'verbose_name_plural': '角色与权限关系管理',
                'db_table': 'city_auth_role_permission_relationship',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CityAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='用户密码')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='市区')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='是否是超级管理员')),
                ('first_name', models.CharField(max_length=30, verbose_name='姓')),
                ('last_name', models.CharField(max_length=30, verbose_name='名')),
                ('email', models.CharField(max_length=254, verbose_name='邮件')),
                ('phone', models.CharField(max_length=11, verbose_name='手机')),
                ('qq', models.CharField(max_length=13, verbose_name='QQ')),
                ('is_staff', models.BooleanField(default=True, verbose_name='是否在职')),
                ('is_active', models.BooleanField(default=False, verbose_name='使用还是禁用')),
                ('last_login', models.DateTimeField(verbose_name='最后登录日期')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='入职日期')),
                ('description', models.TextField(default=None, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'city_auth_user',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CityAuthUserGroupRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user', to='huntjob.CityAuthGroup')),
                ('use', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to='huntjob.CityAuthUser')),
            ],
            options={
                'verbose_name': '用户与组关系管理',
                'verbose_name_plural': '用户与组关系管理',
                'db_table': 'city_auth_user_group_relationship',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CityAuthUserRoleRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_user', to='huntjob.CityAuthRole')),
                ('use', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_role', to='huntjob.CityAuthUser')),
            ],
            options={
                'verbose_name': '用户与角色管理表',
                'verbose_name_plural': '用户与角色管理表',
                'db_table': 'city_auth_user_role_relationship',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CompanyIndustry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='行业名称')),
                ('parent_node', models.IntegerField(verbose_name='父节点')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '公司行业',
                'verbose_name_plural': '公司行业',
                'db_table': 'company_industry',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='公司名称')),
                ('address', models.CharField(max_length=256, verbose_name='公司地址')),
                ('contact', models.CharField(max_length=128, verbose_name='联系方式')),
                ('introduction', models.TextField(default=None, verbose_name='公司简介')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('established', models.DateTimeField(default=None, verbose_name='成立时间')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_industry', to='huntjob.CompanyIndustry')),
            ],
            options={
                'verbose_name': '公司信息',
                'verbose_name_plural': '公司信息',
                'db_table': 'company_information',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CompanyScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='规模名称')),
                ('value_max', models.CharField(max_length=64, verbose_name='最大数')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '公司规模',
                'verbose_name_plural': '公司规模',
                'db_table': 'company_scale',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CompanyStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='公司性质')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '公司性质',
                'verbose_name_plural': '公司性质',
                'db_table': 'company_style',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='JobFunctions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='职业类别名称')),
                ('value_max', models.IntegerField(default=0, verbose_name='最大数')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '职业类别',
                'verbose_name_plural': '职业类别',
                'db_table': 'job_functions',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='JobInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='职位名称')),
                ('recruitment_number', models.IntegerField(verbose_name='招聘人数')),
                ('work_place', models.CharField(max_length=64, verbose_name='工作地点')),
                ('job_responsibilities', models.TextField(default=None, verbose_name='岗位职责')),
                ('job_requirements', models.TextField(default=None, verbose_name='岗位要求')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('academic_requirements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_requirements_job', to='huntjob.AcademicRequirements')),
                ('company_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_information_job', to='huntjob.CompanyInformation')),
            ],
            options={
                'verbose_name': '职位信息',
                'verbose_name_plural': '职位信息',
                'db_table': 'job_information',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='JobInformationFunctionsRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('job_functions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_functions_information_relationship', to='huntjob.JobFunctions')),
                ('job_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_information_funtions_relationship', to='huntjob.JobInformation')),
            ],
            options={
                'verbose_name': '工作与类别关联模型',
                'verbose_name_plural': '工作与类别关联模型',
                'db_table': 'job_information_functions_relationship',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='JobSalaryBenefitsRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('job_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_information_relationship', to='huntjob.JobInformation')),
            ],
            options={
                'verbose_name': '工作与薪资福利关联模型',
                'verbose_name_plural': '工作与薪资福利关联模型',
                'db_table': 'job_salary_benefits_relationship',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='工作类型')),
                ('value_max', models.IntegerField(default=0, verbose_name='最大数')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '工作类型',
                'verbose_name_plural': '工作类型',
                'db_table': 'job_type',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='MonthlySalaryRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='月薪范围')),
                ('value_max', models.IntegerField(default=0, verbose_name='最大数')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '月薪范围',
                'verbose_name_plural': '月薪范围',
                'db_table': 'monthly_salary_range',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ReleaseDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='发布日期名称')),
                ('value_max', models.IntegerField(default=0, verbose_name='最大数')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '发布日期',
                'verbose_name_plural': '发布日期',
                'db_table': 'release_date',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='SalaryBenefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='薪资福利')),
                ('value_max', models.IntegerField(default=0, verbose_name='最大数')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '薪资福利',
                'verbose_name_plural': '薪资福利',
                'db_table': 'salary_benefits',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='WorkingYears',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='工作年限')),
                ('value_max', models.IntegerField(default=0, verbose_name='最大数')),
                ('description', models.TextField(default=None, verbose_name='备注')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '工作年限',
                'verbose_name_plural': '工作年限',
                'db_table': 'working_years',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='jobsalarybenefitsrelationship',
            name='salary_benefits',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_benefits_relationship', to='huntjob.SalaryBenefits'),
        ),
        migrations.AddField(
            model_name='jobinformation',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_type_job', to='huntjob.JobType'),
        ),
        migrations.AddField(
            model_name='jobinformation',
            name='monthly_salary_range',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Monthly_salary_range_job', to='huntjob.MonthlySalaryRange'),
        ),
        migrations.AddField(
            model_name='jobinformation',
            name='release_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='release_date_job', to='huntjob.ReleaseDate'),
        ),
        migrations.AddField(
            model_name='jobinformation',
            name='working_years',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_years_job', to='huntjob.WorkingYears'),
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_scale', to='huntjob.CompanyScale'),
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_style', to='huntjob.CompanyStyle'),
        ),
        migrations.AddField(
            model_name='cityauthgrouprolerelationship',
            name='Role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_group', to='huntjob.CityAuthRole'),
        ),
        migrations.AddField(
            model_name='cityauthgrouprolerelationship',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_role', to='huntjob.CityAuthGroup'),
        ),
    ]
