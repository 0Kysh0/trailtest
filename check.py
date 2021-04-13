import requests
import json
import telegram
import os
import time
from os import environ
from bs4 import BeautifulSoup

URL = environ['predator_link']

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
stock = soup.find(id = "priceblock_ourprice")

def notify_ending(message):
    token = environ['telegram_token']
    chat_id = environ['telegram_chat_id']    
    
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

while(True):
    if stock is None:
        print('Not in stock. Sad')
    else:
        notify_ending(f" Laptop's up for grabs! Price is {float(stock.get_text().replace(',','')[2:])}")
    time.sleep(50)
