# -*- coding:utf-8 -*-
"""数据库管理通用视图."""

# =========================================================
# 作者：韩望
# 时间：2018-06-30
# 功能：数据库通用视图
# 版本: v 0.0.0.1_base
# 公司：中化能源互联科技组
# 更新：无
# 备注：无
# =========================================================
# Create your models here.


class CommonMixin(object):
    """增加公用文件头"""

    def get_context_data(self, **kwargs):
        context = super(CommonMixin, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title or ''
        return context


class EasyAndDateTimeConversion(object):
    """jquery easy时间格式与datetime时间格式字符转换"""

    @classmethod
    def easy_to_datetime(cls, expected_execution_time):
        """jquery easy时间字条转换成datatime,如：07/18/2018 15:38:34 -> 2018-07-18 15:38:34  """
        expected_execution_time_time_sed = expected_execution_time.split(" ")[1]
        expected_execution_time_date_sed = (expected_execution_time.split(" ")[0]).split("/")
        expected_execution_time_date = expected_execution_time_date_sed[2] + "-" + expected_execution_time_date_sed[0] + "-" + expected_execution_time_date_sed[1]
        expected_execution_time = expected_execution_time_date + " " + expected_execution_time_time_sed
        return expected_execution_time

    @classmethod
    def datatime_to_easy(cls, expected_execution_time):
        """datatime to jquery-easy:datatime -> 07/18/2018 15:38:34"""
        return expected_execution_time.strftime("%m/%d/%Y %H:%M:%S")
