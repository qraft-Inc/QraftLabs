
from django.contrib import admin
from django.urls import path
from labswebsite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view ),
    path('', home_view ),
]
