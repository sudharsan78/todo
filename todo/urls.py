
from django.conf.urls import url, include
from django.contrib import admin



urlpatterns = [
    
    #url(r'^todolist/', include('todolist.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^todolist/todoapi/v1/', include('todolist.urls')),  
   
]
