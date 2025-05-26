from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('results/', include('results.urls')),
]