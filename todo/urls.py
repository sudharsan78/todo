
from django.conf.urls import url, include
from django.contrib import admin



urlpatterns = [
    
    url(r'^todo/', include('todolist.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/todo/', include('api.urls')),
   
]
