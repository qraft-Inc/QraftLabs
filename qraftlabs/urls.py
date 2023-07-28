
from django.contrib import admin
from django.urls import path
from labswebsite.views import *
from qraftlabs import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view ),
    path('', home_view ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

