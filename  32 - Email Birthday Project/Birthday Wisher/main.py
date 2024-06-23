##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import os
import random

my_email = "chescore81194@gmail.com"
my_password = "ogsmaafsayureotn"

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    birth_year = int(row['year'])
    birth_month = int(row['month'])
    birth_day = int(row['day'])
    email = row['email']
    name = row['name']

# 2. Check if today matches a birthday in the birthdays.csv
    now = dt.datetime.now()
    day = now.day
    month = now.month

    if birth_month == month and birth_day == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letter = random.choice(os.listdir("./letter_templates"))
        with open(f"./letter_templates/{letter}", "r+") as file:
            data = file.read()
            new_data = data.replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject:Happy Birthday!\n\n{new_data}")
