import smtplib
import datetime as dt
import pandas
import random
def send_email(email, name):
    my_email = #Hidden For Privacy Purposes
    my_password = #Hidden For Privacy Purposes
    temp = random.randint(1,3)
    with open(f"./letter_templates/letter_{temp}.txt") as file:
        letter = file.read()
    letter = letter.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="#Hidden For Privacy Purposes",
                            msg=f"Send:Happy Birthday!\n\n{letter}"
                            )
        connection.close()

now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient="records")
for birthday in birthdays_dict:
    if birthday["month"] == now.month and birthday["day"] == now.day:
        send_email(birthday["email"],birthday["name"])
