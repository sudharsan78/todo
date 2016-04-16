from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views




app_name='todoapi'
urlpatterns=[
   
    url(r'^$', views.TodoAPIView.as_view()),
  
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
