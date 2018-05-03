# coding=utf-8
from time import timezone

from rest_framework import serializers, models
from rest_framework.fields import DateTimeField

from report.models import ReportInfo


class ReportInfoSerializer(serializers.ModelSerializer):
    """
    测试报告详情序列化
    """
    def to_representation(self, instance):
        """
        将更新时间变成天
        :param instance:
        :return:
        """
        ret = super(ReportInfoSerializer, self).to_representation(instance)
        ret["case_date"] = ret["case_date"].split("T")[0]
        return ret

    class Meta:
        model = ReportInfo
        fields = ("case_sum", "case_pass_sum", "case_fail_sum", "case_date", )

