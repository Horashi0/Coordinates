#This project gets your coordinates either manually or automatically. 

import datetime as dt
import webbrowser
import requests

# Go to openweather.org and register an account and create a API key.
API_key = ""

#IP Grabber
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

#IP Grabber
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

choice = input("Would you like to get your coodinates automatically(1) or manually(2)")
#Automatically gets your coordinates
if choice == "1":
    city = get_location()["city"]
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API_key}&units=metric" + \
        API_key+"&q="+city
    weather_data = requests.get(url).json()
    latitude = weather_data["coord"]["lon"]
    longtitude = weather_data["coord"]["lat"]
    print(f"The latitude of {city} is: {longtitude}")
    print(f"The latitude of {city} is: {latitude}")
    print(f"To use this on google maps please copy this format:{longtitude},{latitude}")
    webbrowser.open(f"https://www.google.co.uk/maps/@{longtitude},{latitude},15z")
#Manually gets your coordinates
if choice == "2":
    location = input(
    "What location would you like to look up? ")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API_key}&units=metric" + \
    API_key+"&q="+location
    weather_data = requests.get(url).json()
    latitude = weather_data["coord"]["lon"]
    longtitude = weather_data["coord"]["lat"]
    print(f"The latitude of {location} is: {longtitude}")
    print(f"The latitude of {location} is: {latitude}")
    print(f"To use this on google maps please copy this format:{longtitude},{latitude}")
    webbrowser.open(f"https://www.google.co.uk/maps/@{longtitude},{latitude},15z")
