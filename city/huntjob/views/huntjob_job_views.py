# -*- coding:utf-8 -*-
"""数据库管理通用视图."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库职业工作视图
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.
from django.shortcuts import render
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
)
from django.db.models import Q

# Create your views here.
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView
from utils.common_lib import (
    CommonMixin,
    LoginRequiredMixin,
)
from huntjob.models import (
    ReleaseDate,
    MonthlySalaryRange,
    WorkingYears,
    AcademicRequirements,
    SalaryBenefits,
    JobType,
    JobFunctions,
)
from huntjob.forms import (
    ReleaseDateCreateForm,
    MonthlySalaryRangeCreateForm,
    WorkingYearsCreateForm,
    AcademicRequirementsCreateForm,
    SalaryBenefitsCreateForm,
    JobTypeCreateForm,
    JobFunctionsCreateForm,
)
from django.core.urlresolvers import reverse_lazy
import logging

_log = logging.getLogger(__name__)


class HuntJobReleaseDateListView(LoginRequiredMixin, CommonMixin, ListView):
    """发布日期列表"""

    model = ReleaseDate
    template_name = "job/huntjob_release_date_list.html"
    page_title = "发布日期列表"
    paginate_by = '30'
    context_object_name = 'huntjob_release_date_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_release_date_objs = ReleaseDate.objects
        if name:
            huntjob_release_date_objs = huntjob_release_date_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_release_date_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobReleaseDateListView, self).get_context_data(**kwargs)
        return context


class HuntJobReleaseDateCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """发布日期规模创建."""

    template_name = 'job/huntjob_release_date_create.html'
    page_title = '发布日期创建'
    form_class = ReleaseDateCreateForm
    success_url = reverse_lazy('huntjob:huntjob_release_date_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobReleaseDateCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            ReleaseDate.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobReleaseDateUpdateView(LoginRequiredMixin, CommonMixin, View):
    """发布日期更新."""

    template_name = 'job/huntjob_release_date_update.html'
    page_title = '发布日期更新'
    success_url = reverse_lazy('huntjob:huntjob_release_date_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_release_date_obj = ReleaseDate.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            ReleaseDate.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobReleaseDateDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """发布日期详情展示."""

    model = ReleaseDate
    page_title = '发布日期详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "job/huntjob_release_date_detail.html"
    context_object_name = "huntjob_release_date_obj"


class HuntJobMonthlySalaryRangeListView(LoginRequiredMixin, CommonMixin, ListView):
    """职位月薪列表"""

    model = MonthlySalaryRange
    template_name = "job/huntjob_monthly_salary_range_list.html"
    page_title = "职位月薪列表"
    paginate_by = '30'
    context_object_name = 'huntjob_monthly_salary_range_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_monthly_salary_range_objs = MonthlySalaryRange.objects
        if name:
            huntjob_monthly_salary_range_objs = huntjob_monthly_salary_range_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_monthly_salary_range_objs.all()

    def get_context_data(self, **kwargs):
        """重写."""
        context = super(HuntJobMonthlySalaryRangeListView, self).get_context_data(**kwargs)
        return context


class HuntJobMonthlySalaryRangeCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """职位月薪规模创建."""

    template_name = 'job/huntjob_monthly_salary_range_create.html'
    page_title = '职位月薪创建'
    form_class = MonthlySalaryRangeCreateForm
    success_url = reverse_lazy('huntjob:huntjob_monthly_salary_range_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobMonthlySalaryRangeCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            MonthlySalaryRange.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobMonthlySalaryRangeUpdateView(LoginRequiredMixin, CommonMixin, View):
    """职位月薪更新."""

    template_name = 'job/huntjob_monthly_salary_range_update.html'
    page_title = '职位月薪更新'
    success_url = reverse_lazy('huntjob:huntjob_monthly_salary_range_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_monthly_salary_range_obj = MonthlySalaryRange.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            MonthlySalaryRange.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobMonthlySalaryRangeDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """月薪范围详情展示."""

    model = MonthlySalaryRange
    page_title = '月薪范围详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "job/huntjob_monthly_salary_range_detail.html"
    context_object_name = "huntjob_monthly_salary_range_obj"


class HuntJobWorkingYearsListView(LoginRequiredMixin, CommonMixin, ListView):
    """工作年限列表"""

    model = WorkingYears
    template_name = "job/huntjob_working_years_list.html"
    page_title = "工作年限列表"
    paginate_by = '30'
    context_object_name = 'huntjob_working_years_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_working_years_objs = WorkingYears.objects
        if name:
            huntjob_working_years_objs = huntjob_working_years_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_working_years_objs.all()


class HuntJobWorkingYearsCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """工作年限创建."""

    template_name = 'job/huntjob_working_years_create.html'
    page_title = '工作年限创建'
    form_class = WorkingYearsCreateForm
    success_url = reverse_lazy('huntjob:huntjob_working_years_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobWorkingYearsCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            WorkingYears.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobWorkingYearsUpdateView(LoginRequiredMixin, CommonMixin, View):
    """工作年限更新."""

    template_name = 'job/huntjob_working_years_update.html'
    page_title = '工作年限更新'
    success_url = reverse_lazy('huntjob:huntjob_working_years_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_working_years_obj = WorkingYears.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            WorkingYears.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobWorkingYearsDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """工作年限详情展示."""

    model = MonthlySalaryRange
    page_title = '工作年限详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "job/huntjob_working_years_detail.html"
    context_object_name = "huntjob_working_years_obj"


class HuntJobAcademicRequirementsListView(LoginRequiredMixin, CommonMixin, ListView):
    """工作年限列表"""

    model = WorkingYears
    template_name = "job/huntjob_academic_requirements_list.html"
    page_title = "工作年限列表"
    paginate_by = '30'
    context_object_name = 'huntjob_academic_requirements_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_academic_requirements_objs = AcademicRequirements.objects
        if name:
            huntjob_academic_requirements_objs = huntjob_academic_requirements_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_academic_requirements_objs.all()


class HuntJobAcademicRequirementsCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """学历要求创建."""

    template_name = 'job/huntjob_academic_requirements_create.html'
    page_title = '工作年限创建'
    form_class = AcademicRequirementsCreateForm
    success_url = reverse_lazy('huntjob:huntjob_academic_requirements_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobAcademicRequirementsCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            AcademicRequirements.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)
