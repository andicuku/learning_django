from django.urls import path
from crm_application.views import home_view, specific, lead_create
app_name = 'crm_application'
urlpatterns = [
    path('', home_view, name='index'),
    path('<int:pk>/', specific, name='specific'),
    path('create', lead_create, name='create')
]