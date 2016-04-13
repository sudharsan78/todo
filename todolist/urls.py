from django.conf.urls import url, include

from . import views
app_name='todolist'
urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^add_work/$',views.add_work, name='add_work'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
