import random
import smtplib
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")


# 0 = Monday
# 1 = Tuesday
# 2 = Wednesday
# 3 = Thursday
# 4 = Friday
# 5 = Saturday
# 6 = Sunday

def get_random_quote():
    with open('quotes.txt', "r") as quotes_file:
        quotes = quotes_file.readlines()

    stripped_quotes = [quote.strip() for quote in quotes]
    return random.choice(stripped_quotes)


def send_productivity_message():
    now = dt.datetime.now()
    weekday = now.weekday()
    print("The current weekday is", weekday)

    if weekday == 0:
        random_quote = get_random_quote()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{receiver_email}",
                msg=f"Subject:Monday Motivation\n\n{random_quote}"
            )


send_productivity_message()
