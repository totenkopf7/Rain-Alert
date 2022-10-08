#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import time
import smtplib

MY_EMAIL = "kurdishlearner2018@gmail.com"
MY_PASSWORD = "jarelnzsbyooilej"
rain_logo = """  
                   000000000000000000
             00000000000000000000000000
                    00000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000
              / / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
          / / / / / / / / / / / / / /
          / / / / / / / / / / / / /
        / / / / / / / / / / / /
        / / / / / / / / / /
"""
message = [f"{rain_logo}\nEnjoy your day, it's a rainy day today!!!",  "It's your favorite weather today, it's cloudy.", "Don't be so happy, the sky is clear today..."]
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

weather_params = {
    "lat": "26.821650",
    "lon": "95.099007",
    "appid": "1e379316d41238a0e2896779eae5c6af",
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

        print("Enjoy your day, it's a rainy day today!!!")
        send_email(message[0])
        
        
    
    elif is_cloudy:
        print("It's your favorite weather today, it's cloudy.")
        send_email(message[1])
        

        
    
    elif clear_sky:
        print("Don't be so happy, the sky is clear today...")
        send_email(message[2])
        


