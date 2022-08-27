import time

import requests

import pyfiglet

import os

os.system("py -m pip install pyfiglet")

os.system('clear')

os.system("py -m pyfiglet --font=5lineoblique --color=GREEN Vexxo")

msg = input("Webhook Message -> ")

webhook = input("Webhook Link -> ")

def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent Msg {msg}")
        except:
            print("Bad Webhook ->" + webhook)
            time.sleep(5)
            exit()

vexxo_top = 1

while vexxo_top == 1:
    spam(msg, webhook)
