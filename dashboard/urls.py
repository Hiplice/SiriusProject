from dashboard import views
from django.urls import path

urlpatterns = [
    path('', views.load_dashboard),
    path('getconsent/', views.get_consent),
    path('getdata/', views.get_data),
]
