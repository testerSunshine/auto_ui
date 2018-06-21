# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Report(models.Model):
    """
    测试报告详细记录
    """
    precondition = models.CharField("前置条件", max_length=255, default=None)
    case_name = models.CharField("case名称", max_length=128, default=None)
    check_step = models.CharField("检查步骤", max_length=128, default=None)
    title = models.CharField("用例标题", max_length=64, default=None)
    step = models.TextField("测试步骤", max_length=2048, default=None)
    phone_name = models.CharField("机型", max_length=64, default=None)
    result = models.ImageField("测试结果", default=0)
    screenshots_path = models.ImageField("测试图片", upload_to='upload', default=None)
    msg = models.TextField("失败原因", max_length=1024, default=None)
    case_id = models.CharField("case_id", max_length=64, default=None)
    report_uuid = models.CharField("每次运行唯一md5标识", max_length=256, default=None)
    report_create_time = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    report_update_time = models.DateTimeField("更新时间", auto_now=True, auto_now_add=False)
    platform_name = models.TextField("系统类型", max_length=16, default="android")
    case_step_time = models.TextField("测试步长，json格式", max_length=2048, default=None)
    # case_performance_info = models.TextField("每步运行的性能情况，内存、cpu、fps", max_length=2048, default=None)


class ReportInfo(models.Model):
    """
    测试报告统计
    """
    case_sum = models.IntegerField("case总和", default=0)
    case_pass_sum = models.IntegerField("通过case总和", default=0)
    case_fail_sum = models.IntegerField("失败case总和",  default=0)
    case_date = models.DateTimeField("测试日期", auto_now=False, auto_now_add=True)
    case_run_time = models.CharField("测试总耗时", max_length=64, default="0")
    platform_name = models.TextField("系统类型", max_length=16, default="android")
    report_uuid = models.CharField("每次运行唯一md5标识", max_length=256, default=None)
    report_info_create_time = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    report_info_update_time = models.DateTimeField("更新时间", auto_now=True, auto_now_add=False)

