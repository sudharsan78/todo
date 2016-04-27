
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    url(r'^todo/', include('todolist.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/todo/', include('api.urls')),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
