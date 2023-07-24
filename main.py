#install requests
#install beautifulsoup

# Requests help to work with https requests
import requests

# BeautifulSoup helps to scrap the web
# I haven't used BeautifulSoup now because I used the JSON file given by Steam API
#from bs4 import BeautifulSoup

#Email package to read, write, and send emails
#Importing smtplib for the sending function
import smtplib

# Importing the email modules
from email.message import EmailMessage

#Security Socket Layer
import ssl

#import logging
import logging
import logging.handlers
import os



# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available"


def send_email(game, price):
    email_sender = 'spencer.sv20@gmail.com'
    email_password = 'omvsotnnnwqxhwus'
    email_receiver = 'yuqinghao777@gmail.com'

    subject = f'Steam {game} price is lower!'
    body = f'Now {game} is {price}'

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())

#cookies = {'steamCountry': 'TW%7C6b3e2467d2049673f0bab34a1dec806d'}
#cookies2 = {'browserid': '2921198029950988778'}
#cookies3 = {'steamLoginSecure': '76561199160398054%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQwQl8yMkUwQjVBMl9DMjk4OSIsICJzdWIiOiAiNzY1NjExOTkxNjAzOTgwNTQiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5MDE5MzI3MCwgIm5iZiI6IDE2ODE0NjY0NTYsICJpYXQiOiAxNjkwMTA2NDU2LCAianRpIjogIjBEMUNfMjJFMEI1QTBfOTZBMTgiLCAib2F0IjogMTY5MDEwNjQ1NiwgInJ0X2V4cCI6IDE3MDg2OTM2ODgsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIzOS4xNS40OS4xNzUiLCAiaXBfY29uZmlybWVyIjogIjM5LjE1LjQ5LjE3NSIgfQ.aqT4pemtwt2f3oRP3gxJ9OxA4Mzy-YsUxtDupQ7cFMf7cBaj_clSILIfcFj58RB_bJWIik6FVJ8Pyim2bbDnDg'}
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
})

#Getting the info for game 1426210
#r = session.post("https://store.steampowered.com/api/appdetails?appids=1426210", cookies=cookies)
#print("This is the frist post request: ", r.status_code)
#r = session.post("https://store.steampowered.com/api/appdetails?appids=1426210", cookies=cookies2)
#print("This is the second post request: ", r.status_code)
#r = session.post("https://store.steampowered.com/api/appdetails?appids=1426210", cookies=cookies3)
#print("This is the third post request: ", r.status_code)
r = session.get('https://store.steampowered.com/api/appdetails?appids=1426210')
r_json = r.json()


name = r_json['1426210']['data']['name']
description = r_json['1426210']['data']['detailed_description']
requirements = r_json['1426210']['data']['pc_requirements']
currency = r_json['1426210']['data']
price = r_json['1426210']['data']['price_overview']['final_formatted']
price_float = float(price.replace("$", ""))


logger.info(f"Token value: {SOME_SECRET}")
if price_float <= 15.99:
    print("it's getting lower")
    send_email(name, price_float)








