from . import views
from django.urls import path

urlpatterns = [
    path('', views.endpoints, name='WeatherHome'),
    path('api/weather/<str:city>/', views.WeatherView.as_view(), name='weatherView'),
]
