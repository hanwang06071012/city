# -*- coding:utf-8 -*-
"""数据库管理通用视图."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库职业公司视图
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView
from huntjob.models import (
    JobInformation,
    JobSalaryBenefitsRelationship,
    JobInformationFunctionsRelationship,
    CompanyScale,
    CompanyStyle,
    CompanyIndustry,
    CompanyInformation,
)
from utils.common_lib import (
    CommonMixin,
    LoginRequiredMixin,
    EasyAndDateTimeConversion,
)
from huntjob.forms import (
    CompanyScaleCreateForm,
    CompanyStyleCreateForm,
    CompanyIndustryCreateForm,
    CompanyInformationyCreateForm,
)
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
import logging

_log = logging.getLogger(__name__)


class HuntJobIndexListView(LoginRequiredMixin, CommonMixin, ListView):
    """岗位搜索展示默认页"""

    model = JobInformation
    template_name = "default/index.html"
    page_title = "职位列表"
    paginate_by = '10'
    context_object_name = 'job_infromations'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        job_infromations = JobInformation.objects
        if name:
            job_infromations = job_infromations.filter(Q(name__contains=name) | Q(work_place__contains=name) | Q(job_responsibilities__contains=name) | Q(job_requirements__contains=name))
        return job_infromations.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobIndexListView, self).get_context_data(**kwargs)
        return context


class JobInformationDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """岗位详情展示."""

    model = JobInformation
    page_title = '岗位详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "default/job_information_detail.html"
    context_object_name = "job_information"

    def get_context_data(self, **kwargs):
        """重写上下文函数."""
        context = super(JobInformationDetailView, self).get_context_data(**kwargs)
        name = context[self.context_object_name].name
        job_salary_benefits_relationship_objs = JobSalaryBenefitsRelationship.objects.filter(job_information=context[self.context_object_name])
        context['job_salary_benefits_relationship_objs'] = job_salary_benefits_relationship_objs
        job_information_functions_relationship_objs = JobInformationFunctionsRelationship.objects.filter(job_information=context[self.context_object_name])
        context['job_information_functions_relationship_objs'] = job_information_functions_relationship_objs
        job_information_objs = JobInformation.objects.filter(name__contains=name)
        context['job_information_objs'] = job_information_objs[:8]
        return context


class HuntJobCompanyScaleListView(LoginRequiredMixin, CommonMixin, ListView):
    """公司规模列表"""

    model = CompanyScale
    template_name = "company/huntjob_company_scale_list.html"
    page_title = "公司规模列表"
    paginate_by = '10'
    context_object_name = 'huntjob_company_scale_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_company_scale_objs = CompanyScale.objects
        if name:
            huntjob_company_scale_objs = huntjob_company_scale_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_company_scale_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobCompanyScaleListView, self).get_context_data(**kwargs)
        return context


class HuntJobCompanyScaleCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """公司规模创建."""

    template_name = 'company/huntjob_company_scale_create.html'
    page_title = '公司规模创建'
    form_class = CompanyScaleCreateForm
    success_url = reverse_lazy('huntjob:huntjob_company_scale_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobCompanyScaleCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            CompanyScale.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyScaleUpdateView(LoginRequiredMixin, CommonMixin, View):
    """公司规模更新."""

    template_name = 'company/huntjob_company_scale_update.html'
    page_title = '公司规模更新'
    success_url = reverse_lazy('huntjob:huntjob_company_scale_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_company_scale_obj = CompanyScale.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        print("==========post start===================")
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            # CompanyScale.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
            company_scale_obj = CompanyScale.objects.filter(id=pid).first()
            company_scale_obj.name = name
            company_scale_obj.value_max = value_max
            company_scale_obj.description = description
            company_scale_obj.save()
        except Exception as e:
            print(e)
            _log.info(e)
        print("===========post end=========================")
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyScaleDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """公司规模详情展示."""

    model = CompanyScale
    page_title = '公司规模详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "company/huntjob_company_scale_detail.html"
    context_object_name = "huntjob_company_scale_obj"


class HuntJobCompanyStyleListView(LoginRequiredMixin, CommonMixin, ListView):
    """性质列表"""

    model = CompanyStyle
    template_name = "company/huntjob_company_style_list.html"
    page_title = "性质列表"
    paginate_by = '10'
    context_object_name = 'huntjob_company_style_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_company_style_objs = CompanyStyle.objects
        if name:
            huntjob_company_style_objs = huntjob_company_style_objs.filter(Q(name__contains=name))
        return huntjob_company_style_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobCompanyStyleListView, self).get_context_data(**kwargs)
        return context


class HuntJobCompanyStyleCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """公司性质创建."""

    template_name = 'company/huntjob_company_style_create.html'
    page_title = '公司性质创建'
    form_class = CompanyStyleCreateForm
    success_url = reverse_lazy('huntjob:huntjob_company_style_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobCompanyStyleCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            description = request.POST.get('description', '')
            CompanyStyle.objects.create(name=name, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyStyleUpdateView(LoginRequiredMixin, CommonMixin, View):
    """公司性质更新."""

    template_name = 'company/huntjob_company_style_update.html'
    page_title = '公司性质更新'
    success_url = reverse_lazy('huntjob:huntjob_company_style_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_company_style_obj = CompanyStyle.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            description = request.POST.get('description', '')
            CompanyStyle.objects.filter(id=pid).update(name=name, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyStyleDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """公司性质详情展示."""

    model = CompanyStyle
    page_title = '公司性质详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "company/huntjob_company_style_detail.html"
    context_object_name = "huntjob_company_style_obj"


class HuntJobCompanyIndustryListView(LoginRequiredMixin, CommonMixin, ListView):
    """行业列表"""

    model = CompanyIndustry
    template_name = "company/huntjob_company_industry_list.html"
    page_title = "行业列表"
    paginate_by = '10'
    context_object_name = 'huntjob_company_industry_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_company_industry_objs = CompanyIndustry.objects
        if name:
            huntjob_company_industry_objs = huntjob_company_industry_objs.filter(Q(name__contains=name))
        return huntjob_company_industry_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobCompanyIndustryListView, self).get_context_data(**kwargs)
        return context


class HuntJobCompanyIndustryCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """行业创建."""

    template_name = 'company/huntjob_company_industry_create.html'
    page_title = '行业创建'
    form_class = CompanyIndustryCreateForm
    success_url = reverse_lazy('huntjob:huntjob_company_industry_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobCompanyIndustryCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        """重写,添加所有节点对象."""
        context = super(HuntJobCompanyIndustryCreateView, self).get_context_data(**kwargs)
        huntjob_company_industry_objs = CompanyIndustry.objects.all()
        context['huntjob_company_industry_objs'] = huntjob_company_industry_objs
        return context

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            parent_node = request.POST.get('parent_node')
            description = request.POST.get('description', '')
            CompanyIndustry.objects.create(name=name, parent_node=parent_node, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyIndustryUpdateView(LoginRequiredMixin, CommonMixin, View):
    """公司行业更新."""

    template_name = 'company/huntjob_company_industry_update.html'
    page_title = '公司行业更新'
    success_url = reverse_lazy('huntjob:huntjob_company_industry_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_company_industry_objs = CompanyIndustry.objects.all()
        huntjob_company_industry_obj = huntjob_company_industry_objs.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            parent_node = request.POST.get('parent_node')
            description = request.POST.get('description', '')
            CompanyIndustry.objects.filter(id=pid).update(name=name, parent_node=parent_node, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyIndustryDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """公司行业详情展示."""

    model = CompanyIndustry
    page_title = '公司行业详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "company/huntjob_company_industry_detail.html"
    context_object_name = "huntjob_company_industry_obj"

    def get_context_data(self, **kwargs):
        """重写,添加父节点."""
        try:
            pid = self.kwargs.get('id')
            context = super(HuntJobCompanyIndustryDetailView, self).get_context_data(**kwargs)
            huntjob_company_industry_obj = CompanyIndustry.objects.filter(id=pid).first()
            parent_node = huntjob_company_industry_obj.parent_node
            huntjob_company_industry_parent_obj = CompanyIndustry.objects.filter(id=parent_node).first()
            context['huntjob_company_industry_parent_obj'] = huntjob_company_industry_parent_obj
        except Exception as e:
            raise e
        return context


class HuntJobCompanyInformationListView(LoginRequiredMixin, CommonMixin, ListView):
    """公司列表"""

    model = CompanyInformation
    template_name = "company/huntjob_company_information_list.html"
    page_title = "公司列表"
    paginate_by = '30'
    context_object_name = 'huntjob_company_information_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_company_information_objs = CompanyInformation.objects
        if name:
            huntjob_company_information_objs = huntjob_company_information_objs.filter(Q(name__contains=name) | Q(scale__contains=name) | Q(address__contains=name))
        return huntjob_company_information_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobCompanyInformationListView, self).get_context_data(**kwargs)
        return context


class HuntJobCompanyInformationCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """公司创建."""

    template_name = 'company/huntjob_company_information_create.html'
    page_title = '公司创建'
    form_class = CompanyInformationyCreateForm
    success_url = reverse_lazy('huntjob:huntjob_company_information_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobCompanyInformationCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobCompanyInformationCreateView, self).get_context_data(**kwargs)
        context['scale_objs'] = CompanyScale.objects.all()
        context['style_objs'] = CompanyStyle.objects.all()
        context['industry_objs'] = CompanyIndustry.objects.filter(~Q(parent_node=0))
        return context

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            scale = request.POST.get('scale')
            scale = CompanyScale.objects.filter(id=scale).first()
            style = request.POST.get('style')
            style = CompanyStyle.objects.filter(id=style).first()
            industry = request.POST.get('industry')
            industry = CompanyIndustry.objects.filter(id=industry).first()
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            introduction = request.POST.get('introduction')
            description = request.POST.get('description')
            established = request.POST.get('established')
            established = EasyAndDateTimeConversion.easy_to_datetime(established)
            CompanyInformation.objects.create(name=name, scale=scale, style=style, industry=industry, address=address, contact=contact, introduction=introduction, description=description, established=established)
        except Exception as e:
            print(e)
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyInformationUpdateView(LoginRequiredMixin, CommonMixin, View):
    """公司信息更新."""

    template_name = 'company/huntjob_company_information_update.html'
    page_title = '公司信息更新'
    success_url = reverse_lazy('huntjob:huntjob_company_information_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_company_information_objs = CompanyInformation.objects.all()
        huntjob_company_information_obj = huntjob_company_information_objs.filter(id=pid).first()
        scale_objs = CompanyScale.objects.all()
        style_objs = CompanyStyle.objects.all()
        industry_objs = CompanyIndustry.objects.all()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            scale = request.POST.get('scale')
            scale = CompanyScale.objects.filter(id=scale).first()
            style = request.POST.get('style')
            style = CompanyStyle.objects.filter(id=style).first()
            industry = request.POST.get('industry')
            industry = CompanyIndustry.objects.filter(id=industry).first()
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            introduction = request.POST.get('introduction')
            description = request.POST.get('description')
            established = request.POST.get('established')
            established = EasyAndDateTimeConversion.easy_to_datetime(established)
            CompanyInformation.objects.filter(id=pid).update(name=name, scale=scale, style=style, industry=industry, address=address, contact=contact, introduction=introduction, description=description, established=established)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobCompanyInformationDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """公司详情展示."""

    model = CompanyInformation
    page_title = '公司详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "company/huntjob_company_information_detail.html"
    context_object_name = "huntjob_company_information_obj"
