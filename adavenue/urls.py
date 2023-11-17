# adavenue/urls.py
from django.contrib import admin
from django.urls import path, include
from website import urls as website_urls  # Import the 'urls' module from the 'website' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(website_urls.urlpatterns)),  # Include the urlpatterns directly
]
