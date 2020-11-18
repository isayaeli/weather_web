from django.shortcuts import render
import requests

# Create your views here.
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q=Dar es salaam&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	url1 = 'http://api.openweathermap.org/data/2.5/weather?q=Arusha&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	url2 = 'http://api.openweathermap.org/data/2.5/weather?q=Mwanza&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

	city_weather = requests.get(url.format()).json() #request the API data and convert the JSON to Python data types
	city_weather1 = requests.get(url1.format()).json()
	city_weather2 = requests.get(url2.format()).json()
	weather = {
        # dar city data,
        'temperature' : city_weather['main']['temp'],
        'humidity' : city_weather['main']['humidity'],
        'pressure' : city_weather['main']['pressure'],
        'description' : city_weather['weather'][0]['description'],
        'wind' : city_weather['wind']['speed'],
        'icon' : city_weather['weather'][0]['icon'],
          #Arusha city data
        'temperature1' : city_weather1['main']['temp'],
         'humidity1' : city_weather1['main']['humidity'],
         'pressure1' : city_weather1['main']['pressure'],
        'description1' : city_weather1['weather'][0]['description'],
        'wind1' : city_weather1['wind']['speed'],
        'icon1' : city_weather1['weather'][0]['icon'],
          #Mwanza city data
        'temperature2' : city_weather2['main']['temp'],
        'humidity2' : city_weather2['main']['humidity'],
        'pressure2' : city_weather2['main']['pressure'],
        'description2' : city_weather2['weather'][0]['description'],
        'wind2' : city_weather2['wind']['speed'],
        'icon2' : city_weather2['weather'][0]['icon']
    }
	context = {'weather' : weather}	
	return render(request, 'weather.html', context)