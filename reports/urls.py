from django.urls import path

from . import views

urlpatterns = [
    path('injuryonduty/', views.injuryOnDuty, name='injuryonduty'),
    path('hazmatexpsoure/', views.hazMatExposure, name='hazmatexpsoure'),
    path('biologicalexposure/', views.biologicalExposure, name='biologicalexposure'),
    path('vehicleaccident/', views.vehicleAccident, name='vehicleaccident'),
]