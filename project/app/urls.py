from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'project/', views.home),
]+ static(settings.STATIC_URL)



