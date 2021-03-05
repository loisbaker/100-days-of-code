import smtplib
import datetime as dt
import random

my_email = "bakerlois01@gmail.com"
my_other_email = "bakerlois01@yahoo.com"  # smtp.mail.yahoo.com
my_password = "100daysofcode"

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 4:
    with open('quotes.txt') as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_other_email,
                                msg=f"Subject:Your daily motivational quote\n\n{quote}")

