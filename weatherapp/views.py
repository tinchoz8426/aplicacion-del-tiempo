from django.shortcuts import render

import requests
import datetime
import environ

env = environ.Env()
environ.Env.read_env()

def index(request):
    
    if request.method == "POST":
        city = request.POST['city']
    else:
        city = "washington"


    APP_ID = env('APP_ID')
    URL = "https://api.openweathermap.org/data/2.5/weather"
    # tambien se la suele llamar payload (carga util)
    PARAMS = {'q': city, 'appid': APP_ID, 'lang': "es", 'units': 'metric'}

    req = requests.get(url=URL, params=PARAMS)
    response = req.json()

    try:
        description = response["weather"][0]["description"]
        image = response["weather"][0]["icon"]
        humidity = response["main"]["humidity"]
        temperature = response["main"]["temp"]
        pressure = response["main"]["pressure"]
        wind = response["wind"]["speed"]
        location = response["name"]
        country = response["sys"]["country"]
        # Para que se tome el horario en español, debemos cambiar en settings a español --> LANGUAGE_CODE = 'es-ar'
        today = datetime.datetime.now()
    except:
        description = None
        image = None
        humidity = None
        temperature = None
        pressure = None
        wind = None
        location = None
        country = None
        today = None

    context = {
        'description': description,
        'image': image,
        'humidity': humidity,
        'temp': temperature,
        'location': location,
        "country": country,
        'today': today,
        'pressure': pressure,
        'wind': wind,
        }

    return render(request, 'weatherapp/index.html', context)