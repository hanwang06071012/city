# coding: utf-8
"""
过滤器
"""
from django import template


register = template.Library()


# @register.filter
# def display_name(value, arg):
#     """展示名称."""
#     return apply(eval('value.get_' + arg + '_display'), ())

# 展示中国高校办学类型
@register.filter
def display_chinese_university_style(val):
    """展示中国高校办学类型."""
    style = '民办'
    if(val == 0):
        style = "民办"
    elif (val == 1):
        style = "公办"
    elif (val == 2):
        style = "合作办学"
    else:
        style = "待定"
    return style


# 判断高校类型
@register.simple_tag(takes_context=True)
def judge_chinese_university_style(context, src_dat, dest_dat):
    state = "false"
    if (src_dat == dest_dat):
        state = "true"
    return state
