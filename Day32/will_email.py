import smtplib
import datetime as dt
import pandas
import math
import requests

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "bakerlois01@gmail.com"
will_email = "wboulton12@gmail.com"  # smtp.mail.yahoo.com
my_password = "100daysofcode"

response = requests.get(url='https://api.kanye.rest')
response.raise_for_status()
quote = response.json()["quote"]
time5k = pandas.read_csv('time5k.csv')
time5kint = int(time5k['5k time'])
mins = math.floor(time5kint/60)
secs = time5kint - 60*mins
time5kstr = f"{mins} minutes {secs} seconds"
print(time5kstr)
time5kint -= 20
time5k['5k time'] = time5kint
time5k.to_csv('time5k.csv', index=False)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='loiselizabaker@gmail.com',
                        msg=f"Subject:Good morning William 🐋\n\n"
                            f"Always remember, Kanye says:\n{quote} \n"
                            f"This week, you should run 5km in {time5kstr}. Chop chop 🏃🏻🏃🏻🏃🏻.")