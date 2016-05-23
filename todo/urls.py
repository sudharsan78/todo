
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views


urlpatterns = [
    
    url(r'^', include('todolist.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/todo/', include('api.urls')),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token)
]