from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from devsearch.settings import MEDIA_ROOT, STATIC_ROOT



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('projects/', include('projects.urls')),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=STATIC_ROOT)
