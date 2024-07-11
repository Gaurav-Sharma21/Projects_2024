# International Space Station Tracker 


import requests 
from datetime import datetime
import time

MY_LAT = 49.815273
MY_LONG = 6.129583

def internation_space_station_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    lat_data = float(response.json()["iss_position"]["longitude"])
    long_data = float(response.json()["iss_position"]["latitude"])
    if MY_LAT-5 <= lat_data <= MY_LAT+5 and MY_LONG-5 <= long_data <= MY_LONG+5:
        return True


def is_night_time():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True 
    
while True:
    time.sleep(60)
    if internation_space_station_close() and is_night_time():
        # We can also send an email to ourselves using smtplib or keep track by creating a text file with the time
        # For program completion in one go I am using a print statement 
        print("The internation space station is above my city position")
    else:
        print("Sorry it is still not at the desired position")



