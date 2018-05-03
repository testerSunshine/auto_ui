from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from report import views

urlpatterns = [
    url(r'reportDetail/$', views.reportDetail, name='reportDetail'),
    url(r'reportCount/$', views.reportCount, name='reportCount'),

    url(r'^reportInfo/$', views.reportInfoListView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)