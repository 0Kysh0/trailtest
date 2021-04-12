import requests
import json
import telegram
import os
import time
from os import environ
from bs4 import BeautifulSoup

URL = environ['nitro_link']
URL2 = environ['predator_link']

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}

page = requests.get(URL, headers = headers)
page2 = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')
stock1 = soup.find(class_ = "product-info-stock-sku").get_text()
stock2 = soup2.find(class_ = "product-info-stock-sku").get_text()

def notify_ending(message):
    token = environ['telegram_token']
    chat_id = environ['telegram_chat_id']    
    
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

while(True):
    if stock2.strip() != "Coming Soon" or stock1.strip() !="Coming Soon":
        notify_ending('One of them is in stock!')
    else:
        print('Still same')
    time.sleep(300)
