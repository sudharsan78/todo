from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name='todolist'
urlpatterns=[
   
    url(r'^$', views.index.as_view()),
  
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
