from django.conf.urls import url, include

from . import views
app_name='todolist'
urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^add_work/$',views.add_work, name='add_work'),
    url(r'^(?P<pk>\d+)/work_done/$',views.work_done, name='work_done'),
    url(r'^(?P<pk>\d+)/not_done/$',views.not_done, name='not_done'),
    url(r'^(?P<pk>\d+)/remove_work/$',views.remove_work, name='remove_work'),
    
]
