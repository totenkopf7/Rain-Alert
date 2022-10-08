#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. API_KEY, LAT/LON

import requests
import time
import smtplib

MY_EMAIL = "Your Email"
MY_PASSWORD = "Your Password"

message = ["\nIt's going to rain today. Remember to bring an ☂️.",  "It's gonna be cloudy today.", "It's sunny outside. Don't forget to use sun cream."]
def send_email(message):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=message
        )
    
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
LATITUDE = ""
LONTITUDE = ""
API_KEY = ""

weather_params = {
    "lat": LATITUDE,
    "lon": LONTITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
is_cloudy = False
clear_sky = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    if int(condition_code) >= 801:
        is_cloudy = True
    if int(condition_code) == 800:
        clear_sky = True

while True:
    #time.sleep(60)
    if will_rain:

        print("It's going to rain today. Remember to bring an ☂️. ;)")
        send_email(message[0])
        
        
    
    elif is_cloudy:
        print("It's going to be dark and cloudy today.")
        send_email(message[1])
        

        
    
    elif clear_sky:
        print("It's sunny outside. Don't forget to use sun cream..")
        send_email(message[2])
        


