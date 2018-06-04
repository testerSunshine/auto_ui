
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
import json

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from report.models import ReportInfo, Report
from report.serializers import ReportInfoSerializer


def reportDetail(request):
    """测试报告详情列表"""
    return render(request, "app/report.html", {"report": ReportInfo.objects.order_by("-id")})


def reportCaseInfo(request):
    """
    每个用例详细测试报告信息，包含截图，每步用例步骤耗时
    :param request:
    :return:
    """
    uuid = request.GET.get("id", None)
    case_name = request.GET.get("case_name", None)
    caseInfo = Report.objects.filter(report_uuid=uuid,
                                     case_name=case_name)
    for c in caseInfo:
        if c.case_step_time:
            caseTime = json.loads(c.case_step_time)
        else:
            caseTime = {"step": 0}
        return render(request, "app/reportCaseInfo.html", {"reportCaseInfo": caseInfo[0],
                                                           "caseTimeAll": sum(caseTime.values()),
                                                           "caseTimeK": json.dumps(caseTime.keys()),
                                                           "caseTimeV": caseTime.values()})


def reportCount(request):
    """
    详细测试报告统计
    :param request:
    :return:
    """
    uuid = request.GET.get("id", None)
    reportInfo = Report.objects.filter(report_uuid=uuid)
    reportError = Report.objects.filter(report_uuid=uuid, result="失败")
    reportDetails = ReportInfo.objects.filter(report_uuid=uuid)
    phone = set([r.phone_name for r in reportInfo])
    if uuid:
        return render(request, "app/reportCount.html", {"reportInfo": reportInfo,
                                                        "reportError": reportError,
                                                        "phone": phone,
                                                        "reportDetail": reportDetails})
    else:
        return render(request, "app/page_500.html")


class reportInfoListView(ListCreateAPIView):
    """
    测试报告统计信息
    """
    def get_queryset(self):
        queryset = ReportInfo.objects.order_by("-id")[:7][::-1]
        return queryset

    serializer_class = ReportInfoSerializer
