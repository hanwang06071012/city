# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-27 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('huntjob', '0003_auto_20180723_1434'),
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
        migrations.DeleteModel(
            name='ChineseUniversities',
        ),
        migrations.DeleteModel(
            name='ReginoanlManagement',
        ),
        migrations.AlterModelOptions(
            name='cityauthgroup',
            options={'ordering': ['-create_time'], 'verbose_name': '组管理', 'verbose_name_plural': '组管理'},
        ),
        migrations.AlterModelOptions(
            name='cityauthgrouprolerelationship',
            options={'ordering': ['-create_time'], 'verbose_name': '组与角色管理表', 'verbose_name_plural': '组与角色管理表'},
        ),
        migrations.AlterModelOptions(
            name='cityauthpermission',
            options={'ordering': ['-create_time'], 'verbose_name': '角色管理', 'verbose_name_plural': '角色管理'},
        ),
        migrations.AlterModelOptions(
            name='cityauthrole',
            options={'ordering': ['-create_time'], 'verbose_name': '角色管理', 'verbose_name_plural': '角色管理'},
        ),
        migrations.AlterModelOptions(
            name='cityauthrolepermissionrelationship',
            options={'ordering': ['-create_time'], 'verbose_name': '角色与权限关系管理', 'verbose_name_plural': '角色与权限关系管理'},
        ),
        migrations.AlterModelOptions(
            name='cityauthuser',
            options={'ordering': ['-create_time'], 'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
        migrations.AlterModelOptions(
            name='cityauthusergrouprelationship',
            options={'ordering': ['-create_time'], 'verbose_name': '用户与组关系管理', 'verbose_name_plural': '用户与组关系管理'},
        ),
        migrations.AlterModelOptions(
            name='cityauthuserrolerelationship',
            options={'ordering': ['-create_time'], 'verbose_name': '用户与角色管理表', 'verbose_name_plural': '用户与角色管理表'},
        ),
        migrations.AlterModelOptions(
            name='companyindustry',
            options={'ordering': ['-create_time'], 'verbose_name': '公司行业', 'verbose_name_plural': '公司行业'},
        ),
        migrations.AlterModelOptions(
            name='companyinformation',
            options={'ordering': ['-create_time'], 'verbose_name': '公司信息', 'verbose_name_plural': '公司信息'},
        ),
        migrations.AlterModelOptions(
            name='companyscale',
            options={'ordering': ['-create_time'], 'verbose_name': '公司规模', 'verbose_name_plural': '公司规模'},
        ),
        migrations.AlterModelOptions(
            name='companystyle',
            options={'ordering': ['-create_time'], 'verbose_name': '公司性质', 'verbose_name_plural': '公司性质'},
        ),
        migrations.AlterModelOptions(
            name='jobfunctions',
            options={'ordering': ['-create_time'], 'verbose_name': '职业类别', 'verbose_name_plural': '职业类别'},
        ),
        migrations.AlterModelOptions(
            name='jobinformation',
            options={'ordering': ['-create_time'], 'verbose_name': '职位信息', 'verbose_name_plural': '职位信息'},
        ),
        migrations.AlterModelOptions(
            name='jobinformationfunctionsrelationship',
            options={'ordering': ['-create_time'], 'verbose_name': '工作与类别关联模型', 'verbose_name_plural': '工作与类别关联模型'},
        ),
        migrations.AlterModelOptions(
            name='jobsalarybenefitsrelationship',
            options={'ordering': ['-create_time'], 'verbose_name': '工作与薪资福利关联模型', 'verbose_name_plural': '工作与薪资福利关联模型'},
        ),
        migrations.AlterModelOptions(
            name='jobtype',
            options={'ordering': ['-create_time'], 'verbose_name': '工作类型', 'verbose_name_plural': '工作类型'},
        ),
        migrations.AlterModelOptions(
            name='monthlysalaryrange',
            options={'ordering': ['-create_time'], 'verbose_name': '月薪范围', 'verbose_name_plural': '月薪范围'},
        ),
        migrations.AlterModelOptions(
            name='releasedate',
            options={'ordering': ['-create_time'], 'verbose_name': '发布日期', 'verbose_name_plural': '发布日期'},
        ),
        migrations.AlterModelOptions(
            name='salarybenefits',
            options={'ordering': ['-create_time'], 'verbose_name': '薪资福利', 'verbose_name_plural': '薪资福利'},
        ),
        migrations.AlterModelOptions(
            name='workingyears',
            options={'ordering': ['-create_time'], 'verbose_name': '工作年限', 'verbose_name_plural': '工作年限'},
        ),
        migrations.AddField(
            model_name='jobfunctions',
            name='value_max',
            field=models.IntegerField(default=0, verbose_name='最大数'),
        ),
        migrations.AddField(
            model_name='jobtype',
            name='value_max',
            field=models.IntegerField(default=0, verbose_name='最大数'),
        ),
        migrations.AlterField(
            model_name='companyindustry',
            name='parent_node',
            field=models.IntegerField(verbose_name='父节点'),
        ),
        migrations.AlterField(
            model_name='companyinformation',
            name='established',
            field=models.DateTimeField(default=None, verbose_name='成立时间'),
        ),
        migrations.AlterField(
            model_name='jobinformation',
            name='academic_requirements',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_requirements_job', to='huntjob.AcademicRequirements'),
        ),
        migrations.AlterField(
            model_name='monthlysalaryrange',
            name='value_max',
            field=models.IntegerField(default=0, verbose_name='最大数'),
        ),
        migrations.AlterField(
            model_name='releasedate',
            name='value_max',
            field=models.IntegerField(default=0, verbose_name='最大数'),
        ),
        migrations.AlterField(
            model_name='salarybenefits',
            name='value_max',
            field=models.IntegerField(default=0, verbose_name='最大数'),
        ),
        migrations.AlterField(
            model_name='workingyears',
            name='value_max',
            field=models.IntegerField(default=0, verbose_name='最大数'),
        ),
        migrations.DeleteModel(
            name='Academic_Requirements',
        ),
    ]