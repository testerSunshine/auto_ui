
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from report.models import ReportInfo, Report
from report.serializers import ReportInfoSerializer


def reportDetail(request):
    """测试报告详情列表"""
    return render(request, "app/report.html", {"report": ReportInfo.objects.order_by("-id")})


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
