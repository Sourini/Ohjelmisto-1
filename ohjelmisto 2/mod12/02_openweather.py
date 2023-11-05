# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api.
# Your task is to write a program that asks the user for the name of a municipality and then
# prints out the corresponding weather condition description text and temperature in Celsius degrees.
# Take a good look at the API documentation. You must register for the service to receive the API key
# required for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.

import requests
import json

# api-key 29e67b60a9fbfc8deb127327c47e4cbd


location = input("Enter the municipality you would like the fetch the weather for: ")

coordinate_request = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid=29e67b60a9fbfc8deb127327c47e4cbd"
coordinates_from_api = requests.get(coordinate_request).json()


weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates_from_api[0]['lat']}&lon={coordinates_from_api[0]['lon']}&units=metric&appid=29e67b60a9fbfc8deb127327c47e4cbd"
weather_from_api = requests.get(weather_request).json()

#print(weather_request)

#print(json.dumps(weather_from_api, indent=2))

print(f'Current temperature in {location}: {weather_from_api["main"]["temp"]} celsius.\nCurrent weather condition in {location}: {weather_from_api["weather"][0]["main"]}')