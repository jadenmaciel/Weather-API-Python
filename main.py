import datetime as dt 
import requests 
import pytz

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CITY = "Las Vegas"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
descripition = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'], tz=pytz.UTC)
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'], tz=pytz.UTC)
local_timezone = pytz.FixedOffset(response['timezone'] // 60)
sunrise_time = sunrise_time.astimezone(local_timezone)
sunset_time = sunset_time.astimezone(local_timezone)

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind speed in {CITY}: {wind_speed} m/s")
print(f"Sunrise in {CITY} at: {sunrise_time} local time.")
print(f"Sunset in {CITY} at: {sunset_time} local time.")
print(f"General Weather in {CITY}: {descripition}")
