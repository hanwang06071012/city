"""city URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from huntjob.views import HuntJobTestView
from huntjob.views import (
    HuntJobIndexListView,
    JobInformationDetailView,
    HuntJobCompanyScaleListView,
    HuntJobCompanyScaleCreateView,
    HuntJobCompanyScaleUpdateView,
    HuntJobCompanyScaleDetailView,
    HuntJobCompanyStyleListView,
    HuntJobCompanyStyleCreateView,
    HuntJobCompanyStyleUpdateView,
    HuntJobCompanyStyleDetailView,
    HuntJobCompanyIndustryListView,
    HuntJobCompanyIndustryCreateView,
    HuntJobCompanyIndustryUpdateView,
    HuntJobCompanyIndustryDetailView,
    HuntJobCompanyInformationListView,
    HuntJobCompanyInformationCreateView,
    HuntJobCompanyInformationUpdateView,
    HuntJobCompanyInformationDetailView,
    HuntJobReleaseDateListView,
    HuntJobReleaseDateCreateView,
    HuntJobReleaseDateUpdateView,
    HuntJobReleaseDateDetailView,
    HuntJobMonthlySalaryRangeListView,
    HuntJobMonthlySalaryRangeCreateView,
    HuntJobMonthlySalaryRangeUpdateView,
    HuntJobMonthlySalaryRangeDetailView,
    HuntJobWorkingYearsListView,
    HuntJobWorkingYearsCreateView,
    HuntJobWorkingYearsUpdateView,
    HuntJobWorkingYearsDetailView,
    HuntJobAcademicRequirementsListView,
    HuntJobAcademicRequirementsCreateView,
    HuntJobAcademicRequirementsUpdateView,
    HuntJobAcademicRequirementsDetailView,
    HuntJobSalaryBenefitsListView,
    HuntJobSalaryBenefitsCreateView,
    HuntJobSalaryBenefitsUpdateView,
    HuntJobSalaryBenefitsDetailView,
    HuntJobJobTypeListView,
    HuntJobJobTypeCreateView,
    HuntJobJobTypeUpdateView,
    HuntJobJobTypeDetailView,
    HuntJobJobFunctionsListView,
    HuntJobJobFunctionsCreateView,
    HuntJobJobFunctionsUpdateView,
    HuntJobJobFunctionsDetailView,
)

urlpatterns = [
    url(r'^testview/', HuntJobTestView.as_view(), name='testview'),
    url(r'^index/', HuntJobIndexListView.as_view(), name='index'),
    url(r'^job/information/(?P<id>[0-9]+)/detail/', JobInformationDetailView.as_view(), name='job_information_detail'),
    url(r'^company/scale/list/', HuntJobCompanyScaleListView.as_view(), name='huntjob_company_scale_list'),
    url(r'^company/scale/create/', HuntJobCompanyScaleCreateView.as_view(), name='huntjob_company_scale_create'),
    url(r'^company/scale/(?P<id>[0-9]+)/update/', HuntJobCompanyScaleUpdateView.as_view(), name='huntjob_company_scale_update'),
    url(r'^company/scale/(?P<id>[0-9]+)/detail/', HuntJobCompanyScaleDetailView.as_view(), name='huntjob_company_scale_detail'),
    url(r'^company/style/list/', HuntJobCompanyStyleListView.as_view(), name='huntjob_company_style_list'),
    url(r'^company/style/create/', HuntJobCompanyStyleCreateView.as_view(), name='huntjob_company_style_create'),
    url(r'^company/style/(?P<id>[0-9]+)/update/', HuntJobCompanyStyleUpdateView.as_view(), name='huntjob_company_style_update'),
    url(r'^company/style/(?P<id>[0-9]+)/detail/', HuntJobCompanyStyleDetailView.as_view(), name='huntjob_company_style_detail'),
    url(r'^company/industry/list/', HuntJobCompanyIndustryListView.as_view(), name='huntjob_company_industry_list'),
    url(r'^company/industry/create/', HuntJobCompanyIndustryCreateView.as_view(), name='huntjob_company_industry_create'),
    url(r'^company/industry/(?P<id>[0-9]+)/update/', HuntJobCompanyIndustryUpdateView.as_view(), name='huntjob_company_industry_update'),
    url(r'^company/industry/(?P<id>[0-9]+)/detail/', HuntJobCompanyIndustryDetailView.as_view(), name='huntjob_company_industry_detail'),
    url(r'^company/information/list/', HuntJobCompanyInformationListView.as_view(), name='huntjob_company_information_list'),
    url(r'^company/information/create/', HuntJobCompanyInformationCreateView.as_view(), name='huntjob_company_information_create'),
    url(r'^company/information/(?P<id>[0-9]+)/update/', HuntJobCompanyInformationUpdateView.as_view(), name='huntjob_company_information_update'),
    url(r'^company/information/(?P<id>[0-9]+)/detail/', HuntJobCompanyInformationDetailView.as_view(), name='huntjob_company_information_detail'),
    url(r'^release/date/list/', HuntJobReleaseDateListView.as_view(), name='huntjob_release_date_list'),
    url(r'^release/date/create/', HuntJobReleaseDateCreateView.as_view(), name='huntjob_release_date_create'),
    url(r'^release/date/(?P<id>[0-9]+)/update/', HuntJobReleaseDateUpdateView.as_view(), name='huntjob_release_date_update'),
    url(r'^release/date/(?P<id>[0-9]+)/detail/', HuntJobReleaseDateDetailView.as_view(), name='huntjob_release_date_detail'),
    url(r'^monthly/salary/range/list/', HuntJobMonthlySalaryRangeListView.as_view(), name='huntjob_monthly_salary_range_list'),
    url(r'^monthly/salary/range/create/', HuntJobMonthlySalaryRangeCreateView.as_view(), name='huntjob_monthly_salary_range_create'),
    url(r'^monthly/salary/range/(?P<id>[0-9]+)/update/', HuntJobMonthlySalaryRangeUpdateView.as_view(), name='huntjob_monthly_salary_range_update'),
    url(r'^monthly/salary/range/(?P<id>[0-9]+)/detail/', HuntJobMonthlySalaryRangeDetailView.as_view(), name='huntjob_monthly_salary_range_detail'),
    url(r'^working/years/list/', HuntJobWorkingYearsListView.as_view(), name='huntjob_working_years_list'),
    url(r'^working/years/create/', HuntJobWorkingYearsCreateView.as_view(), name='huntjob_working_years_create'),
    url(r'^working/years/(?P<id>[0-9]+)/update/', HuntJobWorkingYearsUpdateView.as_view(), name='huntjob_working_years_update'),
    url(r'^working/years/(?P<id>[0-9]+)/detail/', HuntJobWorkingYearsDetailView.as_view(), name='huntjob_working_years_detail'),
    url(r'^academic/requirements/list/', HuntJobAcademicRequirementsListView.as_view(), name='huntjob_academic_requirements_list'),
    url(r'^academic/requirements/create/', HuntJobAcademicRequirementsCreateView.as_view(), name='huntjob_academic_requirements_create'),
    url(r'^academic/requirements/(?P<id>[0-9]+)/update/', HuntJobAcademicRequirementsUpdateView.as_view(), name='huntjob_academic_requirements_update'),
    url(r'^academic/requirements/(?P<id>[0-9]+)/detail/', HuntJobAcademicRequirementsDetailView.as_view(), name='huntjob_academic_requirements_detail'),
    url(r'^salary/benefits/list/', HuntJobSalaryBenefitsListView.as_view(), name='huntjob_salary_benefits_list'),
    url(r'^salary/benefits/create/', HuntJobSalaryBenefitsCreateView.as_view(), name='huntjob_salary_benefits_create'),
    url(r'^salary/benefits/(?P<id>[0-9]+)/update/', HuntJobSalaryBenefitsUpdateView.as_view(), name='huntjob_salary_benefits_update'),
    url(r'^salary/benefits/(?P<id>[0-9]+)/detail/', HuntJobSalaryBenefitsDetailView.as_view(), name='huntjob_salary_benefits_detail'),
    url(r'^job/type/list/', HuntJobJobTypeListView.as_view(), name='huntjob_job_type_list'),
    url(r'^job/type/create/', HuntJobJobTypeCreateView.as_view(), name='huntjob_job_type_create'),
    url(r'^job/type/(?P<id>[0-9]+)/update/', HuntJobJobTypeUpdateView.as_view(), name='huntjob_job_type_update'),
    url(r'^job/type/(?P<id>[0-9]+)/detail/', HuntJobJobTypeDetailView.as_view(), name='huntjob_job_type_detail'),
    url(r'^job/functions/list/', HuntJobJobFunctionsListView.as_view(), name='huntjob_job_functions_list'),
    url(r'^job/functions/create/', HuntJobJobFunctionsCreateView.as_view(), name='huntjob_job_functions_create'),
    url(r'^job/functions/(?P<id>[0-9]+)/update/', HuntJobJobFunctionsUpdateView.as_view(), name='huntjob_job_functions_update'),
    url(r'^job/functions/(?P<id>[0-9]+)/detail/', HuntJobJobFunctionsDetailView.as_view(), name='huntjob_job_functions_detail'),

]
