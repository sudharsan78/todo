from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.generic import TemplateView


app_name='api'
urlpatterns=[
    url(r'^$', views.TodoAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.TodoDetail.as_view()),
      
]
urlpatterns = format_suffix_patterns(urlpatterns)
