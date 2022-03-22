from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('poll/', views.getAllOrCreate, name='get-all-or-create-polls'),
    path('poll/<str:pk>', views.getSpecificPollOrDelete, name='get-specific-poll'),
]