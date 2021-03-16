import requests
from datetime import datetime
import time
import smtplib

my_email = "bakerlois01@gmail.com"
my_password = "100daysofcode"
my_real_email = "loiselizabaker@gmail.com"

MY_LAT = 51.507351 # Your latitude
MY_LON = -0.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (abs(iss_latitude - MY_LAT) < 5) and (abs(iss_longitude - MY_LON) < 5):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if (time_now.hour >= sunset) or (time_now.hour < sunrise):
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=[my_real_email,'adjelley@gmail.com'],
                                msg=f"Subject:Look up!\n\nThe ISS is above you now 👽")



