from django.urls import path
from crm_application.views import home_view

urlpatterns = [
    path('', home_view, name = 'index')
]