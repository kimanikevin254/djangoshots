from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('selenium/', include('seleniumshots.urls')),
    path('scrapingbee/', include('scrapingbeeshots.urls')),
    path('urlbox/', include('urlboxshots.urls')),
]
