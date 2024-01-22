import smtplib
import datetime
import random
import string

now = datetime.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

my_email = "@gmail.com"
my_password = ""

if day_of_week == 4:
    with open("quotes.txt", "r") as quotes:
        quotesList = quotes.readlines()
        random_quote = random.choice(quotesList)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="mbrunocampos20@gmail.com",
                            msg=f"Subject:Hello \n\n This is a Test email from a Python code"
                                f" read this quote: \n {random_quote} \n Thank you"
                            )


