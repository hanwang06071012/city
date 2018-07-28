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

    model = WorkingYears
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


class HuntJobAcademicRequirementsUpdateView(LoginRequiredMixin, CommonMixin, View):
    """学历要求更新."""

    template_name = 'job/huntjob_academic_requirements_update.html'
    page_title = '学历更新'
    success_url = reverse_lazy('huntjob:huntjob_academic_requirements_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_academic_requirements_obj = AcademicRequirements.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            AcademicRequirements.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobAcademicRequirementsDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """学历详情展示."""

    model = AcademicRequirements
    page_title = '学历要求详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "job/huntjob_academic_requirements_detail.html"
    context_object_name = "huntjob_academic_requirements_obj"


class HuntJobSalaryBenefitsListView(LoginRequiredMixin, CommonMixin, ListView):
    """薪资福利列表"""

    model = SalaryBenefits
    template_name = "job/huntjob_salary_benefits_list.html"
    page_title = "薪资福利列表"
    paginate_by = '30'
    context_object_name = 'huntjob_salary_benefits_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_salary_benefits_objs = SalaryBenefits.objects
        if name:
            huntjob_salary_benefits_objs = huntjob_salary_benefits_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_salary_benefits_objs.all()


class HuntJobSalaryBenefitsCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """薪资福利创建."""

    template_name = 'job/huntjob_salary_benefits_create.html'
    page_title = '薪资福利创建'
    form_class = SalaryBenefitsCreateForm
    success_url = reverse_lazy('huntjob:huntjob_salary_benefits_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobSalaryBenefitsCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            SalaryBenefits.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobSalaryBenefitsUpdateView(LoginRequiredMixin, CommonMixin, View):
    """薪资福利更新."""

    template_name = 'job/huntjob_salary_benefits_update.html'
    page_title = '薪资福利更新'
    success_url = reverse_lazy('huntjob:huntjob_salary_benefits_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_salary_benefits_obj = SalaryBenefits.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            SalaryBenefits.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobSalaryBenefitsDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """薪资福利详情展示."""

    model = SalaryBenefits
    page_title = '薪资福利详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "job/huntjob_salary_benefits_detail.html"
    context_object_name = "huntjob_salary_benefits_obj"


class HuntJobJobTypeListView(LoginRequiredMixin, CommonMixin, ListView):
    """工作类型列表"""

    model = JobType
    template_name = "job/huntjob_job_type_list.html"
    page_title = "工作类型列表"
    paginate_by = '30'
    context_object_name = 'huntjob_job_type_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_job_type_objs = JobType.objects
        if name:
            huntjob_job_type_objs = huntjob_job_type_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_job_type_objs.all()


class HuntJobJobTypeCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """工作类型创建."""

    template_name = 'job/huntjob_job_type_create.html'
    page_title = '工作类型创建'
    form_class = JobTypeCreateForm
    success_url = reverse_lazy('huntjob:huntjob_job_type_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobJobTypeCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            JobType.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobJobTypeUpdateView(LoginRequiredMixin, CommonMixin, View):
    """工作类型更新."""

    template_name = 'job/huntjob_job_type_update.html'
    page_title = '工作类型更新'
    success_url = reverse_lazy('huntjob:huntjob_job_type_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_job_type_obj = JobType.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            JobType.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobJobTypeDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """工作类型详情展示."""

    model = JobType
    page_title = '工作类型详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "job/huntjob_job_type_detail.html"
    context_object_name = "huntjob_job_type_obj"


class HuntJobJobFunctionsListView(LoginRequiredMixin, CommonMixin, ListView):
    """职业类别列表"""

    model = JobFunctions
    template_name = "job/huntjob_job_functions_list.html"
    page_title = "职业类别列表"
    paginate_by = '30'
    context_object_name = 'huntjob_job_functions_objs'

    def get_queryset(self):
        """重写."""
        name = self.request.GET.get('name')

        huntjob_job_functions_objs = JobFunctions.objects
        if name:
            huntjob_job_functions_objs = huntjob_job_functions_objs.filter(Q(name__contains=name) | Q(value_max__contains=name))
        return huntjob_job_functions_objs.all()


class HuntJobJobFunctionsCreateView(LoginRequiredMixin, CommonMixin, CreateView):
    """职业类别创建."""

    template_name = 'job/huntjob_job_functions_create.html'
    page_title = '职业类别创建'
    form_class = JobFunctionsCreateForm
    success_url = reverse_lazy('huntjob:huntjob_job_functions_list')

    def get_form_kwargs(self):
        """重写."""
        kwargs = super(HuntJobJobFunctionsCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            JobFunctions.objects.create(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobJobFunctionsUpdateView(LoginRequiredMixin, CommonMixin, View):
    """职业类别更新."""

    template_name = 'job/huntjob_job_functions_update.html'
    page_title = '职业类别更新'
    success_url = reverse_lazy('huntjob:huntjob_job_functions_list')

    def get(self, request, *args, **kwargs):
        pid = self.kwargs.get('id')
        huntjob_job_functions_obj = JobFunctions.objects.filter(id=pid).first()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        try:
            pid = self.kwargs.get('id')
            name = request.POST.get('name')
            value_max = request.POST.get('value_max')
            description = request.POST.get('description', '')
            JobFunctions.objects.filter(id=pid).update(name=name, value_max=value_max, description=description)
        except Exception as e:
            _log.info(e)
        return HttpResponseRedirect(self.success_url)


class HuntJobJobFunctionsDetailView(LoginRequiredMixin, CommonMixin, DetailView):
    """职业类别详情展示."""

    model = JobFunctions
    page_title = '职业类别详情'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "job/huntjob_job_functions_detail.html"
    context_object_name = "huntjob_job_functions_obj"
