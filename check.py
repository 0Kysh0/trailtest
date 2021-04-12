import requests
import json
import telegram
import os
from os import environ
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/ASUS-GeForce-RTX-3060-Graphics-Graphite-FA506QM-HN008TS/dp/B08XBSV648'
URL2 = 'https://www.amazon.in/Redgear-Blaze-backlit-keyboard-aluminium/dp/B073QQR2H2/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}

page = requests.get(URL, headers = headers)
def check_availability():
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id = "priceblock_ourprice")
    if price == None:
        notify_ending('It is still not available. Sadge')
    else:
        current_price = price.get_text().replace(',','')[2:6]
        mesge = f"The price is {current_price}"
        notify_ending(mesge)
        #send_mail() 

def notify_ending(message):
    token = environ['telegram_token']
    chat_id = environ['telegram_chat_id']    
    
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

check_availability()
# with open('./getUpdates.json', 'r') as keys_file:
#         k = json.load(keys_file)
#         token = k['telegram_token']
#         chat_id = k['telegram_chat_id']
#         print(token)    