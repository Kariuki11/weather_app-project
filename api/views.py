import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.conf import settings
weather_apikey = settings.WEATHER_API_KEY
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

class WeatherView(APIView):
    def get(self, request, *args, **kwargs):
        city = kwargs.get(city)
        url = f"{BASE_URL}?q={city}&appid={weather_apikey}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Request failed"}, status=status.HTTP_404_NOT_FOUND)