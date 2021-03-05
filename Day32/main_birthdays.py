import smtplib
import datetime as dt
import pandas
import random

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "bakerlois01@gmail.com"
my_other_email = "bakerlois01@yahoo.com"  # smtp.mail.yahoo.com
my_password = "100daysofcode"

letters_list = [f"./letter_templates/letter_{num}.txt" for num in range(1,4)]


with open('birthdays.csv') as birthday_file:
    birthdays = pandas.read_csv(birthday_file)
    for index, row in birthdays.iterrows():
        if row["month"] == month and row["day"] == day:
            name = row["name"]
            email = row["email"]
            letter_template_file = random.choice(letters_list)
            with open(letter_template_file) as letter_file:
                letter_text = letter_file.read()
                personalised_letter_text = letter_text.replace('[NAME]', name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg=f"Subject:Happy Birthday!\n\n{personalised_letter_text}")
                print(f'Email sent to {email}')



