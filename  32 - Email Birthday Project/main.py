import smtplib
import datetime as dt
import random
import os

now = dt.datetime.now()
day_of_the_week = now.strftime('%A')
print(day_of_the_week)

with open("quotes.txt") as file:
    data = file.read()
    quotes_list = data.splitlines()
    print(quotes_list)

quote = random.choice(quotes_list)
print(quote)

my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="chescore81194@yahoo.com",
                        msg=f"Subject:Quote of the day!\n\n{quote}")

