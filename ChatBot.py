# -*- coding: utf-8 -*-
#! /usr/bin/env python
import os 
import requests


def get_bot_updates(offset):
    url = "https://api.telegram.org/bot564880207:AAEseyuy6zZKOgFYcdj3lTuvbF_sKGkfpXM/getUpdates"
    params = {'offset': offset} 
    response = requests.get(url, params=params)
    decoded = response.json()
    result = decoded['result']
    get_message = []
    for update in result:
        id_update = update['message']['from']['id']
        text_update = update['message']['text']
        offset = update["update_id"] + 1
        get_message.append([id_update, text_update])
    return get_message, offset


def send_message_bot(chat_id, text):
    parameters = {'chat_id':chat_id, 'text': text}
    response = requests.get("https://api.telegram.org/bot564880207:AAEseyuy6zZKOgFYcdj3lTuvbF_sKGkfpXM/sendMessage", params=parameters)
    decoded = response.json()


def btc_course():
    url = "https://api.cryptonator.com/api/ticker/btc-usd"
    response = requests.get(url)
    decoded = response.json()
    ticker = decoded ["ticker"]
    course = ticker ['price']
    return str(course)


def eth_course():
    url = "https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=RUB"
    response = requests.get(url)
    decoded = response.json()
    ticker = decoded [0]["price_usd"]
    return str(ticker)
 
    
offset = 0
while True:
    get_message, offset = get_bot_updates(offset)
    for message in get_message:
        chat_id = message[0]
        text = message[1]
        if "Start" in text:
            send_message_bot (chat_id, "Hello! My name is EtheriumCryptoBot.")
        elif "Btc" in text:
            send_message_bot (chat_id, "Current BITCOIN course: " + btc_course())
        elif "Eth" in text:
            send_message_bot (chat_id, "Current ETHERIUM course: " + eth_course())  
        elif "Exit" in text: 
            send_message_bot (chat_id, "Thank you for your visit, I wish you all the best!")
        else: send_message_bot (chat_id, "Please, enter the command 'Start' - for information about me. 'Btc' or 'Eth' commands to find out the current BITCOIN course or the current ETHERIUM course. Enter 'Exit' to say goodbye to me.")