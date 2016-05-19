from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.generic import TemplateView


app_name='api'
urlpatterns=[
    url(r'^$', views.TodoAPIView.as_view()),
    # url(r'^$', views.api_root),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
    url(r'^(?P<pk>\d+)$', views.TodoDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	url(r'^users/tasks/$', views.UserTaskList.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]
