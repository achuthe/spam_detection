from django.contrib import admin
from django.urls import path, include
from api.views import home

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

