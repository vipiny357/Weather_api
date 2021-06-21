import requests
from datetime import datetime
import os
import sys

api_key = '7b264409fa9433b3e2f6bcc9ee796905'

location = (input("Please enter your City: ").strip()+',India').strip()

api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+api_key

api_req = requests.get(api_link)
api_data = api_req.json()


try:
    temp_city = ((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']

    sunrise_t = api_data['sys']['sunrise']
    sunrise = datetime.fromtimestamp(sunrise_t)
    sunset_t = api_data['sys']['sunset']
    sunset = datetime.fromtimestamp(sunset_t)

    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


    sys.stdout = open("logss.txt", "a")

    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",humidity, '%')
    print ("Current wind speed    :",wind_speed ,'kmph')
    print ("Today's Sunrise Time  :",sunrise)
    print ("Today's Sunset Time  :",sunset)

    sys.stdout.close()
except:
    print("You might have entered a wrong place.\nPlease visit again ")