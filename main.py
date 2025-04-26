import os
import time
import requests

# Install pyfiglet if needed
os.system("py -m pip install pyfiglet")
import pyfiglet

# Clear screen - use 'cls' for Windows
os.system('cls')

# Display banner
os.system("py -m pyfiglet --font=5lineoblique --color=GREEN Vexxo")

# Get user inputs
msg = input("Webhook Message -> ")
webhook = input("Webhook Link -> ")
numbers = int(input("Number of Msgs -> "))  # Convert to integer immediately

def spam(msg, webhook, count):
    remaining = count
    while remaining > 0:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent Msg {msg} ({count - remaining + 1}/{count})")
                remaining -= 1
            else:
                print(f"Failed to send message. Status code: {data.status_code}")
                time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            print("Bad Webhook -> " + webhook)
            print("If You click ctrl + c click again to kill")
            time.sleep(5)
            return False
    return True

# Send the messages once
spam(msg, webhook, numbers)
print("All messages sent successfully!")
