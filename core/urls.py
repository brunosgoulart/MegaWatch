from django.urls import path
from .views import Energy, EnergyUpdate, DailyEnergy

urlpatterns = [
    path('', Energy),
    path('energy-update', EnergyUpdate),
    path('energy-daily', DailyEnergy)
]