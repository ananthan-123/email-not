
# from pdftools.settings import STATIC_URL
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('storedata/', views.storeData, name='storeData'),
    path('activate/<int:activate_id>', views.activate, name='activateView'),
]
