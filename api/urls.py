from . import views
from django.urls import path

urlpatterns = [
    path('', views.WeatherView.as_view(), name='WeatherHome'),
    path('api/weather/', views.WeatherView.as_view(), name='weatherView'),
]
