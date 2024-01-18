##################### Normal Starting Project ######################
import random,smtplib,pandas,datetime, string

user = ""
password =""
def sendmail(to_email, letter):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr="", to_addrs=to_email, msg=letter)
def letter_chooser():
    with open("letter_templates/letter_1.txt", "r") as letter1:
        l1 =letter1.read()
    with open("letter_templates/letter_2.txt", "r") as letter2:
        l2 = letter2.read()
    with open("letter_templates/letter_3.txt", "r") as letter3:
        l3 = letter3.read()
        list_letters = [l1,l2,l3]
        letter_chosen = random.choice(list_letters)
        return letter_chosen
#data treatment
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)
now= datetime.datetime.now()
nowd = now.day
nowm = now.month
print(nowd)
length = len(data_dict)

for a in range(0, length-1):
    tmp = data_dict[a]
    int_month = int(tmp["month"])
    if int_month == nowm:
        int_day = tmp["day"]
        if int_day == nowd:
            # it's the day to send a message
            name = str(tmp["name"])
            email = str(tmp["email"])
            letter = str(letter_chooser())
            edited_letter = letter.replace("[NAME]",name )
            sendmail(email,edited_letter)

























# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



