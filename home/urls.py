from django.conf.urls import url
from django.views.static import serve

from auto_ui.settings import MEDIA_ROOT
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^image/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
]


