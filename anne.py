#CODE BY Sythe
import requests
import re
import os
from bs4 import BeautifulSoup as bs
import random
import urllib3
from mahdix import *
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import threading
clear()
import os
from mahdix import *
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor
import re
import requests
import json
import random
import json
import requests
import uuid
import string
import base64
import urllib
import urllib3
import re
import os
import time
import sys
from datetime import datetime
from urllib.request import urlopen
from time import sleep as slp
import re
import requests
import json
import os
import random
import string
import uuid
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests
import json
import sys
import os
import platform
import re
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
R="[bold red]"
G="[bold green]"
Y="[bold yellow]"
B="[bold blue]"
M="[bold magenta]"
P="[bold violet]"
C="[bold cyan]"
W="[bold white]"
r="\033[1;31m"
g="\033[1;32m"
y="\033[1;33m"
b="\033[1;34m"
m="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
import re
import re
import requests

def get_combined_data(url):
    """
    Fetch the response from the given URL and extract the `actrs` number and `post_id`.
    Combine these values and return the result.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        str: The combined string of `actrs` number and `post_id`, or an error message.
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'cache-control': "max-age=0",
        'dpr': "2",
        'viewport-width': "980",
        'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Linux\"",
        'sec-ch-ua-platform-version': "\"\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"131.0.6778.104\", \"Chromium\";v=\"131.0.6778.104\", \"Not_A Brand\";v=\"24.0.0.0\"",
        'sec-ch-prefers-color-scheme': "light",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9",
        'priority': "u=0, i",
        'Cookie': "sb=fuZTZ8Zyl9dXj5TFodlxDrGD; dpr=2; wd=980x1628; datr=fuZTZxL-gtbBjTkfeBq-VVDZ"
    }

    try:
        response = requests.get(url, headers=headers).text

        # Extract `actrs` number
        actrs_match = re.search(r'"actrs\\":\\"(\d+)\\"', response)
        actrs_number = actrs_match.group(1) if actrs_match else None

        # Extract `post_id`
        post_id_match = response.split('"post_id":"')[1].split('"')[0] if '"post_id":"' in response else None

        if actrs_number and post_id_match:
            return f"{actrs_number}_{post_id_match}"
        elif not actrs_number:
            return "actrs number not found!"
        elif not post_id_match:
            return "post_id not found!"

    except Exception as e:
        return f"An error occurred: {str(e)}"
def extract_facebook_video_id(url):
    # Regular expression pattern to match the user ID and video ID
    pattern = r'facebook\.com/(\d+)/videos/(\d+)/'
    
    # Search for the pattern in the URL
    match = re.search(pattern, url)
    
    if match:
        # Extract the user ID and video ID
        user_id, video_id = match.groups()
        return f"{user_id}_{video_id}"
    else:
        return None

# Example usage:


def extract_ids(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    else:
        return None 
def get_approval_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

    
def jovan():
    adrkz = "\033[34m "
    
    
    print(f"""
    {green} 
                

           ░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗░██████╗
           ██╔══██╗██╔══██╗████╗░████║██║████╗░██║██╔════╝
           ███████║██║░░██║██╔████╔██║██║██╔██╗██║╚█████╗░
           ██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║░╚═══██╗
           ██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║██████╔╝
          ╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░
                 {white} https://exoboost.site
     {red}──────────────────────────────────────────────────────────────────────\033[0m
     {red}OWNER     {white}: {yellow} Frack  
     {red}FACEBOOK  {white}: {yellow} None
     {red}──────────────────────────────────────────────────────────────────────\033[0m""")

import os
import time
import requests
import logging

def get_approval_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text



def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([
        True,
        False])
    if is_win64:
        if not 'WOW64;':
            user_agent = f'''Mozilla/5.0 (Windows NT {windows_version}.{''}Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'''
            return user_agent
import os
import uuid
import random
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import string  # Added for generating random characters in get_ua()

import os

import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
# Color codes for formatting output
purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
import random
import string
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))

    # Randomly vary the Android OS version, device, and app version for realism
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))  # Updated range for FBAV versions
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])

    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    
    return ua_bgraph

ua_bgraph = generate_user_agent()


import requests
import random
import concurrent.futures as thread
import os
import string

# Random FB version generation
fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))

# User agent string
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        
        if uid in existing_uids:
            print(f"     {yellow}[INFO] {red}ACCOUNT --> {white}{uid} {red}already exists.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            return

        response = requests.post(url, data=data).json()
        
        print(response)
        if 'access_token' in response:
            token = response['access_token']

            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")

            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: Extracted Account ─────> {uid}.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            success_count.append(uid)
        else:
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT Account ─────> {uid}.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except Exception as e:
        print(f"     \033[1;31m[ERROR]\033[0m Error extracting account: {uid}. Reason: {str(e)}\033[0m\n")


def proz(accounts_file, token_output_path, extract_type):
    """Process the accounts and extract tokens concurrently."""
    success_count = []

    # Load existing uids from the output file to avoid duplicates
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
        return

import requests
import random
import concurrent.futures as thread
import os
import string

fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def load_existing_tokens(path_file):
    """Load existing accounts or pages from the output file."""
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}  # Set of existing uids or page ids
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token
    
    if uid in existing_tokens:
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
        return

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        response = requests.post(url, data=data).json()
        
        if 'access_token' in response:
            token = response['access_token']

            # Extract Facebook Pages associated with the account token
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}Page ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")

            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")

    except Exception as e:
        print(f"[ERROR] Error extracting account: {uid}. Reason: {str(e)}")

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    pages_data = []
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f'Error: {response.text}')
            return None
        
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        
        url = data.get('paging', {}).get('next')  # Update the URL for the next request

    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
def extraction():

    clear_screen()
    jovan()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {green}CHOICE: ").strip() 
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")
def axl2():
    clear_screen()
    jovan()
    folder_path = "/sdcard/boostphere"  
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    prozc(file_path, account_file, extract_type)
def axl1():
    clear_screen()
    jovan()
    folder_path = "/sdcard/boostphere"
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    token_output_path = account_file

    proz(file_path, token_output_path, extract_type)




    
folder_name = "/sdcard/boostphere"
file_names = ["FRAACCOUNT.txt", "FRAPAGES.txt", "RPWACCOUNT.txt", "RPWPAGES.txt","generated_code.txt"]



if not os.path.exists(folder_name):


    try:
          os.makedirs(folder_name)
    except Exception:
              pass
              


    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)

        if not os.path.exists(file_path):

            try:

                with open(file_path, 'w') as file:

                    pass  
            except Exception:

                pass  


def count_tokens(accounts_file, pages_file):
    """Count the number of accounts and pages stored in the respective files."""
    total_accounts = 0
    total_pages = 0

    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Account file not found: {accounts_file}")

    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Page file not found: {pages_file}")

    return total_accounts, total_pages
import os
import requests
import random
import string
import uuid
import random
def user_agint():
   

    
    fbcr_values = [
        "AT&T", "Orange France", "Telia Sweden","Vodafone Italy", "Sky Mobile","Proximus Belgium", "Movistar Spain", "Tele2 Netherlands", "Vodafone Spain", "Telekom Deutschland","Eir Ireland", "KPN Netherlands", "Three Ireland", "Telekom Austria", "Telia Sweden","Vodafone Italy", "Sky Mobile", "Proximus Belgium", "Movistar Spain", "Tele2 Netherlands","Vodafone Spain", "Telekom Deutschland", "Eir Ireland", "KPN Netherlands", "Three Ireland","Telekom Austria", "Telia Sweden", "Vodafone Italy", "Sky Mobile", "Proximus Belgium","Movistar Spain", "Tele2 Netherlands","Vodafone Spain", "Telekom Deutschland", "Eir Ireland","KPN Netherlands", "Three Ireland", "Telekom Austria", "China Mobile", "NTT Docomo", "KT Corporation", "Singtel","AIS Thailand", "Viettel", "Smart Communications", "PTCL Pakistan", "Grameenphone Bangladesh","Nepal Telecom", "MTN Nigeria", "T-Mobile USA", "Verizon Wireless", "Rogers Canada","O2 United Kingdom", "Telstra Australia", "TIM Brazil", "Vivo India", "Telenor Norway","Mobilink Pakistan", "Bell Canada", "Etisalat UAE", "Claro Mexico", "Orange Spain","Vodafone Portugal", "Telkomsel Indonesia","Beeline Russia", "MTS Russia", "Optus Australia","SK Telecom South Korea", "Entel Chile", "MTNL India", "Tigo Ghana", "Idea India","DTAC Thailand", "Zong Pakistan", "Orange Romania", "EE United Kingdom", "Digi Malaysia","Koodo Canada", "Yoigo Spain", "Airtel Nigeria", "Airtel Kenya", "Telekom Malaysia","Cosmote Greece", "Digicel Jamaica", "LIME Caribbean", "Telus Canada", "Sprint USA","Movistar Mexico", "Vodafone Germany", "Optus Australia","Vivo Brazil", "Singtel Singapore", "Airtel India", "Ncell Nepal", "Telenor Sweden","MEO Portugal", "Claro Argentina", "EE Estonia", "Telkom South Africa", "Telenor Norway","Yoigo Spain", "Giffgaff United Kingdom", "Lycamobile France", "A1 Telekom Austria", "Telenor Hungary","Vodafone Greece", "Cosmote Romania", "Telenor Serbia", "Vodafone New Zealand", "Telekom Croatia","Orange Belgium", "Telkomsel Indonesia", "Vivacom Bulgaria", "Orange Poland", "Rogers Canada","Telkom South Africa", "Lycamobile Germany", "M1 Singapore", "DT Mobile Austria", "Claro Colombia","Telkomsel Indonesia", "Tele2 Norway", "Telia Estonia", "Telenor Denmark","Rakuten Mobile Japan","Ooredoo Qatar","Movistar Argentina", "T-Mobile Netherlands", "Telekom Hungary", "Vodafone Romania","NOS Portugal", "Digicel Haiti", "Three Hong Kong", "Airtel Bangladesh", "Telcel Mexico","Orange Moldova", "Telkomsel Indonesia", "Telenor Bulgaria","Vodafone Ukraine", "Cosmote Greece","T-Mobile Czech Republic", "NetOne Zimbabwe", "Glo Nigeria", "MTS Belarus", "Cell C South Africa","Maxis Malaysia", "Fido Canada", "Zain Saudi Arabia", "Telenor Serbia", "Beeline Uzbekistan","A1 Telekom Austria", "Zong Pakistan", "Jazz Pakistan", "Vodafone Portugal", "Telstra Australia","Vodafone Ireland", "Orange Slovakia", "Claro Peru", "Vivo Brazil", "Vodafone Czech Republic","Telenor Montenegro", "Digi Malaysia", "Etisalat Egypt", "Tigo Rwanda", "Robi Bangladesh","MTC Namibia", "AIS Thailand", "Vodafone Greece", "Orange Romania", "T-Mobile Poland","Telenor Hungary", "Telia Latvia", "Ooredoo Oman", "Optus Australia", "Orange Belgium","Telenor Norway", "Lycamobile France", "EE Estonia", "Yoigo Spain", "Giffgaff United Kingdom","Sprint USA", "Telus Canada", "Vodafone Germany", "Movistar Mexico", "Telkomsel Indonesia","Vivo India", "Airtel India", "Ncell Nepal", "Telenor Sweden", "MEO Portugal","Claro Argentina", "Telekom Croatia", "Cosmote Romania", "Orange Poland", "Telenor Serbia","Vodafone New Zealand", "Vivacom Bulgaria", "Telenor Denmark", "T-Mobile Netherlands", "NOS Portugal","Telkomsel Indonesia", "Tele2 Norway", "Telia Estonia", "Telenor Denmark", "Rakuten Mobile Japan","Ooredoo Qatar", "Movistar Argentina", "T-Mobile Netherlands", "Telekom Hungary", "Vodafone Romania","Digicel Haiti", "Three Hong Kong", "Airtel Bangladesh", "Telcel Mexico", "Orange Moldova","Telkomsel Indonesia", "O2 Germany", "Airtel Nigeria", "Orange Kenya","Digicel Jamaica","Unitel Angola", "MobiFone Vietnam", "TMN Portugal", "Grameenphone Bangladesh", "Movitel Mozambique","Telkom South Africa", "Globacom Nigeria", "Nawras Oman", "Vodafone Ghana", "Telenor Pakistan","Yoigo Spain", "SFR France", "Tigo Colombia", "Vodafone Qatar", "Etisalat UAE","Telenor Norway", "Telia Finland", "LIME Caribbean", "EE United Kingdom", "Koodo Canada","TIM Italy", "Telekom Romania", "Jio India", "Ooredoo Kuwait", "Orange Switzerland","Bouygues Telecom France", "Entel Bolivia", "A1 Telekom Austria", "MTN South Africa", "Vodafone Hungary","Zain Jordan", "Ncell Nepal", "Zain Kuwait", "Djezzy Algeria", "Smart Philippines","Telenor Bulgaria", "Cosmote Greece", "Vodafone Portugal", "Telstra Australia", "Three Ireland","Rogers Canada", "Safaricom Kenya", "Orange Luxembourg", "Elisa Finland", "Vodafone Netherlands","KPN Netherlands", "Telia Lithuania", "Vodafone Iceland", "Tigo Ghana", "Idea India","Tata Docomo India", "Aircel India", "Claro Chile", "Movistar Peru", "T-Mobile Croatia","Telkomsel Indonesia", "O2 Czech Republic", "Smartfren Indonesia", "Axiata Malaysia", "Digicel Caribbean","Beeline Kazakhstan", "Moldcell Moldova", "Djezzy Algeria", "Tigo Rwanda", "Vodafone Egypt","COSMOTE Cyprus", "Bell Mobility Canada", "Telenor Sweden", "3 Sweden", "DNA Finland","Zain Bahrain", "Ooredoo Tunisia", "Orange Morocco", "Vivacom Bulgaria", "VIPnet Croatia","Vodafone Greece", "Orange Romania", "T-Mobile Poland", "Telenor Hungary", "AIS Thailand","TrueMove Thailand", "Vodafone Czech Republic", "Digi Malaysia", "XL Axiata Indonesia", "Dialog Sri Lanka","MTN Uganda", "Airtel Bangladesh", "Viva Kuwait", "Wind Italy", "LMT Latvia","Yoigo Spain", "Maroc Telecom Morocco", "Orange Ivory Coast", "Airtel Malawi", "Airtel Zambia", "DITO", "Globe", "GOMO", "TNT", "TM"]
   

    fbmf_fbdv_dict = {

    "asus": ["ZenFone 8", "ROG Phone 5", "ZenFone 7", "ROG Phone 3", "ZenFone 6", "ROG Phone II", "ZenFone 5Z", "ZenFone 5", "ZenFone 4 Pro", "ZenFone 4", "ZenFone 3 Deluxe", "ZenFone 3", "ZenFone 2 Laser", "ZenFone 2", "ZenFone", "ZenFone 6Z", "ZenFone Max Pro (M2)", "ZenFone Max Pro (M1)", "ZenFone 6Z", "ZenFone Max Plus (M2)", "ZenFone Max (M2)", "ZenFone Max (M1)", "ZenFone Live", "ZenFone Zoom", "ZenFone Selfie", "ASUS_Z01RD", "ASUS_Z01QD", "ASUS_I01WD", "ASUS_I01BD", "ASUS_I01HDA"],
    
    "lenovo": ["Legion Phone Duel 2", "Legion Phone Duel", "K12 Note", "K10 Note", "Z6 Pro", "Z5 Pro", "Lenovo Z6 Pro", "Lenovo Z6 Youth", "Lenovo Z5s", "Lenovo Z5 Pro GT", "Lenovo Z5 Pro", "Lenovo Z5", "Lenovo K9", "Lenovo A5", "Lenovo K320t", "Lenovo K8 Note", "Lenovo K6 Note", "Lenovo Vibe K5 Note", "Lenovo Vibe K5", "Lenovo Vibe P1", "Lenovo Vibe X3", "Lenovo Vibe Z2 Pro", "Lenovo Vibe Z2", "Lenovo Vibe Z","A6000", "A6000 Plus", "A7000", "A7000 Turbo", "A2010", "A2010-a", "K3 Note", "Vibe K4 Note", "Vibe K5 Note", "Vibe K5 Plus", "Vibe K5", "Vibe K5 Lite", "Vibe K5 Power", "Vibe K5 S", "Vibe X2", "Vibe X3", "Vibe Z2 Pro", "K6 Power", "K6 Note", "K6", "K6 Plus", "K6 Turbo", "Vibe C", "Vibe C2", "Vibe C2 Power", "Vibe C2 K10a40", "Vibe C2 K10a40C", "Vibe B", "Vibe B A2016a40", "Vibe B A2016b30", "Vibe B A2016b31", "Vibe B A2016b31C", "Vibe B A2016b30A", "Vibe B A2016b30B", "Vibe B A2016b30C", "Vibe B A2016b30D", "Vibe B A2016b30E", "Vibe B A2016b30G", "Vibe B A2016b30J", "Vibe B A2016b30K", "Vibe B A2016b30L", "Vibe B A2016b30M", "Vibe B A2016b30N", "Vibe B A2016b30O", "Vibe B A2016b30Q", "Vibe B A2016b30R", "Vibe B A2016b30T", "Vibe B A2016b30W", "Vibe B A2016b30Y", "Vibe B A2016b31A", "Vibe B A2016b31B", "Vibe B A2016b31C", "Vibe B A2016b31E", "Vibe B A2016b31F", "Vibe B A2016b31G", "Vibe B A2016b31H", "Vibe B A2016b31K", "Vibe B A2016b31L", "Vibe B A2016b31M", "Vibe B A2016b31N", "Vibe B A2016b31O", "Vibe B A2016b31P", "Vibe B A2016b31Q", "Vibe B A2016b31R", "Vibe B A2016b31S", "Vibe B A2016b31T", "Vibe B A2016b31U", "Vibe B A2016b31V", "Vibe B A2016b31W", "Vibe B A2016b31X", "Vibe B A2016b31Y", "Vibe B A2016b31Z", "Vibe B A2016b31AA", "Vibe B A2016b31AB", "Vibe B A2016b31AC", "Vibe B A2016b31AD", "Vibe B A2016b31AE", "Vibe B A2016b31AF", "Vibe B A2016b31AG", "Vibe B A2016b31AH", "Vibe B A2016b31AI", "Vibe B A2016b31AJ", "Vibe B A2016b31AK", "Vibe B A2016b31AL", "Vibe B A2016b31AM", "Vibe B A2016b31AN", "Vibe B A2016b31AO", "Vibe B A2016b31AP", "Vibe B A2016b31AQ", "Vibe B A2016b31AR", "Vibe B A2016b31AS", "Vibe B A2016b31AT", "Vibe B A2016b31AU", "Vibe B A2016b31AV", "Vibe B A2016b31AW", "Vibe B A2016b31AX", "Vibe B A2016b31AY", "Vibe B A2016b31AZ", "Vibe B A2016b31BA", "Vibe B A2016b31BB", "Vibe B A2016b31BC", "Vibe B A2016b31BD", "Vibe B A2016b31BE", "Vibe B A2016b31BF", "Vibe B A2016b31BG", "Vibe B A2016b31BH", "Vibe B A2016b31BI", "Vibe B A2016b31BJ", "Vibe B A2016b31BK", "Vibe B A2016b31BL", "Vibe B A2016b31BM", "Vibe B A2016b31BN", "Vibe B A2016b31BO", "Vibe B A2016b31BP", "Vibe B A2016b31BQ", "Vibe B A2016b31BR", "Vibe B A2016b31BS"],
    
    "sony": ["Xperia 5 III", "Xperia 10 II", "Xperia 1 II", "Xperia 10 Plus", "Xperia 1", "Xperia XZ3", "Xperia 1 III", "Xperia 1 II", "Xperia 1", "Xperia 5 III", "Xperia 5 II", "Xperia 5", "Xperia 10 III", "Xperia 10 II", "Xperia 10", "Xperia Pro", "Xperia L4", "Xperia L3", "Xperia XZ3", "Xperia XZ2 Premium", "Xperia XZ2", "Xperia XZ1 Compact", "Xperia XZ1", "Xperia XZ Premium", "Xperia XZ", "Xperia XA2 Ultra", "Xperia XA2", "Xperia XA1 Ultra", "Xperia XA1 Plus", "Xperia XA1", "Xperia X Compact","C6603", "D6503", "F5121", "F8331", "G3116", "H3113", "J9210", "XQ-AS52", "XQ-AD52", "XQ-BT52", "XQ-BS52", "XQ-AT51", "XQ-AT52", "XQ-AD52", "XQ-AT52", "XQ-AT42", "XQ-AT41", "XQ-AD51", "XQ-BT51", "XQ-BS41", "XQ-BS52", "XQ-BT52", "XQ-AD51", "XQ-BT51", "XQ-BS41", "XQ-AT41", "XQ-BS52", "XQ-BT52", "XQ-AS42", "XQ-BS42", "XQ-AT42", "XQ-BS41", "XQ-AT51", "XQ-AD51", "XQ-AD42", "XQ-AS41", "XQ-BT41", "XQ-BT51", "XQ-BS51", "XQ-BS42", "XQ-AS52", "XQ-AS41", "XQ-BS42", "XQ-BT41", "XQ-AS42", "XQ-AT42", "XQ-AD42", "XQ-BS41", "XQ-AT41", "XQ-BS51", "XQ-BT51", "XQ-AT51", "XQ-AD51", "F8131", "F8132", "G3121", "G3112", "G3123", "G3125", "G8141", "G8142", "G8341", "G8342", "H8216", "H8266", "H8296", "H8416", "H9436", "H9461", "H9436", "H9461", "H9436", "H9493", "H8541", "H8526", "H8116", "H8166", "I4213", "I4293", "I4293", "I4312", "I4332", "I4332", "I4113", "I4193", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213"],
    
    "htc": ["Wildfire E3", "Desire 21 Pro", "U20 5G", "Desire 20 Pro", "Desire 19+", "U12 Life","HTC U20", "HTC U12+", "HTC U11", "HTC U12+", "HTC U12 Life", "HTC U11+", "HTC U11 Life", "HTC U11", "HTC U Ultra", "HTC 10", "HTC One M9", "HTC One M8", "HTC One (M7)", "HTC Desire 820", "HTC Desire 816", "HTC Desire 610", "HTC Desire 510", "HTC Butterfly S", "HTC One Max", "HTC One Mini", "HTC Desire 600", "HTC First", "HTC One X+","HTC One M8", "HTC One M9", "HTC 10", "HTC U11", "HTC U12+", "HTC U Ultra", "HTC U Play", "HTC Desire 626", "HTC Desire 816", "HTC Desire 610", "HTC Desire 510", "HTC Desire 820", "HTC Desire 626G+", "HTC One X", "HTC One X+", "HTC One S", "HTC One V", "HTC One Mini", "HTC One Mini 2", "HTC One Max", "HTC One E8", "HTC One E9", "HTC One A9", "HTC One E9+", "HTC One M8s", "HTC Desire Eye", "HTC Desire 820s", "HTC Desire 816G", "HTC Desire 626s", "HTC Desire 530", "HTC Desire 828", "HTC 10 Lifestyle", "HTC U11 Life", "HTC U11 Eyes", "HTC U11+"],
    
    "apple": ["iPhone 13 Pro", "iPhone 13", "iPhone 13 mini", "iPhone 12 Pro", "iPhone 12", "iPhone SE (3rd Gen)", "iPhone 13 Pro Max", "iPhone 13 Pro", "iPhone 13", "iPhone 13 mini", "iPhone 12 Pro Max", "iPhone 12 Pro", "iPhone 12", "iPhone 12 mini", "iPhone SE (2nd generation)", "iPhone 11 Pro Max", "iPhone 11 Pro", "iPhone 11", "iPhone XR", "iPhone XS Max", "iPhone XS", "iPhone X", "iPhone 8 Plus", "iPhone 8", "iPhone 7 Plus", "iPhone 7", "iPhone SE (1st generation)", "iPhone 6s Plus", "iPhone 6s", "iPhone 6 Plus", "iPhone 6", "iPhone 5s", "iPhone 5c", "iPhone 5", "iPhone 4s", "iPhone 4", "iPhone 3GS", "iPhone 3G", "iPhone","A1549", "A1522", "A1586", "A1633", "A1688", "A1699", "A1700", "A1660", "A1778", "A1661", "A1784", "A1863", "A1901", "A1865", "A1902", "A1920", "A1921", "A2101", "A2102", "A2104", "A1984", "A2103", "A1920", "A1921", "A2160", "A2161", "A2215", "A2217", "A2218", "A2220", "A2221", "A2223", "A2111", "A2229", "A2112", "A2131", "A2106", "A2107", "A2108", "A2162", "A2047", "A2048", "A2049", "A2105", "A2014", "A2015", "A2016", "A1867", "A1868", "A1897", "A1898", "A1899", "A1900", "A1903", "A1923", "A2212", "A2200", "A2202", "A2201", "A2301", "A2223", "A2215", "A1866", "A1993", "A1990", "A2013", "A2012", "A1983", "A1954", "A1953", "A2100", "A2005", "A2114", "A2116", "A2110", "A1920", "A1921", "A1985", "A2115", "A2117", "A2118", "A2003", "A2004", "A2160", "A2161", "A2202", "A2298", "A2299", "A2162", "A2270", "A2271", "A2229", "A2272", "A2273", "A2301", "A2304", "A2324", "A2325", "A2340", "A2341", "A2342", "A2375", "A2376", "A2377", "A2378", "A2406", "A2407", "A2408", "A2451", "A2452", "A2453", "A2600", "A2594", "A2503", "A2571", "A2570", "A2410", "A2402", "A2412", "A2399", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602"],
    
    "oppo": ["Reno 7 Pro", "Reno 7", "Reno 6 Pro+", "A95", "A96", "A93", "Oppo Find X3 Pro", "Oppo Find X2 Pro", "Oppo Find X2", "Oppo Reno 6 Pro+", "Oppo Reno 6 Pro", "Oppo Reno 6", "Oppo Reno 5 Pro+", "Oppo Reno 5 Pro", "Oppo Reno 5", "Oppo A94", "Oppo A74", "Oppo F19 Pro+", "Oppo F19 Pro", "Oppo F19", "Oppo A93", "Oppo A53", "Oppo A33", "Oppo A32", "Oppo A72", "Oppo A52", "Oppo A92", "Oppo A12", "Oppo Reno 3 Pro", "Oppo Reno 3", "Oppo Reno 2", "Oppo Reno", "Oppo K7x", "Oppo K7", "Oppo A9 (2020)", "Oppo A5 (2020)", "CPH1903", "CPH1803", "CPH1859", "CPH1969", "CPH1989", "CPH1919", "CPH1941", "CPH1983", "CPH1963", "CPH1879", "CPH1831", "CPH2035", "CPH2069", "CPH1987", "CPH2071", "CPH2083", "CPH2015", "CPH2019", "CPH2173", "CPH2089", "CPH2067", "CPH2017", "CPH2087", "CPH2205", "CPH2251", "CPH2197", "CPH2235", "CPH2347", "CPH2295", "CPH2249", "CPH2243", "CPH2349", "CPH2359", "CPH2383", "CPH2381", "CPH2239", "CPH2213", "CPH2129", "CPH2195", "CPH2227", "CPH2316", "CPH2353", "CPH2261", "CPH2225", "CPH2269", "CPH2073", "CPH2185", "CPH1877", "CPH2013", "CPH2061", "CPH1955", "CPH1871", "CPH1801", "CPH1873", "CPH1901", "CPH1809", "CPH1853", "CPH1923", "CPH1981", "CPH1833", "CPH1917", "CPH1967", "CPH1937", "CPH1893", "CPH1931", "CPH1921", "CPH1823", "CPH2023", "CPH2021", "CPH2103", "CPH2220", "CPH2127", "CPH2059", "CPH2139", "CPH2253", "CPH2267", "CPH2263", "CPH2247", "CPH2241", "CPH2297", "CPH2357", "CPH2255", "CPH2345", "CPH2329", "CPH2209", "CPH2191", "CPH2199", "CPH2289", "CPH2319", "CPH2343", "CPH2363", "CPH2161", "CPH2163", "CPH1979", "CPH1977", "CPH1973", "CPH1965", "CPH1959", "CPH1951", "CPH1913", "CPH1909", "CPH1905", "CPH1861", "CPH1863", "CPH1967", "CPH1933", "CPH1937", "CPH1921", "CPH1923", "CPH1987", "CPH1919", "CPH1897", "CPH1875", "CPH1874", "CPH1872", "CPH1865", "CPH1863", "CPH1862", "CPH1853", "CPH1852", "CPH1851", "CPH1843", "CPH1841", "CPH1835", "CPH1833", "CPH1832", "CPH1831", "CPH1825", "CPH1823", "CPH1821", "CPH1819", "CPH1813", "CPH1812", "CPH1811", "CPH1809", "CPH1808", "CPH1807", "CPH1805", "CPH1803", "CPH1801"],
    
    "realme": ["Realme GT Master Edition", "Realme 8i", "Realme 8s", "Narzo 30", "Narzo 20", "Realme 7i", "Realme 8", "Realme 7 Pro", "Realme X50 Pro","Realme GT Master Explorer Edition", "Realme GT Master Edition", "Realme GT", "Realme 8 Pro", "Realme 8", "Realme Narzo 30 Pro", "Realme Narzo 30A", "Realme X7 Pro", "Realme X7", "Realme 7 Pro", "Realme 7", "Realme C21", "Realme C20", "Realme C15", "Realme C12", "Realme C11", "Realme 6 Pro", "Realme 6", "Realme X2 Pro", "Realme XT", "Realme 5 Pro", "Realme 5", "Realme 3 Pro", "Realme 3", "Realme 2 Pro", "Realme 2", "Realme 1","RMX2111", "RMX3092", "RMX3161", "RMX3142", "RMX3185", "RMX3186", "RMX3281", "RMX3274", "RMX3361", "RMX3165", "RMX3243", "RMX3242", "RMX3294", "RMX3162", "RMX3241", "RMX3290", "RMX3289", "RMX3270", "RMX3267", "RMX3266", "RMX3263", "RMX3260", "RMX3240", "RMX3280", "RMX3276", "RMX3244", "RMX3121", "RMX3063", "RMX3061", "RMX3090", "RMX3091", "RMX3080", "RMX3211", "RMX3334", "RMX3221", "RMX3295", "RMX3292", "RMX3331", "RMX3383", "RMX3350", "RMX3332", "RMX3300", "RMX3310", "RMX3311", "RMX3385", "RMX3336", "RMX3337", "RMX3338", "RMX3235", "RMX3225", "RMX3124", "RMX3065", "RMX3143", "RMX3201", "RMX3070", "RMX3250", "RMX3246", "RMX3261", "RMX3071", "RMX3150", "RMX3164", "RMX3141", "RMX3063", "RMX3060", "RMX3357", "RMX3223", "RMX3330", "RMX3284", "RMX3362", "RMX3236", "RMX3193", "RMX3191", "RMX3358", "RMX3384", "RMX3262", "RMX3248", "RMX3339", "RMX3283", "RMX3195", "RMX3093", "RMX3098", "RMX3245", "RMX3095", "RMX3064", "RMX3341", "RMX3340", "RMX3365", "RMX3363", "RMX3364", "RMX3366", "RMX3367", "RMX3368", "RMX3369", "RMX3370", "RMX3371", "RMX3372", "RMX3373", "RMX3374", "RMX3375", "RMX3376", "RMX3377", "RMX3378", "RMX3379", "RMX3380", "RMX3381", "RMX3382", "RMX3312", "RMX3249", "RMX3094", "RMX3116", "RMX3187", "RMX3096", "RMX3097", "RMX3171", "RMX3152", "RMX3115", "RMX3081", "RMX3272", "RMX3273", "RMX3264", "RMX3265", "RMX3269", "RMX3268", "RMX3082", "RMX3083", "RMX3084", "RMX3085", "RMX3086", "RMX3087", "RMX3088", "RMX3089", "RMX3099", "RMX309A", "RMX309B", "RMX309C", "RMX309D", "RMX309E", "RMX309F", "RMX309G", "RMX309H", "RMX309I", "RMX309J", "RMX309K", "RMX309L", "RMX309M", "RMX309N", "RMX309O", "RMX309P", "RMX309Q", "RMX309R", "RMX309S", "RMX309T", "RMX309U", "RMX309V", "RMX309W", "RMX309X", "RMX309Y", "RMX309Z", "RMX31ZM", "RMX31ZN", "RMX31ZS", "RMX31ZT", "RMX31ZW", "RMX31ZV", "RMX31ZR", "RMX31ZQ", "RMX31ZP", "RMX31ZO", "RMX31ZN", "RMX31ZM", "RMX31ZL", "RMX31ZK", "RMX31ZJ", "RMX31ZI", "RMX31ZH", "RMX31ZG", "RMX31ZF", "RMX31ZE", "RMX31ZD", "RMX31ZC"],
    
    "motorola": ["Moto G100", "Moto G60", "Moto G40 Fusion", "Moto G30", "Moto G9 Power", "Moto G8", "Moto G Power 2022", "Moto G7", "Moto G Stylus 2022", "Motorola Edge 20 Pro", "Motorola Edge 20", "Motorola Edge 20 Lite", "Motorola Moto G Stylus (2021)", "Motorola Moto G Power (2021)", "Motorola Moto G Play (2021)", "Motorola Moto G9 Plus", "Motorola Moto G9", "Motorola Moto G8 Plus", "Motorola Moto G8 Power", "Motorola Moto G8", "Motorola Moto G7 Plus", "Motorola Moto G7 Power", "Motorola Moto G7 Play", "Motorola Moto G7", "Motorola Moto G6 Plus", "Motorola Moto G6", "Motorola Moto G5S Plus", "Motorola Moto G5 Plus", "Motorola Moto G5", "Motorola Moto G4 Plus", "Motorola Moto G4", "Motorola Moto X4", "Motorola Moto X (2nd Gen)", "Motorola Moto X", "Motorola Moto Z3 Play", "Motorola Moto Z2 Play", "Motorola Moto Z", "Motorola Moto E7 Plus", "Motorola Moto E6 Plus", "Motorola Moto E5 Plus", "Motorola Moto E4 Plus", "Motorola Moto E (2nd Gen)", "Motorola Moto E", "XT2127-2", "XT2127-4", "XT2127-5", "XT2127-6", "XT2127-7", "XT2127-8", "XT2127-10", "XT2127-11", "XT2127-12", "XT2127-13", "XT2127-14", "XT2127-15", "XT2127-16", "XT2127-17", "XT2127-18", "XT2127-19", "XT2127-20", "XT2127-21", "XT2127-22", "XT2127-23", "XT2127-24", "XT2127-25", "XT2127-26", "XT2127-27", "XT2127-28", "XT2127-29", "XT2127-30", "XT2127-31", "XT2127-32", "XT2127-33", "XT2127-34", "XT2127-35", "XT2127-36", "XT2127-37", "XT2127-38", "XT2127-39", "XT2127-40", "XT2127-41", "XT2127-42", "XT2127-43", "XT2127-44", "XT2127-45", "XT2127-46", "XT2127-47", "XT2127-48", "XT2127-49", "XT2127-50", "XT2127-51", "XT2127-52", "XT2127-53", "XT2127-54", "XT2127-55", "XT2127-56", "XT2127-57", "XT2127-58", "XT2127-59", "XT2127-60", "XT2127-61", "XT2127-62", "XT2127-63", "XT2127-64", "XT2127-65", "XT2127-66", "XT2127-67", "XT2127-68", "XT2127-69", "XT2127-70", "XT2127-71", "XT2127-72", "XT2127-73", "XT2127-74", "XT2127-75", "XT2127-76", "XT2127-77", "XT2127-78", "XT2127-79", "XT2127-80", "XT2127-81", "XT2127-82", "XT2127-83", "XT2127-84", "XT2127-85", "XT2127-86", "XT2127-87", "XT2127-88", "XT2127-89", "XT2127-90", "XT2127-91", "XT2127-92", "XT2127-93", "XT2127-94", "XT2127-95", "XT2127-96", "XT2127-97", "XT2127-98", "XT2127-99", "XT2127-100", "XT2127-101", "XT2127-102", "XT2127-103", "XT2127-104", "XT2127-105", "XT2127-106", "XT2127-107", "XT2127-108", "XT2127-109", "XT2127-110", "XT2127-111", "XT2127-112", "XT2127-113", "XT2127-114", "XT2127-115", "XT2127-116", "XT2127-117", "XT2127-118", "XT2127-119", "XT2127-120", "XT2127-121", "XT2127-122", "XT2127-123", "XT2127-124", "XT2127-125", "XT2127-126", "XT2127-127", "XT2127-128", "XT2127-129", "XT2127-130", "XT2127-131", "XT2127-132", "XT2127-133", "XT2127-134", "XT2127-135", "XT2127-136", "XT2127-137", "XT2127-138", "XT2127-139", "XT2127-140", "XT2127-141", "XT2127-142", "XT2127-143", "XT2127-144", "XT2127-145", "XT2127-146", "XT2127-147", "XT2127-148", "XT2127-149", "XT2127-150", "XT2127-151", "XT2127-152", "XT2127-153"],
    
    "nokia": ["Nokia X20", "Nokia X10", "Nokia G20", "Nokia G10", "Nokia 8.3 5G", "Nokia 5.4", "Nokia 3.4", "Nokia 2.4", "Nokia 8.1", "Nokia 7.2", "Nokia 6.2", "Nokia 4.2", "Nokia 3.2", "Nokia 2.2", "Nokia 9 PureView", "Nokia 8 Sirocco", "Nokia 8", "Nokia 7 Plus", "Nokia 7.1", "Nokia 6.1 Plus", "Nokia 6.1", "Nokia 5.1 Plus", "Nokia 5.1", "Nokia 4.1", "Nokia 3.1 Plus", "Nokia 3.1", "Nokia 2.1", "Nokia 1", "TA-1337", "TA-1380", "TA-1395", "TA-1208", "TA-1208", "TA-1334", "TA-1336", "TA-1230", "TA-1239", "TA-1283", "TA-1335", "TA-1234", "TA-1347", "TA-1353", "TA-1340", "TA-1233", "TA-1338", "TA-1386", "TA-1307", "TA-1296", "TA-1281", "TA-1333", "TA-1244", "TA-1235", "TA-1357", "TA-1236", "TA-1339", "TA-1316", "TA-1329", "TA-1343", "TA-1354", "TA-1300", "TA-1303", "TA-1289", "TA-1315", "TA-1287", "TA-1342", "TA-1351", "TA-1331", "TA-1325", "TA-1295", "TA-1240", "TA-1286", "TA-1328", "TA-1284", "TA-1293", "TA-1341", "TA-1292", "TA-1327", "TA-1298", "TA-1323", "TA-1238", "TA-1291", "TA-1345", "TA-1309", "TA-1344", "TA-1324", "TA-1346", "TA-1326", "TA-1304", "TA-1320", "TA-1348", "TA-1318", "TA-1330", "TA-1280", "TA-1246", "TA-1248", "TA-1317", "TA-1299", "TA-1310", "TA-1350", "TA-1332", "TA-1242", "TA-1206", "TA-1294", "TA-1313", "TA-1249", "TA-1241", "TA-1216", "TA-1297", "TA-1285", "TA-1319", "TA-1243", "TA-1356"],
    
    "xiaomi": ["Mi 11", "Mi 10 Pro", "Mi 9T","M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2012K11C","Redmi 6A","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4","Redmi Note 5", "Redmi 4X","Redmi Note 8","Redmi Note 8 Pro","Xiaomi Mi 11 Ultra", "Xiaomi Mi 11 Pro", "Xiaomi Mi 11", "Xiaomi Mi 10 Ultra", "Xiaomi Mi 10 Pro", "Xiaomi Mi 10", "Xiaomi Mi 10T Pro", "Xiaomi Mi 10T", "Xiaomi Mi 9T Pro", "Xiaomi Mi 9T", "Xiaomi Mi 9 Pro 5G", "Xiaomi Mi 9", "Xiaomi Mi 8 Pro", "Xiaomi Mi 8", "Xiaomi Mi 8 Lite", "Xiaomi Mi 8 SE", "Xiaomi Mi Mix 3", "Xiaomi Mi Mix 2S", "Xiaomi Mi Mix 2", "Xiaomi Mi Mix", "Xiaomi Redmi Note 11 Pro+", "Xiaomi Redmi Note 11 Pro", "Xiaomi Redmi Note 11", "Xiaomi Redmi Note 10 Pro", "Xiaomi Redmi Note 10", "Xiaomi Redmi Note 9 Pro", "Xiaomi Redmi Note 9", "Xiaomi Redmi Note 8 Pro", "Xiaomi Redmi Note 8", "Xiaomi Redmi Note 7 Pro", "Xiaomi Redmi Note 7", "Xiaomi Redmi K40 Pro", "Xiaomi Redmi K40", "Xiaomi Redmi K30 Pro", "Xiaomi Redmi K30", "Xiaomi Redmi K20 Pro", "Xiaomi Redmi K20", "Xiaomi Poco X3 Pro", "Xiaomi Poco X3", "Xiaomi Poco X2", "Xiaomi Poco F3", "Xiaomi Poco F2 Pro", "Xiaomi Poco F1"],
    
    "samsung": ["Galaxy S21", "Galaxy A52", "Galaxy S20","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935F","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820","SPH-L720","SM-S906E", "Samsung Galaxy S21 Ultra", "Samsung Galaxy S21+", "Samsung Galaxy S21", "Samsung Galaxy Note 20 Ultra", "Samsung Galaxy Note 20", "Samsung Galaxy S20 Ultra", "Samsung Galaxy S20+", "Samsung Galaxy S20", "Samsung Galaxy Note 10+", "Samsung Galaxy Note 10", "Samsung Galaxy S10+", "Samsung Galaxy S10", "Samsung Galaxy Note 9", "Samsung Galaxy S9+", "Samsung Galaxy S9", "Samsung Galaxy Note 8", "Samsung Galaxy S8+", "Samsung Galaxy S8", "Samsung Galaxy Note 7", "Samsung Galaxy S7 Edge", "Samsung Galaxy S7", "Samsung Galaxy Note 5", "Samsung Galaxy S6 Edge+", "Samsung Galaxy S6 Edge", "Samsung Galaxy S6", "Samsung Galaxy Note 4", "Samsung Galaxy S5", "Samsung Galaxy S4", "Samsung Galaxy S3", "Samsung Galaxy Note 3", "SM-G991", "SM-G981", "SM-G973", "SM-G960", "SM-G950", "SM-G930", "SM-G920", "SM-G900", "GT-I9500", "GT-I9300", "GT-I9100", "GT-I9000", "SM-N981", "SM-N970", "SM-N960", "SM-N950", "SM-N920", "SM-N910", "SM-N900", "GT-N7100", "GT-N7000", "SM-G991", "SM-G981", "SM-G973", "SM-G960", "SM-G950", "SM-G930", "SM-G920", "SM-G900", "GT-I9500", "GT-I9300", "GT-I9100", "GT-I9000", "SM-N981", "SM-N970", "SM-N960", "SM-N950", "SM-N920", "SM-N910", "SM-N900", "GT-N7100", "GT-N7000", "SM-A526B", "SM-A516B", "SM-A516N", "SM-A526U", "SM-A716U", "SM-A716V", "SM-A5260", "SM-A526W", "SM-A126U", "SM-A126V", "SM-A016G", "SM-A016B", "SM-A016M", "SM-A025M", "SM-A025F", "SM-A217F", "SM-A217M", "SM-A207F", "SM-A207M", "SM-A102U", "SM-A102U1", "SM-A102W", "SM-A102N", "SM-A1020", "SM-A105F", "SM-A105G", "SM-A105M", "SM-A202F", "SM-A202G", "SM-A202M", "SM-A125U", "SM-A125V", "SM-A022G", "SM-A022M", "SM-A027G", "SM-A027M", "SM-A2170", "SM-A115M", "SM-A107M", "SM-A107F", "SM-A107M", "SM-A0220", "SM-A115F", "SM-A102F", "SM-A1050"],
    
    "vivo": ["Vivo_X60_Pro", "Vivo_X50_Pro", "Vivo_X30_Pro", "Vivo_X27", "Vivo_X23", "Vivo_X21", "Vivo_V21", "Vivo_V17", "Vivo_V15", "Vivo_V11", "Vivo_V9", "Vivo_Y95", "Vivo_Y91", "Vivo_Y81", "Vivo_Y71", "Vivo_S1", "V2056", "V2112A", "V2112", "V2122A", "V2120A", "V2120", "V2116A", "V2114A", "V2112A", "V2010A", "V2019A", "V2010", "V2003A", "V2002A", "V2002", "V1932A", "V1932T", "V1932", "V1929A", "V1928A", "V1928T", "V1928", "V1927A", "V1926A", "V1925A", "V1925", "V1924A", "V1922A", "V1921A", "V1921", "V1920A", "V1919A", "V1916A", "V1916", "V1912A", "V1911A", "V1910A", "V1910", "V1909A", "V1907A", "V1905", "V1903A", "V1901A", "V1901T", "V1901", "V1836", "V1824A", "V1824T", "V1824", "V1818A", "V1818T", "V1813A", "V1813T", "V1813", "V1812A", "V1811A", "V1811T", "V1811", "V1808A", "V1808T", "V1808", "V1801A", "V1801T", "V1801", "V1730T", "V1730F", "V1730A", "V1730", "V1724A", "V1723A", "V1723", "V1721A", "V1720A", "V1720T", "V1720", "V1716A", "V1715A", "V1715", "V1713A", "V1713", "V1712A", "V1712", "V1711T", "V1711A", "V1711", "V1709A", "V1709T", "V1709", "V1708A", "V1708T", "V1707A", "V1707T", "V1706T", "V1706", "V1703A", "V1701A", "V1701", "V1624A", "V1623A", "V1622A", "V1622", "V1621A", "V1619", "V1618A", "V1617A", "V1616", "V1615T", "V1614T", "V1613", "V1611T", "V1611", "V1608A", "V1609", "V1605", "V1604", "V1603", "V1601", "V1570", "V1562", "V1561", "V1550", "V1548", "V1546", "V1543", "V1542", "V1540", "V1530", "V1520", "V1510", "V1500", "V1420", "V1400", "V1310", "V1320"],
    
    "zte": ["ZTE_Axon_10_Pro", "ZTE_Axon_9", "ZTE_Axon_7", "ZTE_Axon_7_Mini", "ZTE_Blade_20", "ZTE_Blade_10", "ZTE_Blade_V10", "ZTE_Blade_V9", "ZTE_Blade_X", "ZTE_Blade_A7", "ZTE_Nubia_Red_Magic", "ZTE_Nubia_Z20", "ZTE_Nubia_X", "ZTE_Nubia_Z18", "ZTE_Nubia_Z17","Axon_10_Pro", "Axon_9", "Axon_7", "Axon_7_Mini", "Blade_20", "Blade_10", "Blade_V10", "Blade_V9", "Blade_X", "Blade_A7", "Nubia_Red_Magic", "Nubia_Z20", "Nubia_X", "Nubia_Z18", "Nubia_Z17"],
    
    "lg": ["LG_G8", "LG_V50", "LG_V40", "LG_G7", "LG_V30", "LG_G6", "LG_V20", "LG_G5", "LG_V10", "LG_G4", "LG_G3", "LG_G2", "LG_G_Flex"],
    
    "huawei": ["Huawei_P40", "Huawei_P30", "Huawei_P20", "Huawei_Mate_30", "Huawei_Mate_20", "Huawei_Mate_10", "Huawei_Nova_5", "Huawei_Nova_4", "Huawei_Nova_3", "Huawei_P10", "Huawei_P9", "Huawei_Honor_9", "Huawei_Honor_8", "Huawei_Y9", "Huawei_Y8"],
    
    "oneplus": ["OnePlus_9_Pro", "OnePlus_9", "OnePlus_8T", "OnePlus_8_Pro", "OnePlus_8", "OnePlus_7T_Pro", "OnePlus_7T", "OnePlus_7_Pro", "OnePlus_7", "OnePlus_6T", "OnePlus_6", "OnePlus_5T", "OnePlus_5", "OnePlus_3T", "OnePlus_3"]}




    fbcr = random.choice(fbcr_values)
    
    fbmf = random.choice(list(fbmf_fbdv_dict.keys()))
    fbdv = random.choice(fbmf_fbdv_dict[fbmf])
    
    color = random.choice(['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m','\033[97m'])

    user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(0,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/en_US;FBRV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBCR/"+fbcr+";FBMF/"+fbmf+";FBBD/"+fbmf+";FBPN/com.facebook.katana;FBDV/"+fbdv+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:]"
    return user_agent


    



import random
import string

def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))

    # Randomly vary the Android OS version, device, and app version for realism
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))  # Updated range for FBAV versions
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])

    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    
    return ua_bgraph

ua_bgraph = generate_user_agent()


import requests
import random
import concurrent.futures as thread
import os
import string

# Random FB version generation
fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))

# User agent string
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        
        if uid in existing_uids:
            print(f"     {yellow}[INFO] {red}ACCOUNT --> {white}{uid} {red}already exists.")
            print("\033[1;31m───────────────────────────────────────────────────────────────\033[0m")
            return

        response = requests.post(url, data=data).json()
        
        print(response)
        if 'access_token' in response:
            token = response['access_token']

            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")

            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: Extracted Account ─────> {uid}.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            success_count.append(uid)
        else:
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT Account ─────> {uid}.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except Exception as e:
        print(f"     \033[1;31m[ERROR]\033[0m Error extracting account: {uid}. Reason: {str(e)}\033[0m\n")


def proz(accounts_file, token_output_path, extract_type):
    """Process the accounts and extract tokens concurrently."""
    success_count = []

    # Load existing uids from the output file to avoid duplicates
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
        return


def axl1():
    clear_screen()
    jovan()
    folder_path = "/sdcard/boostphere"
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    token_output_path = account_file

    proz(file_path, token_output_path, extract_type)


import requests
import random
import concurrent.futures as thread
import os
import string

fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def load_existing_tokens(path_file):
    """Load existing accounts or pages from the output file."""
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}  # Set of existing uids or page ids
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token
    
    if uid in existing_tokens:
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
        return

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        response = requests.post(url, data=data).json()
        
        if 'access_token' in response:
            token = response['access_token']

            # Extract Facebook Pages associated with the account token
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}Page ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")

            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")

    except Exception as e:
        print(f"[ERROR] Error extracting account: {uid}. Reason: {str(e)}")

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    pages_data = []
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f'Error: {response.text}')
            return None
        
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        
        url = data.get('paging', {}).get('next')  # Update the URL for the next request

    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")

def axl2():
    clear_screen()
    jovan()
    folder_path = "/sdcard/boostphere"  
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    prozc(file_path, account_file, extract_type)

def remove_duplicates():
    clear_screen()
    jovan()
    file_paths = {
        "1": "/sdcard/boostphere/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/FRAPAGES.txt",
        "3": "/sdcard/boostphere/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/RPWPAGES.txt"
    }
    
    print(f"     {red}Choose which file to remove duplicates from:")
    print(f"     {yellow}[1]  {blue}FRA ACCOUNT")
    print(f"     {yellow}[2]  {blue}FRA PAGES")
    print(f"     {yellow}[3]  {blue}RPW ACCOUNT")
    print(f"     {yellow}[4]  {blue}RPW PAGES")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {white}Enter your choice: ").strip()
    
    if choice not in file_paths:
        print("Invalid choice. Please try again.")
        return
    
    file_path = file_paths[choice]
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        seen_uids = set()  # To store unique uids
        unique_lines = []

        for line in lines:
            # Split the line into 'uid' and 'password'
            if '|' in line:
                uid, password = line.split('|', 1)  # Split only at the first '|'
                if uid not in seen_uids:
                    unique_lines.append(line)  # Keep the line if 'uid' is unique
                    seen_uids.add(uid)  # Add the 'uid' to the set
        
        # Write the unique lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(unique_lines)
        
        print(f"     {green}Successfully removed duplicates from: {file_path}")
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


# Call the function to start the process


# REACT  
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction_vid(token, uid_url, reaction_type, reactions_count):
    """
    Send a reaction using the provided access token.
    
    Parameters:
    - token: User's token (in the format email|access_token)
    - uid_url: The post ID or URL for the reaction
    - reaction_type: Type of reaction (LIKE, LOVE, etc.)
    - reactions_count: The number of reactions performed so far
    
    Returns:
    - access_token: The access token used for the request
    - status_code: HTTP status code returned by the request
    - response_text: Response content from Facebook
    """
    access_token = token.split('|')[1]  # Extract the access token (assuming the format is email|access_token)
    auto_react_url = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    
    try:
        # Send POST request to Facebook's API to add the reaction
        response = requests.post(auto_react_url)
        return access_token, response.status_code, response.text  # Return results for further processing
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request (e.g., network issues)
        return access_token, None, str(e)

def clear_text_files():
    """
    Clear the contents of specified text files based on user choice.
    """
    clear_screen()  # Assuming clear_screen is defined elsewhere
    jovan()         # Assuming jovan is defined elsewhere

    # Dictionary of file paths for resetting
    file_paths = {
        "1": "/sdcard/boostphere/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/FRAPAGES.txt",
        "3": "/sdcard/boostphere/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/RPWPAGES.txt"
    }

    print(f"     {blue}Choose File To Reset:")
    print(f"     {yellow}[01]  {blue}FRA ACCOUNT")
    print(f"     {yellow}[02]  {blue}FRA PAGES")
    print(f"     {yellow}[03]  {blue}RPW ACCOUNT")
    print(f"     {yellow}[04]  {blue}RPW PAGES")
    print(f"     {yellow}[05]  {blue}All files")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    user_choice = input(f"    {red}Enter your choice: ").strip()

    # Clear all files if option 5 is selected
    if user_choice == '5':
        for file_path in file_paths.values():
            try:
                with open(file_path, 'w') as file:
                    file.truncate(0)  # Clear the file content
                print(f"Successfully cleared: {file_path}")
            except Exception as e:
                print(f"Error clearing {file_path}: {str(e)}")
        return

    # Handle clearing a single file based on the user's choice
    selected_file = file_paths.get(user_choice)
    if selected_file:
        try:
            with open(selected_file, 'w') as file:
                file.truncate(0)  # Clear the file content
            print(f"Successfully cleared: {selected_file}")
        except Exception as e:
            print(f"Error clearing {selected_file}: {str(e)}")
    else:
        print("Invalid choice. Please enter a valid number.")

def perform_reaction_fast_vid():
    """
    Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions.
    """
    # Define available file paths
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()  # Assuming clear_screen is defined elsewhere
    jovan()         # Assuming jovan is defined elsewhere

    # Display options to the user
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[01] {green}FRA ACCOUNT 
     {blue}[02] {green}FRA PAGES
     {blue}[03] {green}RPW ACCOUNT
     {blue}[04] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  

    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Load tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Filter out empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)
    
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    # Prompt for starting line
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Slice the tokens based on starting line
    tokens = tokens[start_line - 1:]

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/videos/539673715119122/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    post_link = input(f"   {green}Enter the post link or ID: ")
    uid_url = extract_facebook_video_id(post_link)  # Assuming Video_Extractid is defined elsewhere

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Get number of reactions
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
    except ValueError:
        print(f"Please enter a valid number for reactions.")
        return

    # Check if requested reactions exceed available tokens
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT exceeding {len(tokens)}")
        return

    reactions_count = 0
    max_workers = 15  # Set maximum number of threads

    while reactions_count < num_reactions and tokens:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit reactions for the current available tokens
            future_to_token = {executor.submit(perform_reaction_vid, token, uid_url, reaction_type): token for token in tokens}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"   {green}[SUCCESS] SUCCESSFULLY REACTED TO {white}───────> {red}{uid_url}")
                        # Check if we've reached the success limit
                        if reactions_count >= num_reactions:
                            break  # Exit the loop if the desired number of successful reactions is reached
                    else:
                        print(f"   {green}[FAILED] FAILED TO SEND REACTION  {white}───────> {red}{uid_url}")
                except Exception as e:
                    print(f"Error processing token {token}: {str(e)}")

        # Remove the tokens that were attempted in this round
        tokens = tokens[len(future_to_token):]  # Use tokens for the next round if needed

    print(f"Reactions complete! {reactions_count} reactions were successfully sent.")
    print(f"Total reactions sent: {reactions_count} out of {num_reactions}")


# Run the reaction function (this would be called in your program)





import requests

def fetch_account_info(file_options):
    clear_screen()
    jovan()
    print(f"     {yellow}CHOOSE WHICH FILE YOU WANT TO CHECK:")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    for key, value in file_options.items():
        print(f"     {red}[{key}] {yellow}{value.split('/')[-1]}")  # Display only the filename
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    file_choice = int(input(f"  {red}Choose: "))
    accounts_file = file_options.get(file_choice)

    if accounts_file is None:
        print("Invalid choice. Exiting.")
        return

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        for account in accounts:
            uid, token = account.strip().split('|')

            # Fetching account info using the token
            account_info = get_account_info(token)
            if account_info:
                account_name = account_info.get('name', 'No name available')
                print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
                print(f"     {yellow}ACCOUNT NAME {red}: {green}{account_name}")

                # Optionally, you can also fetch pages associated with the account
                pages = extract_fb_pages(token)
                if pages:
                    print()
                    print(f"          {yellow}PAGES ASSOCIATED WITH {white}: {red}{account_name}")
                    for page in pages:
                        print()
                        print(f"       👉 {yellow}{page['name']} {white}= {green}PAGE ID: {red}{page['id']}")
                        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
                else:
                    print(f"     {red}NO PAGES ASSOCIATED WITH THIS ACCOUNT ! .")
            else:
                print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
                print(f"     {yellow}FAILED TO FETCH ACCOUNT INFORMATION ! {white}= {red}{uid}")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
    except Exception as e:
        print(f"[ERROR] {str(e)}")

def get_account_info(token):
    url = 'https://graph.facebook.com/v18.0/me'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  # Return account info as JSON
        else:
            pass
            return None
    except Exception as e:
        print(f"[ERROR] Error fetching account info: {str(e)}")
        return None

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    pages_data = []
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for page in data.get('data', []):
                pages_data.append({
                    'id': page.get('id'),
                    'name': page.get('name'),
                    'accessToken': page.get('access_token')
                })
            return pages_data
        else:
            print(f"Failed to fetch pages: {response.text}")
            return None
    except Exception as e:
        print(f"[ERROR] Error fetching pages: {str(e)}")
        return None

# File options mapping
file_options = {
    1: "/sdcard/boostphere/FRAACCOUNT.txt",
    2: "/sdcard/boostphere/FRAPAGES.txt",
    3: "/sdcard/boostphere/RPWACCOUNT.txt",
    4: "/sdcard/boostphere/RPWPAGES.txt"
}

# Run the account info fetch


import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()  # Use the randomly selected user agent
    }
    
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions

def perform_reaction_fast():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the selected line
    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = extract_ids(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    max_workers = 15  # Set a limit for the number of concurrent threads
    reactions_count = 0  # Counter for successful reactions
    total_successful_reactions = 0
    results = []  # Store results for further processing

    tokens_used = 0  # Track the total number of tokens used
    
    # Keep processing tokens until we reach the successful reaction limit
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]  # Get the remaining tokens
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]  # Get only the needed tokens
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
                    else:
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO REACT!")
                        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        
        tokens_used += len(tokens_batch)  # Update the total tokens used
        
        # Break if we run out of tokens
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break

    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()  # Use the randomly selected user agent
    }
    
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions
def live_react():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the selected line
    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/video/110105688267538/")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    max_workers = 10  # Set a limit for the number of concurrent threads
    reactions_count = 0  # Counter for successful reactions
    total_successful_reactions = 0
    results = []  # Store results for further processing

    tokens_used = 0  # Track the total number of tokens used
    
    # Keep processing tokens until we reach the successful reaction limit
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]  # Get the remaining tokens
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]  # Get only the needed tokens
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        
        tokens_used += len(tokens_batch)  # Update the total tokens used
        
        # Break if we run out of tokens
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break

    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")
def vid():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the selected line
    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/video/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    max_workers = 10  # Set a limit for the number of concurrent threads
    reactions_count = 0  # Counter for successful reactions
    total_successful_reactions = 0
    results = []  # Store results for further processing

    tokens_used = 0  # Track the total number of tokens used
    
    # Keep processing tokens until we reach the successful reaction limit
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]  # Get the remaining tokens
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]  # Get only the needed tokens
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        
        tokens_used += len(tokens_batch)  # Update the total tokens used
        
        # Break if we run out of tokens
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break

    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")

import requests
import json
import time
import uuid
import base64
import re

def AutoReact():
    def Reaction(actor_id: str, post_id: str, react: str, token: str):
        rui = requests.Session()
        feedback_id = str(base64.b64encode(('feedback:{}'.format(post_id)).encode('utf-8')).decode('utf-8'))
        var = {
            "input": {
                "feedback_referrer": "native_newsfeed",
                "tracking": [None],
                "feedback_id": feedback_id,
                "client_mutation_id": str(uuid.uuid4()),
                "nectar_module": "newsfeed_ufi",
                "feedback_source": "native_newsfeed",
                "feedback_reaction_id": react,
                "actor_id": actor_id,
                "action_timestamp": str(time.time())[:10]
            }
        }
        data = {
            'access_token': token,
            'method': 'post',
            'pretty': False,
            'format': 'json',
            'server_timestamps': True,
            'locale': 'id_ID',
            'fb_api_req_friendly_name': 'ViewerReactionsMutation',
            'fb_api_caller_class': 'graphservice',
            'client_doc_id': '2857784093518205785115255697',
            'variables': json.dumps(var),
            'fb_api_analytics_tags': ["GraphServices"],
            'client_trace_id': str(uuid.uuid4())
        }

        pos = rui.post('https://graph.facebook.com/graphql', data=data).json()
        try:
            if react == '0':
                print(f"{blue}「Success」» {red}Removed reaction from {actor_id} on {post_id}")
                return True
            elif react in str(pos):
                print(f"{blue}「Success」» {red} Reacted with » {actor_id} to {post_id}")
                return True
            else:
                print(f"{red}「Failed」» Reacted with » {actor_id} to {post_id}")
                return False
        except Exception:
            print('Reaction failed due to an error.')
            return False

    def linktradio(post_link: str) -> str:
        # Extract post ID from various Facebook URLs
        patterns = [
            r'/posts/(\w+)',          # Regular post
            r'/videos/(\w+)',         # Video post
            r'/groups/(\d+)/permalink/(\d+)',  # Group permalink post
            r'/reels/(\w+)',          # Reels
            r'/live/(\w+)',           # Live videos
            r'/photos/(\w+)',         # Photo posts
            r'/permalink/(\w+)',      # Permalink posts
            r'story_fbid=(\w+)',      # Story posts
            r'fbid=(\d+)'             # Photo post (new pattern for photo links)
        ]
        
        for pattern in patterns:
            match = re.search(pattern, post_link)
            if match:
                # Return the group ID and post ID for group permalink posts
                if pattern == r'/groups/(\d+)/permalink/(\d+)':
                    return match.group(2)
                return match.group(1)
        
        print("Invalid post link or format")
        return None

    def get_ids_tokens(file_path):
        with open(file_path, 'r') as file:
            data = [line.strip().split('|') for line in file]
        return data

    def choose_reaction():
        
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}HAHA
     {blue}[4] {green}WOW
     {blue}[5] {green}CARE
     {blue}[6] {green}SAD
     {blue}[7] {green}ANGRY
     {red}[8] {red}REMOVE REACTION
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
        
        rec = input(f' {yellow}Choose a reaction: ')
        reaction_ids = {
            '1': '1635855486666999',  # Like
            '2': '1678524932434102',  # Love
            '3': '115940658764963',   # Haha
            '4': '478547315650144',   # Wow
            '5': '613557422527858',   # Care
            '6': '908563459236466',   # Sad
            '7': '444813342392137',   # Angry
            '8': '0'                  # Remove Reaction
        }
        return reaction_ids.get(rec)

    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    
    
    file_choice = int(input(f"    {yellow}Choose: "))
    file_path = file_options.get(file_choice)

    # Step 2: Count tokens in the selected file
    tokens_data = get_ids_tokens(file_path)
    total_tokens = len(tokens_data)
    # Step 3: Ask for starting line
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    start_line = int(input("   \033[38;5;81mEnter the starting line (You currently have {}): ".format(total_tokens)))

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    post_link = input(f'   {yellow}Enter Link: ')
    post_id = get_combined_data(post_link)

    if not post_id:
        return
    
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    react_count = int(input(f"     {yellow}Enter Limit(up to {total_tokens - (start_line - 1)}): "))
    
    # Step 6: Choose reaction type
    react = choose_reaction()
    
    if react == '0':  # Unreact
        remove_count = min(react_count, total_tokens - (start_line - 1))
        reactions_removed = 0
        for actor_id, token in tokens_data[start_line - 1:start_line - 1 + remove_count]:
            success = Reaction(actor_id=actor_id, post_id=post_id, react='0', token=token)
            if success:
                reactions_removed += 1
        print(f"All {reactions_removed} reactions have been successfully removed! You're awesome!")
    elif react:  # React
        send_count = min(react_count, total_tokens - (start_line - 1))
        reactions_sent = 0
        for actor_id, token in tokens_data[start_line - 1:start_line - 1 + send_count]:
            success = Reaction(actor_id=actor_id, post_id=post_id, react=react, token=token)
            if success:
                reactions_sent += 1
        print(f"All {reactions_sent} reactions have been successfully sent! You're awesome!")
    else:
        print('Invalid reaction option.')

# Call AutoReact to run the program


# Call AutoReact to run the program



# To run the AutoReact function:



# Run the AutoReact script







import re

def extract_reel_id(link):
    """
    Extract the reel ID from the provided Facebook reel link.
    Example: https://www.facebook.com/reel/1020864812286112?mibextid=rS40aB7S9Ucbxw6v
    should return '1020864812286112'
    """
    # Define the regular expression pattern to match the reel ID
    pattern = r'/reel/(\d+)'  # Looks for '/reel/' followed by digits
    
    # Search for the pattern in the link
    match = re.search(pattern, link)
    
    if match:
        # If the pattern matches, return the reel ID (the digits after '/reel/')
        return match.group(1)
    else:
        # Return None if no match found
        return None

# Example usage:
def react_comment(token, uid_url, reaction_type, reactions_count):
    """
    Send a reaction using the provided access token and return the results for further processing.
    
    Parameters:
    - token (str): The token in the format 'email|access_token'.
    - uid_url (str): The post ID or user ID where the reaction is sent.
    - reaction_type (str): The type of reaction (e.g., 'LIKE', 'LOVE').
    - reactions_count (int): Number of reactions to send.
    
    Returns:
    - tuple: access_token, status_code, response_text or error message.
    """
    access_token = token.split('|')[1]
    url = f'https://graph.facebook.com/v18.0/{uid_url}/reactions'
    
    params = {
        'access_token': access_token,
        'type': reaction_type
    }
    
    headers_ = {
        'User-Agent': W_ueragnt()  # Your custom user agent function
    }

    try:
        response = requests.post(url, params=params, headers=headers_)
        return access_token, response.status_code, response.text  # Return access_token and response
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)


def comment_react():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")

    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]

    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/541319968479439/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    post_id = input(f"   {green}POST ID: ")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    comment_id = input(f"   {green}COMMENT ID: ")

    uid_url = f"{post_id}_{comment_id}"

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")

    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT exceeding {len(tokens)}")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        return

    reactions_count = 0
    failed_reactions = 0
    target_reactions = num_reactions  # Target number of successful reactions
    remaining_tokens = tokens[:num_reactions]  # Limit the tokens to the number requested

    max_workers = 20
    results = []

    while reactions_count < target_reactions and remaining_tokens:
        # Perform reactions using multithreading
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(react_comment, token, uid_url, reaction_type, reactions_count): token for token in remaining_tokens}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED TO COMMENT!")
                        print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
                    else:
                        failed_reactions += 1
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")

        # Remove tokens that failed
        remaining_tokens = [token for token in remaining_tokens if token not in future_to_token]

        if failed_reactions > 0:
            print(f"{red}Retrying failed reactions...{blue}")

    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL: {reactions_count} successfully reacted")

        



#REACT TO REELS
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()  # Use the randomly selected user agent
    }
    
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions

def perform_reaction_fast():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {red}FRA ACCOUNT 
     {blue}[2] {red}FRA PAGES
     {blue}[3] {red}RPW ACCOUNT
     {blue}[4] {red}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {blue}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the selected line
    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {red}LIKE  👍🏼
     {blue}[2] {red}LOVE 💜
     {blue}[3] {red}WOW 😯
     {blue}[4] {red}SAD 😢
     {blue}[5] {red}ANGRY 🤬
     {blue}[6] {red}HAHA 🤣
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    max_workers = 10  # Set a limit for the number of concurrent threads
    reactions_count = 0  # Counter for successful reactions
    total_successful_reactions = 0
    results = []  # Store results for further processing

    tokens_used = 0  # Track the total number of tokens used
    
    # Keep processing tokens until we reach the successful reaction limit
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]  # Get the remaining tokens
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]  # Get only the needed tokens
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        
                        print(f"     {white}[ACCOUNT UID] {green}{uid}  {yellow} |───────{red}➤ {green}SUCCESSFULLY {yellow} REACTED!")
                        print(f"    {blue}──────────────────────────────────────────────────────{red} • {yellow}• {green}• {blue}──────\033[0m")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        
        tokens_used += len(tokens_batch)  # Update the total tokens used
        
        # Break if we run out of tokens
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break

    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()  # Use the randomly selected user agent
    }
    
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions

def reels():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the selected line
    
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/reel/26674343208847358?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    max_workers = 10  # Set a limit for the number of concurrent threads
    reactions_count = 0  # Counter for successful reactions
    total_successful_reactions = 0
    results = []  # Store results for further processing

    tokens_used = 0  # Track the total number of tokens used
    
    # Keep processing tokens until we reach the successful reaction limit
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]  # Get the remaining tokens
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]  # Get only the needed tokens
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        
        tokens_used += len(tokens_batch)  # Update the total tokens used
        
        # Break if we run out of tokens
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break

    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}")


# Example call
# perform_reaction_fast()


from concurrent.futures import ThreadPoolExecutor
import re
import requests

def extract_user_id_prof(url):
    """Extract user ID from a Facebook profile URL."""
    pattern = r'id=(\d+)|profile\.php\?id=(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1) or match.group(2)  # Return the captured group
    return None  # Return None if no match is found

def follow_account(page_access_token, account_id):
    """Follow an account using a specific page access token."""
    headers_ = {
        'User-Agent': W_ueragnt()  # Assuming W_ueragnt() function provides user agents
    }
    headers = {
        'Authorization': f'Bearer {page_access_token}',
        **headers_  # Merging both headers
    }
    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
            headers=headers
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Request failed for token {page_access_token}: {e}")
        return False

def auto_follow_fast():
    """Automatically follow a target account using tokens and pages."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename

    # Display file options for user to select
    file_choice = int(input(f"    {green}Choose the type of followers : "))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    file_path = file_options.get(file_choice)
    if not file_path:
        print("Invalid choice.")
        return

    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return

    if len(tokens) == 0:
        print("No tokens found in the selected file.")
        return
    
    start_line = int(input(f"    {yellow}Enter the starting line (1 to {len(tokens)}): "))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    tokens = tokens[start_line - 1:]
    
    account_id = extract_user_id_prof(input(f"   {yellow}Enter the target account URL: "))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    if not account_id:
        print(f"Invalid account ID.")
        return

    try:
        
        follow_limit = int(input(f'    {red}LIMIT: '))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print("Invalid number for follow limit.")
        return

    follow_count = 0
    failed_count = 0  # Track failed follows
    current_index = 0  # Start from the beginning of the tokens list

    with ThreadPoolExecutor(max_workers=10) as executor:
        while follow_count < follow_limit and current_index < len(tokens):
            token = tokens[current_index]
            page_access_token = token.split('|')[1]
            uid = token.split('|')[0]

            future = executor.submit(follow_account, page_access_token, account_id)
            success = future.result()

            if success:
                follow_count += 1
                print("   {blue}───────────────────────────────────────────────────────────────\033[0m")
                print(f"     {green}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY FOLLOWED!")
            else:
                failed_count += 1
                print("   {blue}───────────────────────────────────────────────────────────────\033[0m")
                print(f"   {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO FOLLOW!")
                

            current_index += 1  # Move to the next token after each attempt

            if current_index >= len(tokens) and follow_count < follow_limit:
                pass
                current_index = 0  # Reset index to reuse tokens if needed

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f'     {green}SUCCESS: {follow_count}')
    print(f'     {red}FAILED: {failed_count}')

# Run the function









import re

def extract_fbid_dp(url):
    """Extract Facebook ID from a Facebook photo URL."""
    pattern = r'fbid=(\d+)'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)  # Return the captured group
    return None  # Return None if no match is found


import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction(token, uid_url, reaction_type):
    """Send a reaction using the provided access token."""
    access_token = token.split('|')[1]  # Assuming format is email|access_token
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    
    try:
        response = requests.post(auto_react)
        return access_token, response.status_code, response.text  # Return the results for further processing
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)  # Handle request exceptions

def perform_reaction_fast_dp():
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""
       
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  # Display only the filename
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/photo.php?fbid=541361691808600")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = get_combined_data(z)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id  

    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    # Step 5: Check if the requested number of reactions exceeds the available tokens
    if num_reactions > len(tokens):
        print(f"{red}ENTER AGAIN NOT exceeding {len(tokens)}")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        return

    # Step 6: Perform reactions using multithreading
    reactions_count = 0
    max_workers = 10  # Set maximum number of threads
    results = []  

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit reactions for each token
        future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens[:num_reactions]}

        # Process the reactions
        while reactions_count < num_reactions:
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
                    else:
                        pass
                
                    # If the desired number of successful reactions is achieved, break the loop
                    if reactions_count >= num_reactions:
                        print(f"\n{green}Successfully reached {reactions_count} reactions! Exiting...")
                        return  # Exit the function after reaching the desired count
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
            
            # If there are still remaining reactions to perform, submit more tasks from the remaining tokens
            remaining_tokens = tokens[num_reactions: num_reactions + 5]  # Submit 5 more tasks at a time if needed
            if remaining_tokens:
                future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in remaining_tokens}
    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}TOTAL: {reactions_count}")



import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def rep(post_id, comment, access_token):
    """Comment on a Facebook post using the provided access token."""
    
    # Split the token in case it includes 'uid|access_token' format
    if '|' in access_token:
        _, access_token = access_token.split('|', 1)
    
    # Now check if the token starts with 'EA' or 'EAA'
    if not access_token.startswith(("EA", "EAA")):
        return f"Invalid token: {access_token}"
    
    try:
        converted_link = post_id
        auto_comment_url = f'https://graph.facebook.com/v13.0/{converted_link}/comments'
        params = {
            'message': comment,
            'access_token': access_token
        }
        time.sleep(1)  # Sleep for 1 second between comments
        headers = {
            'user-agent': W_ueragnt()  # Use the random user agent
        }
        response = requests.post(auto_comment_url, params=params, headers=headers)
        
        # Print status code and response for debugging

        if response.status_code == 200:
            return f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY COMMENTED: {green}{comment}\033[1;32m"
        else:
            return f"\033[1;31m[FAILED]\033[1;31m FAILED TO COMMENT: {green}{comment} "

    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"


def reply():
    """Perform comments based on user input for file choice, starting line, post link, and number of comments."""
    
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {yellow}[1] {green}FRA ACCOUNT 
     {yellow}[2] {green}FRA PAGES
     {yellow}[3] {green}RPW ACCOUNT
     {yellow}[4] {green}RPW PAGES
     {red}[0] {red}EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        file_choice = int(input(f"     {green}Choose: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the given line
    
    # Step 4: Ask for the post ID
    a = input(f"    {green}Enter the post ID: ")
    b = input(f"    {green}Enter the comment ID: ")
    result = f"{a}_{b}"

    post_id = result
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    try:
        num_comments = int(input(f"    {red}Enter the number of comments: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if num_comments <= 0:
            print("Number of comments must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    comments_list = []
    for i in range(num_comments):
        comment = input(f"    {green}Enter comment {i + 1}: ")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        comments_list.append(comment)

    # Step 6: Ask how many accounts to use for commenting
    try:
        num_accounts = int(input(f"   {green}Enter the number of accounts to use for commenting (1 to {len(tokens)}): "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"Please enter a valid number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 7: Perform comments using multithreading
    results = []
    comments_count = 0
    max_workers = 10  # Set the maximum number of threads
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        for i, token in enumerate(tokens[:num_accounts]):
            comment = random.choice(comments_list)  # Randomly pick a comment
            future = executor.submit(rep, post_id, comment, token)
            future_to_token[future] = token

        for future in as_completed(future_to_token):
            try:
                result = future.result()
                print(result)  # Print the result of the comment attempt
                if "SUCCESSFULLY" in result:
                    comments_count += 1
            except Exception as e:
                print(f"Error processing token: {e}")

    print(f"Total comments made: {comments_count}")

def comment_with_token(post_id, comment, access_token):
    """Comment on a Facebook post using the provided access token."""
    
    # Split the token in case it includes 'uid|access_token' format
    if '|' in access_token:
        _, access_token = access_token.split('|', 1)
    
    # Now check if the token starts with 'EA' or 'EAA'
    if not access_token.startswith(("EA", "EAA")):
        return f"Invalid token: {access_token}"
    
    try:
        converted_link = post_id
        auto_comment_url = f'https://graph.facebook.com/v13.0/{converted_link}/comments'
        params = {
            'message': comment,
            'access_token': access_token
        }
        time.sleep(1)  # Sleep for 1 second between comments
        headers = {
            'user-agent': W_ueragnt()  # Use the random user agent
        }
        response = requests.post(auto_comment_url, params=params, headers=headers)
        
        # Print status code and response for debugging
        pass

        if response.status_code == 200:
            return f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY COMMENTED: {green}{comment}\033[1;32m"
        else:
            pass

    except requests.exceptions.RequestException as e:
        pass
    


def perform_comment_fast():
    """Perform comments based on user input for file choice, starting line, post link, and number of comments."""
    
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {yellow}[1] {green}FRA ACCOUNT 
     {yellow}[2] {green}FRA PAGES
     {yellow}[3] {green}RPW ACCOUNT
     {yellow}[4] {green}RPW PAGES
     {red}[0] {red}EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        file_choice = int(input(f"     {green}Choose: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        pass
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the given line
    
    # Step 4: Ask for the post ID
    a = input(f"    {green}Enter the post ID: ")
    post_id = get_combined_data(a)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    # Step 5: Ask how many comments and get the list of comments
    try:
        num_comments = int(input(f"    {red}Enter the number of comments: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if num_comments <= 0:
            print("Number of comments must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    comments_list = []
    for i in range(num_comments):
        comment = input(f"    {green}Enter comment {i + 1}: ")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        comments_list.append(comment)

    # Step 6: Ask how many accounts to use for commenting
    try:
        num_accounts = int(input(f"   {green}Enter the number of accounts to successfully comment (1 to {len(tokens)}): "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"Please enter a valid number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 7: Perform comments, ensuring the required number of successful comments
    successful_comments = 0
    max_workers =  2 # Set the maximum number of threads

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while successful_comments < num_accounts and tokens:
            token = tokens.pop(0)  # Take the next token
            comment = random.choice(comments_list)  # Randomly pick a comment
            future = executor.submit(comment_with_token, post_id, comment, token)
            
            try:
                result = future.result()
                print(result)  # Print the result of the comment attempt
                if "SUCCESSFULLY" in result:
                    successful_comments += 1  # Increment only for successful comments
                    print(f"{successful_comments}/{num_accounts} comments successful.")
            except Exception as e:
                pass

    # Final output
    if successful_comments == num_accounts:
        print(f"All {num_accounts} comments were successfully made!")
    else:
        print(f"Only {successful_comments}/{num_accounts} comments were successful. No more tokens available.")

def live_comment():
    """Perform comments based on user input for file choice, starting line, post link, and number of comments."""
    
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    jovan()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {yellow}[1] {green}FRA ACCOUNT 
     {yellow}[2] {green}FRA PAGES
     {yellow}[3] {green}RPW ACCOUNT
     {yellow}[4] {green}RPW PAGES
     {red}[0] {red}EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        file_choice = int(input(f"     {green}Choose: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]  # Use tokens starting from the given line
    
    # Step 4: Ask for the post ID
    a = input(f"    {green}Enter the post ID: ")
    post_id = get_combined_data(a)
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    # Step 5: Ask how many comments and get the list of comments
    try:
        num_comments = int(input(f"    {red}Enter the number of comments: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if num_comments <= 0:
            print("Number of comments must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    comments_list = []
    for i in range(num_comments):
        comment = input(f"    {green}Enter comment {i + 1}: ")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        comments_list.append(comment)

    
    try:
        num_accounts = int(input(f"   {green}Enter the number of accounts to use for commenting (1 to {len(tokens)}): "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"Please enter a valid number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 7: Perform comments using multithreading
    results = []
    comments_count = 0
    max_workers = 2  # Set the maximum number of threads
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        for i, token in enumerate(tokens[:num_accounts]):
            comment = random.choice(comments_list)  # Randomly pick a comment
            future = executor.submit(comment_with_token, post_id, comment, token)
            future_to_token[future] = token

        for future in as_completed(future_to_token):
            try:
                result = future.result()
                print(result)  # Print the result of the comment attempt
                if "SUCCESSFULLY" in result:
                    comments_count += 1
            except Exception as e:
                print(f"Error processing token: {e}")

    print(f"Total comments made: {comments_count}")
# Execute the function


# Execute the function

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed



def load_tokens(file_path):
    """Load tokens from the specified file."""
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
        return tokens
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return []

def follow_and_like_facebook_page(uid, access_token):
    """Follow and like a Facebook page/profile using the given UID and access token."""
    follow_url = f"https://graph.facebook.com/v20.0/{uid}/subscribers"
    headers = {'Authorization': f'Bearer {access_token}'}
    
    # Perform the follow action
    follow_response = make_http_request('POST', follow_url, headers=headers)
    if follow_response and 'error' in follow_response:
        print(f"Error following page with UID {uid}: {follow_response['error']['message']}")
    elif follow_response:
        print(f"\033[1;32m[SUCCESSFULLY] FOLLOWED the page/profile with UID {uid}\033[0m")

    # Perform the like action
    like_url = f"https://graph.facebook.com/v20.0/{uid}/likes"
    like_response = make_http_request('POST', like_url, headers=headers)
    if like_response and 'error' in like_response:
        print(f"Error liking page with UID {uid}: {like_response['error']['message']}")
    else:
        print(f"\033[1;32m[SUCCESSFULLY] LIKED the page/profile with UID {uid}\033[0m")

def make_http_request(method, url, headers=None, data=None):
    """Make an HTTP request."""
    try:
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        else:
            print(f"Unsupported HTTP method: {method}")
            return None

        if response.status_code == 200:
            return response.json()
        else:
            print(f"HTTP request failed with status code: {response.status_code}")
            return response.json()
    except Exception as e:
        print(f"An error occurred during the HTTP request: {str(e)}")
        return None

def perform_actions_from_file():
    """Main function to manage the follow and like actions based on user input."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    
    clear_screen()
    jovan()
    
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 1: Load tokens and display the total
    tokens = load_tokens(file_path)
    total_tokens = len(tokens)
    
    if total_tokens == 0:
        print("No tokens available from the selected file.")
        return

    

    # Step 2: Ask for the starting line
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {total_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > total_tokens:
            print(f"Please enter a valid line number between 1 and {total_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Adjust the tokens based on the starting line
    tokens = tokens[start_line - 1:]

    # Step 3: Get the page ID
    uid = input(f"    {green}Enter the Page/Profile UID: ").strip()
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    if not uid.isdigit():
        print("Invalid UID. Please ensure you entered a correct numeric UID.")
        return

    # Step 4: Get the number of actions
    try:
        num_actions = int(input(f"    {green}LIMIT {red}(not exceeding {total_tokens}): ").strip())
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if num_actions > total_tokens:
            print(f"It exceeds the limit of {total_tokens}.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for the actions.")
        return

    # Step 5: Perform actions using multithreading
    action_count = 0
    tasks = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        for token in tokens[:num_actions]:  # Limit the tokens to the number of actions requested
            future = executor.submit(follow_and_like_facebook_page, uid, token.split('|')[1])  # Assuming token format is email|access_token
            tasks.append(future)
            action_count += 1

        # Wait for all tasks to complete
        for task in as_completed(tasks):
            y = token.split('|')[0]
            try:
                task.result()  # To raise any exceptions if occurred during execution
            except Exception as e:
                print(f"An error occurred during execution: {str(e)}")

    print(f"     {red}ID {white}: {blue}{y} | {green}\nSUCCESSFULLY FOLLOWED AND LIKED | ID:", uid)
    print(f"Completed {action_count} requested actions.")

# Call the method to execute the functionality
import requests
import sys
import time
from concurrent.futures import ThreadPoolExecutor

gome_token = []

def tokz(input_cookies):
    for cookie in input_cookies:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass

def shar():
    clear_screen()
    jovan()
    input_cookies = input(f"     {green}Enter Cookie:  \x1b[38;2;233;233;233m").split(',')
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    id_share = input(f"     {green}Enter Post ID: \x1b[38;2;233;233;233m")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    total_share = int(input(f"    {green}How Many Share: \x1b[38;2;233;233;233m"))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    delay = int(input(f"    {green} Delay Share: \x1b[38;2;233;233;233m"))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print('\x1b[38;2;173;255;47m[*] \x1b[38;2;233;233;233mwaiting...', end='\r')
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    all = tokz(input_cookies)
    total_live = len(all)
    print(f'\x1b[38;2;173;255;47mLive: \x1b[38;2;233;233;233m{total_live} \x1b[38;2;173;255;47mCookies')
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    if total_live == 0:
        sys.exit()

    print(f"    {green}───────────────────────────────────────────────────────────────\033[0m")
    stt = 0

    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = []
        while True:
            for tach in all:
                if stt >= total_share:
                    break
                futures.append(executor.submit(share, tach, id_share))
                stt += 1
                print(f'\x1b[38;2;173;255;47mShare: + \x1b[38;2;233;233;233m{stt}', end='\r')
                time.sleep(delay)
            if stt >= total_share:
                break

    gome_token.clear()
    input('\x1b[38;2;173;255;47m[*] \x1b[38;2;233;233;233mEnter^^\033[0m')

import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan



import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan
import platform
import os
import random
import uuid
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
R = "\033[31m"  # Red
G = "\033[32m"  # Green
Y = "\033[33m"  # Yellow
B = "\033[34m"  # Blue
M = "\033[35m"  # Magenta
P = "\033[36m"  # Cyan
C = "\033[37m"  # White
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def randc():
    return random.choice([R, G, Y, B, M, P, C])

def logo():
    rp(pan(f"""{randc()}

██╗░░░██╗██╗░░░██╗░██████╗██╗░░██╗
╚██╗░██╔╝██║░░░██║██╔════╝██║░░██║
░╚████╔╝░██║░░░██║╚█████╗░███████║
░░╚██╔╝░░██║░░░██║░╚═══██╗██╔══██║
░░░██║░░░╚██████╔╝██████╔╝██║░░██║
░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝░░╚═╝
                  """,
           title=f"{Y}COOKIE GETTER", subtitle=f"{R}DEVELOP BY Y U S H ", border_style="bold yellow"))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_file_path():
    clear_screen()
    jovan()
    return input(f"     {green}{C}(Enter path to file with email and password):~ ")
print(f"  ")

def get_cookie_storage_path():
    print(f"    {red}───────────────────────────────────────────────────────────────\033[0m")
    return input(f"     {yellow}{C}(Enter path to store cookies):~ ")

def read_credentials(file_path):
    credentials = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if '|' in line:
                uid, password = line.split('|', 1)
                credentials.append((uid.strip(), password.strip()))
            elif line:
                print(f"Warning: Skipping invalid line format: {line}")
                
    except FileNotFoundError as e:
        print(f"Error: File not found {file_path}: {str(e)}")
    
   
    return credentials


def cuser(user, passw):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'method': 'auth.login',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
    }
    response = pt("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False)
    return response.json()

def runing():
    clear_screen()
    jovan()
    file_path = get_file_path()
    storage_path = get_cookie_storage_path()  # Get path for storing cookies
    credentials = read_credentials(file_path)

    if not credentials:
        print(f"{R}No credentials found in the file.")
        return
     
    print(f"      {red}FOUND {len(credentials)} {green}CREDENTIALS !...")

    for user, passw in credentials:
        response = cuser(user, passw)

        if "session_key" in response:
            clear()
            cookie_str = '; '.join(f'{i["name"]}={i["value"]}' for i in response.get('session_cookies', []))
            clear_screen()
            jovan()
            print(f"     {red}COOKIE {yellow}: {white}{C}{cookie_str}")
            
            with open(storage_path, 'a') as f:  # Use the user-defined path for storing cookies
                f.write(cookie_str + '\n')
        else:
            print(f"{R}INVALID/CHECKPOINT for USER ID: {C}{user}")

    print(f"{G}Processing complete. All credentials have been processed.")

# Run main() only when script is executed directly
def bitz():
    clear_screen()
    jovan()
    print(f"     {yellow}[1] {green}GET COOKIE")
    print(f"     {yellow}[2] {green}AUTO CREATE PAGE")
    print(f"    {red}───────────────────────────────────────────────────────────────\033[0m")
    num_reactions = int(input(f'     {red}Enter Option: '))

    if num_reactions == 1:
        runing()
    elif num_reactions == 2:
        hackezr() # Placeholder for further implementation
    else:
        print(f"{R}Invalid option selected.")
import random
import requests
from colorama import init, Fore, Style
import os

# Initialize colorama
init()

class RegPro5:
    def __init__(self, cookies) -> None:
        self.cookies = cookies
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }
        
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text

        # Initialize fb_dtsg to None
        self.fb_dtsg = None
        
        # Try to find fb_dtsg using multiple patterns
        patterns = [
            '{"name":"fb_dtsg","value":"',  # Primary pattern
            ',"f":"',                      # Secondary pattern
            # Add more patterns if necessary
        ]

        for pattern in patterns:
            try:
                self.fb_dtsg = profile.split(pattern)[1].split('"},')[0]
                break  # Break if the pattern is found
            except IndexError:
                continue  # Try the next pattern

        if not self.fb_dtsg:
            kolor("Error: fb_dtsg not found in profile data.", 'red')
    import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
# Color codes for formatting output
purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
import random
import string
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))

    # Randomly vary the Android OS version, device, and app version for realism
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))  # Updated range for FBAV versions
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])

    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    
    return ua_bgraph

ua_bgraph = generate_user_agent()


import requests
import random
import concurrent.futures as thread
import os
import string

# Random FB version generation
fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))

# User agent string
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        
        if uid in existing_uids:
            print(f"     {yellow}[INFO] {red}ACCOUNT --> {white}{uid} {red}already exists.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            return

        response = requests.post(url, data=data).json()
        
        print(response)
        if 'access_token' in response:
            token = response['access_token']

            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")

            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: Extracted Account ─────> {uid}.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            success_count.append(uid)
        else:
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT Account ─────> {uid}.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except Exception as e:
        print(f"     \033[1;31m[ERROR]\033[0m Error extracting account: {uid}. Reason: {str(e)}\033[0m\n")


def proz(accounts_file, token_output_path, extract_type):
    """Process the accounts and extract tokens concurrently."""
    success_count = []

    # Load existing uids from the output file to avoid duplicates
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
        return

import requests
import random
import concurrent.futures as thread
import os
import string

fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def load_existing_tokens(path_file):
    """Load existing accounts or pages from the output file."""
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}  # Set of existing uids or page ids
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token
    
    if uid in existing_tokens:
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
        return

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        response = requests.post(url, data=data).json()
        
        if 'access_token' in response:
            token = response['access_token']

            # Extract Facebook Pages associated with the account token
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}Page ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")

            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")

    except Exception as e:
        print(f"[ERROR] Error extracting account: {uid}. Reason: {str(e)}")

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    pages_data = []
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f'Error: {response.text}')
            return None
        
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        
        url = data.get('paging', {}).get('next')  # Update the URL for the next request

    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
def extraction():

    clear_screen()
    jovan()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("     \033[1;14m───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {green}CHOICE : ").strip() 
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")
def axl2():
    clear_screen()
    jovan()
    folder_path = "/sdcard/boostphere"  
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    prozc(file_path, account_file, extract_type)
def axl1():
    clear_screen()
    jovan()
    folder_path = "/sdcard/boostphere"
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    token_output_path = account_file

    proz(file_path, token_output_path, extract_type)


def get_token_from_file(file_path):
    """Read tokens from the file and return a random token."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        tokens = [line.strip().split('|')[1] for line in lines if '|' in line]
    return random.choice(tokens)

class FacebookPoster:
    def __init__(self, link):
        self.link = link

    def share_post(self, token):
        """Shares a post on the user's feed with 'Only Me' privacy."""
        url = "https://graph.facebook.com/v13.0/me/feed"
        payload = {
            'link': self.link,
            'published': '0',
            'privacy': '{"value":"SELF"}',
            'access_token': token
        }
        try:
            response = requests.post(url, data=payload)
            print(response)
            if response.status_code == 200:
                
                print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
                print("      Successfully Shared")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return False

def share_in_threads(link, file_path, num_shares):
    start_all = time.time()  # Record the start time for the entire operation
    
    def worker():
        success = False
        while not success:
            token = get_token_from_file(file_path)
            fb_poster = FacebookPoster(link)
            success = fb_poster.share_post(token)

    max_workers = 40
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for _ in range(num_shares):
            executor.submit(worker)

    end_all = time.time()  # Record the end time for the entire operation
    duration = end_all - start_all
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"\n  {yellow}Sharing started: {start_all}")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"     {yellow}Sharing ended: {end_all}")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f"    {yellow}Total duration: {duration:.2f} seconds\033[0m")
def count_tokens(accounts_file, pages_file):
    """Count the number of accounts and pages stored in the respective files."""
    total_accounts = 0
    total_pages = 0

    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Account file not found: {accounts_file}")

    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Page file not found: {pages_file}")

    return total_accounts, total_pages
def share():
    clear_screen()
    jovan()
    print(f"""     \033[1;37mCHOOSE TYPE OF ACCOUNTS TO AUTO SHARE: 
     \033[1;34m[1] \033[1;32mFRA ACCOUNT 
     \033[1;31m[0] \033[1;31mEXIT 
    \033[1;34m───────────────────────────────────────────────────────────────\033[0m""")
    choice = input(f"     {blue}Choice ")
    
    file_map = {
        '1': '/sdcard/boostphere/FRAACCOUNT.txt',
        '2': '/sdcard/boostphere/FRAPAGES.txt',
        '3': '/sdcard/boostphere/RPWACCOUNT.txt',
        '4': '/sdcard/boostphere/RPWACCOUNT.txt'
    }

    file_path = file_map.get(choice)
    if not file_path:
        print("Invalid choice. Exiting.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    post_id = input(f"   {green}Enter the post ID to share: ")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    num_shares = int(input(f"   {green}how many share ? : "))

    # Construct the link using the post ID
    link = f"https://www.facebook.com/{post_id}"

    share_in_threads(link, file_path, num_shares)
def main2(): 
    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages = '/sdcard/boostphere/RPWPAGES.txt'
    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts,rpwpages)
    clear_screen()
    jovan()
    print(f"""                 {yellow}OVERVIEW OF STORED ACCOUNT & PAGES💫
          
                            {blue}FRA ACCOUNT{yellow} : {green}{total_accounts}
      {blue}───────────────────────────────────────────────────────────────\033[0m""")
    print(f"     {blue}[1] {yellow}EXTRACT ACCOUNT")
    print(f"     {blue}[2] {yellow}AUTO SHARE ")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f'    {yellow}Enter Choice: ')
    if choice == '1': 
        extraction()
    if choice == '2': 
        share()



def extraction():

    clear_screen()
    jovan()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {green}CHOICE: ").strip() 
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")
    def reg(self, name):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"' + name + '","page_referrer":"launch_point","actor_id":"' + self.id_acc + '","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)

        try:
            result = response.json()
            if 'id' in result:
                page_id = result['id']
                self.set_profile_picture(page_id)
            return result
        except:
            return response.text

    def set_profile_picture(self, page_id):
        picture_path = "/home/spade/Desktop/load data/Profile.jpeg"  # Replace with your actual path to the profile picture
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': f'https://www.facebook.com/{page_id}',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'ProfilePicUpload',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        files = {
            'source': (os.path.basename(picture_path), open(picture_path, 'rb'), 'image/jpeg')
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            'profile_id': page_id,
            'fb_dtsg': self.fb_dtsg,
            'photo_source': '4',
            'composer_entry_time': '0',
            'composer_session_id': 'abc',
            'ref': 'timeline',
            'upload_id': 'profile_pic',
            'upload_type': 'profile',
        }

        response = requests.post('https://www.facebook.com/photos/upload', headers=headers, files=files, data=data)

        try:
            return response.json()
        except:
            return response.text

# Function to print colored text
def kolor(text, color):
    if color == 'green':
        print(Fore.GREEN + text + Style.RESET_ALL)
    elif color == 'red':
        print(Fore.RED + text + Style.RESET_ALL)
    else:
        print(text)

def get_cookies_file_path():
    clear_screen()
    jovan()
    return input("Enter the path to the cookies.txt file: ")

def hackezr():
    
    cookies_file = get_cookies_file_path()

    try:
        with open(cookies_file, 'r') as f:
            cookies_list = f.readlines()
    except FileNotFoundError:
        kolor("Error: File not found. Please check the path.", 'red')
        return

    for cookie_line in cookies_list:
        cookie_line = cookie_line.strip()  # Remove leading/trailing whitespace

        # For your provided format, no need to split further; just use the entire line as cookies
        cookies = cookie_line

        vietnamese_names = [
           "MrsTexasUNIVERSE Dr.MeenakshiRavi",
"Melanii",
"Israt Jahan",
"Md Rubel Kahan",
"Mariya Akthr Sathi",
"Israt Xahan Esha",
"Younietha Wasilah",
"Nusaiba Islam Eva",
"Lx Zoya",
"Tasnia Rahman",
"Mehedi Hasan",
"Roja Islam",
"Esme Johnston",
"Riya Jahan",
"Sinthiya Chowdhury",
"Jannatul Ferdos",
"Aysha Jannat",
"Moinul Islam Shanto",
"Tanveer Rahman",
"Rosabel Mercado Oaing",
"Bnegali Basi",
"Ashlie Allaisa",
"Rapk Miah",
"Saima Akter",
"Md Minar",
"Tahmina Jannat Mim",
"Humaryra Bin Allbihi",
"Sadiya Akter",
"MD Naeem",
"Foysol Khan",
"Md Robiul Sheikh",
"Md Sohel",
"Alex Hels Afridy",
"Ocena Manus",
"Shohag Sheikh",
"Gojo Saturo",
"Shaddat Khan",
"MD Mithun",
"Rakib Ahmmed Foysal",
"Md Oliull Sheikh",
"Md Sabbir Shaike",
"Sk Tushar",
"Vagne Dev",
"MB �m�m",
"Limon Sehk Limon Sehk",
"Md Milan",
"Reyad Islam",
"Md Shobuzpra",
"Md Masum Islam",
"Tanzim Rabby",
"R�bin Here",
"MD Sumon MD Sumon",
"Asif Khan",
"Mis Afia",
"���m�l H�q��",
"Md Shakib Mridha",
"Urzzal Mia",
"Samuel Ramirez",
"Shaddat Khan",
"Shaheen Kanaipur",
"MD Salman Sak",
"MD Amirol",
"Mahedi Islam",
"MD Alhassan Hawlder",
"Anis Osim",
"Raihan Islam",
"Hamida Forid Pur",
"MD Sohel Sheikh",
"Md Emram",
"Md Nijam Uddin Sheikh",
"MD Biplob",
"Md Moyazzem",
"Md Azad",
"BA DH ON",
"Md Rezaul Rezaul",
"Tanjin Molla",
"Md Sumon",
"Obaidul Krim",
"Rabby Khan",
"Jahangir Gazi",
"Md. Tamim",
"Najir Sheikh",
"Abu Bakar Khan",
"Md Alamin",
"Sgush Rsuhe",
"Rabby Sheikh",
        ]

        random_name = random.choice(vietnamese_names)

        reg_instance = RegPro5(cookies)
        result = reg_instance.reg(random_name)

        if 'error' not in result:
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            kolor(f"     {green}[SUCCESS] {red}Created Page", 'green')
        else:
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            kolor(f"     {red}[UNSUCCESSFUL] {green}Created Page", 'red')
import requests
import os

class Color:
    END = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'

def pzl(username, passwords):
    # Define the new access token and API details
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    for password in passwords:
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'email': username,
            'password': password,
            'access_token': accessToken
        }
        
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            responses = response.json()
            
            if 'access_token' in responses:
                return responses['access_token'], True
            else:
                error_msg = responses.get('error_msg', 'Unknown error')
                print(f"{Color.RED}Error for {username}: {error_msg}{Color.END}")
        except requests.exceptions.RequestException as e:
            print(f"{Color.RED}Error for {username}: {str(e)}{Color.END}")
    
    return None, False

def sav(tokens_array, token_file_path):
    """Save tokens in uid|token format."""
    with open(token_file_path, 'w') as file:
        for token_info in tokens_array:
            uid = token_info['email']
            access_token = token_info['access_token']
            file.write(f"{uid}|{access_token}\n")

def prz(file_path, tokens_array):
    """Process the file and extract tokens for uid|pass format."""
    if not os.path.isfile(file_path):
        print(f"{Color.BOLD}File {file_path} does not exist.{Color.END}")
        return

    print(f"     {Color.BOLD}Processing file: {file_path}{Color.END}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        print(f"{Color.BOLD}File {file_path} is empty.{Color.END}")
        return

    account_pairs = [line.strip() for line in lines if '|' in line]

    if not account_pairs:
        print(f"{Color.BOLD}No valid uid|pass pairs found in {file_path}.{Color.END}")
        return

    for account in account_pairs:
        uid, password = account.split('|')
        pass
        token, success = pzl(uid, [password])  # Using the password as a single element list
        if success:
            tokens_array.append({"email": uid, "access_token": token})
            print(f"{Color.GREEN}Successfully extracted token for {uid}{Color.END}")
        else:
            print(f"{Color.BOLD}Failed to get token for {uid}.{Color.END}")

def maz():
    clear_screen()
    jovan()
    file_path = input(f"{Color.YELLOW}Enter the path of the text file with accounts and passwords: {Color.END}").strip()
    token_file_path = input(f"{Color.YELLOW}Enter the path of the file where tokens should be stored: {Color.END}").strip()
    
    tokens_array = []
    prz(file_path, tokens_array)

    if tokens_array:
        pass
        for token_info in tokens_array:
            pass
        
        sav(tokens_array, token_file_path)  # Save tokens in uid|token format
    else:
        print(f"{Color.BOLD}No tokens collected.{Color.END}")

    print(f"{Color.BLUE}Exiting the program...{Color.END}")

# Run the program






# Start the program



def start():
    clear_screen()
    jovan()
    token_file_path = input("Enter the path to the file containing the tokens: ").strip()
    
    tokens = rad(token_file_path)
    if not tokens:
        print("No tokens found. Exiting.")
        return

    if not os.path.exists(DIRECTORY):
        print(f"Error: Directory '{DIRECTORY}' does not exist.")
        return

    files_in_directory = os.listdir(DIRECTORY)
    if not files_in_directory:
        print(f"Error: No files found in directory '{DIRECTORY}'.")
        return

    for user_token in tokens:
        pages = pigzs(user_token)
        if not pages:
            print(f"No pages found for token {user_token}. Skipping.")
            continue

        for page in pages:
            pass
            page_id = page['id']
            page_access_token = page.get('access_token')

            if not page_access_token:
                print(f"No access token found for page {page_id}. Skipping.")
                continue

            # Check if the page already has a profile picture
            if pec(page_id):
                pass
                continue

            # Randomly select a file from the directory
            file_name = random.choice(files_in_directory)
            file_path = os.path.join(DIRECTORY, file_name)

            result = plod(page_id, page_access_token, file_path)
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            print(f"    {green}SUCCESSFULLY UPLOADED PROFILE PICTURE {page['name']} ──────> {page['id']} ")
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            # Add a delay between requests to avoid hitting rate limits
            time.sleep(2)  # Adjust delay as needed
import requests
import os
import random
import time

BASE_URL = 'https://graph.facebook.com/v18.0'
DIRECTORY = 'Picture'

def pigzs(access_token):
    url = f'{BASE_URL}/me/accounts'
    params = {
        'access_token': access_token
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error getting pages for token {access_token}: {str(e)}")
        return []

def pec(page_id):
    url = f'{BASE_URL}/{page_id}?fields=picture'
    try:
        response = requests.get(url)
        response.raise_for_status()
        picture_data = response.json().get('picture', {})
        return 'data' in picture_data and 'url' in picture_data['data']
    except requests.exceptions.RequestException as e:
        print(f"Error checking profile picture for page {page_id}: {str(e)}")
        return False

def plod(page_id, page_access_token, file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {
                'source': file
            }
            data = {
                'access_token': page_access_token
            }
            url = f'{BASE_URL}/{page_id}/picture'
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error uploading profile picture to page {page_id}: {str(e)}")
        return {'error': str(e)}
    except FileNotFoundError as e:
        print(f"Error: File not found {file_path}: {str(e)}")
        return {'error': str(e)}

def rad(file_path):
    tokens = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Strip any whitespace and check if the line contains the expected format
                line = line.strip()
                if '|' in line:
                    uid, token = line.split('|', 1)  # Split on the first '|'
                    tokens.append((uid.strip(), token.strip()))  # Append as a tuple
    except FileNotFoundError as e:
        print(f"Error: Tokens file not found {file_path}: {str(e)}")
    return tokens

def mainzsa():
    clear_screen()
    jovan()
    print(f"     {red}[1] {green}GET TOKEN")
    print()
    print(f"     {red}[2] {green}SET PFP")
    print("\033[1;31m───────────────────────────────────────────────────────────────\033")
    choice = input("Enter: ")
    if choice == '1':
        maz()
    if choice == '2':
        start()
    else: 
        print("invalid po")
        clear_screen()



           


import requests
import random
import string
import os

CODE_FILE = '/sdcard/boostphere/generated_code.txt'  # File to store the generated code

def ensure_file_exists():
    """Ensure that the code file exists by creating it if it doesn't exist."""
    open(CODE_FILE, 'a').write('')  # This will create the file if it doesn't exist, but won't modify it.

def generate_code():
    """Generate a unique code in the format BOOSTPHERE-XXX-XXXXX."""
    prefix = "BOOSTPHERE"
    number_part = ''.join(random.choices(string.digits, k=3))  # 3 random digits
    letters_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # 5 alphanumeric characters
    code = f"{prefix}-{number_part}-{letters_part}"
    return code

def save_code(code):
    """Save the generated code to a file."""
    with open(CODE_FILE, 'w') as file:
        file.write(code)

def load_code():
    """Load the code from the file, if it exists."""
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE, 'r') as file:
            return file.read().strip()
    return None

def is_code_approved(code):
    """Check if the generated code is approved by fetching the approval list."""
    try:
        response = requests.get("https://raw.githubusercontent.com/testerz559/BOOSTINGAPPROVAL/refs/heads/main/Approval")
        response.raise_for_status()  # Raise an error for bad responses
        approved_codes = response.text.splitlines()  # Split the response into lines
        
        # Remove comments and strip whitespace, then check for the code
        approved_codes = [line.split('#')[0].strip() for line in approved_codes if line]
        return code in approved_codes  # Check if the code is in the approved list
    except requests.RequestException as e:
        print(f"Error fetching the approval list: {e}")
        return False


def generate_and_check_code():
    """Generate a code if not existing, check if it's approved, then run main()."""
    ensure_file_exists()  # Ensure the code file exists before proceeding
    
    code = load_code()
    
    if code is None or code == '':
        code = generate_code()
        save_code(code)
        clear_screen()
        jovan()
        
        print(f"      {yellow}YOUR GENERATED CODE {white}: {red}{code}")
    else:
        clear_screen()
        jovan()
        
        print(f"     {yellow}YOUR CODE {white}: {red}{code}")

    if is_code_approved(code):
        main()
    else:
        print(f"     {red}───────────────────────────────────────────────────────────────\033[0m")
        print(f"     {red}CODE IS NOT APPROVED ! {yellow}PLEASE SEND IT TO {white}: {yellow}https://www.facebook.com/profile.php?id=100078043222260")

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_profile_id(access_token):
    """Retrieve the profile ID using the provided access token."""
    try:
        url = 'https://graph.facebook.com/me'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return response.json().get('id')
        else:
            return None
    except requests.exceptions.RequestException:
        return None

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def join_group(group_id, profile_id, access_token):
    """Attempt to join a group using the provided access token."""
    try:
        # Construct the URL by including the profile ID in the path
        url = f'https://graph.facebook.com/{group_id}/members/{profile_id}'
        params = {'access_token': access_token}
        
        response = requests.post(url, params=params)
        
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
import requests
#https://graph.facebook.com/debug_token?input_token={token}&access_token={token}
def val(token):
    # Create the validation URL
    validation_url = f"https://graph.facebook.com/debug_token?input_token={token}&access_token={token}"

    # Send the request to the Facebook Graph API
    response = requests.get(validation_url)

    # Return the response as JSON if valid, otherwise return None
    if response.status_code == 200:
        return response.json()
    else:
        return None
import requests
import base64

# Your GitHub token
token = ''

# GitHub API headers
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Define file options for storing tokens
file_options = {
    1: "/sdcard/boostphere/FRAACCOUNT.txt",
    2: "/sdcard/boostphere/FRAPAGES.txt",
    3: "/sdcard/boostphere/RPWACCOUNT.txt",
    4: "/sdcard/boostphere/RPWPAGES.txt"
}

def git(repo_owner, repo_name, file_path):
    # GitHub API URL for file content
    file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'

    response = requests.get(file_url, headers=headers)
    
    if response.status_code == 200:
        content = response.json()
        file_sha = content['sha']
        file_content = base64.b64decode(content['content']).decode('utf-8')
        return file_content, file_sha
    elif response.status_code == 404:
        print(f"     FAILED")
        return None, None
    else:
        print(f"     FAILED")
        return None, None

def contint(repo_owner, repo_name, file_path, file_sha):
    # GitHub API URL for updating the file content (clearing the file)
    file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
    
    empty_content = base64.b64encode(''.encode('utf-8')).decode('utf-8')
    commit_message = f"Clear {file_path}"

    data = {
        "message": commit_message,
        "content": empty_content,
        "sha": file_sha
    }

    response = requests.put(file_url, json=data, headers=headers)
    
    if response.status_code == 200:
        pass
    else:
        pass

def choose_file_path():
    clear_screen()
    jovan()
    print(f"""     \033[1;37mCHOOSE TYPE OF FILE TO SAVE TOKENS: 
     \033[1;34m[1] \033[1;32mFRA ACCOUNT 
     \033[1;34m[2] \033[1;32mFRA PAGES
     \033[1;34m[3] \033[1;32mRPW ACCOUNT
     \033[1;34m[4] \033[1;32mRPW PAGES
     \033[1;31m[0] \033[1;31mEXIT 
    \033[1;31m───────────────────────────────────────────────────────────────\033[0m""")

    # Ask the user to enter their choice
    choice = int(input(f"     {red}ENTER NUMBER {white}: "))
    
    if choice == 0:
        print("Exiting the program.")
        exit()  # Exit the program if the user chooses 0
    elif choice in file_options:
        return file_options[choice]  # Return the selected file path
    else:
        print("Invalid choice. Please try again.")
        return choose_file_path()  # Retry if the choice is invalid

def cynt(content):
    # Count the number of tokens by splitting the content into lines
    tokens = content.splitlines()
    return len(tokens)

def count_cookies(cookies_content):
    # Count the number of cookies by splitting the content into lines
    cookies = cookies_content.splitlines()
    return len(cookies)

def githubtoks():
    clear_screen()
    jovan()
    repo_owner = 'boostphere'  # Change this to your GitHub username
    
    repo_name = input(f"    {yellow}CODE: ")

    # Fetch contents of the Tokens file
    tokens_content, tokens_sha = git(repo_owner, repo_name, 'Tokens')
    if tokens_content:
        token_count = cynt(tokens_content)
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print(f"       {red}{token_count} {green}TOKENS FOUND !")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        # Ask the user where to store the tokens
        storage_path = choose_file_path()
        with open(storage_path, 'a') as file:

           file.write(tokens_content + '\n')  # Append new tokens to the file

        
        # Clear the Tokens file
        contint(repo_owner, repo_name, 'Tokens', tokens_sha)

    # Fetch contents of the Cookies file
    cookies_content, cookies_sha = git(repo_owner, repo_name, 'Cookies')
    
    if cookies_content:
        cookie_count = count_cookies(cookies_content)
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print(f"       {red}{cookie_count} {green}COOKIES FOUND !")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        # Ask the user where to store the cookies
        cookie_path = input("PATH TO SAVE COOKIES: ")
        with open(cookie_path, 'a') as cookie_file:

            cookie_file.write(cookies_content + '\n')  # Append new cookies to the file

        
        # Clear the Cookies file
        contint(repo_owner, repo_name, 'Cookies', cookies_sha)
    else:
        pass





def check():
    clear_screen()
    jovan()
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }

    # Display the available file options
    print(f"""     \033[1;37mCHOOSE TYPE OF FILE TO VERIFY: 
     \033[1;34m[1] \033[1;32mFRA ACCOUNT 
     \033[1;34m[2] \033[1;32mFRA PAGES
     \033[1;34m[3] \033[1;32mRPW ACCOUNT
     \033[1;34m[4] \033[1;32mRPW PAGES
     \033[1;31m[0] \033[1;31mEXIT 
    \033[1;31m───────────────────────────────────────────────────────────────\033[0m""")

    choice = int(input(f"     {green}Enter your choice: "))
    if choice in file_options:
        file_path = file_options[choice]
    elif choice == 0:
        print("Exiting...")
        return
    else:
        print("Invalid choice. Exiting...")
        return

    # Read the tokens from the selected file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    valid_tokens = []
    
    # Validate each token and keep valid ones
    for line in lines:
        uid, token = line.strip().split('|')
        if val(token):
            valid_tokens.append(line.strip())
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            print(f"     {green}ACCOUNT ─────> {blue}{uid} {white}= {yellow} IS VALID")
        else:
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            print(f"     {red}ACCOUNT ─────> {blue}{uid} {white}= {yellow} IS NOT VALID AND WILL BE REMOVED")

    # Write the valid tokens back to the file
    with open(file_path, 'w') as file:
        for valid_token in valid_tokens:
            file.write(valid_token + '\n')

    


def perform_group_join():
    """Perform group joins based on user input for file choice, group ID, and number of tokens."""
    
    clear_screen()
    jovan()
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    
    # Display the available file options
    print(f"""     \033[1;37mCHOOSE TYPE OF ACCOUNTS TO JOIN GROUP: 
     \033[1;34m[1] \033[1;32mFRA ACCOUNT 
     \033[1;34m[2] \033[1;32mFRA PAGES
     \033[1;34m[3] \033[1;32mRPW ACCOUNT
     \033[1;34m[4] \033[1;32mRPW PAGES
     \033[1;31m[0] \033[1;31mEXIT 
    \033[1;31m───────────────────────────────────────────────────────────────\033[0m""")

    try:
        file_choice = int(input("   \033[1;32mChoose: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    # Step 3: Ask the user for the starting line
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    try:
        start_line = int(input(f"   \033[1;32mEnter the starting line (1 to {available_tokens}): "))
        print(f"    {red}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]

    # Step 4: Ask the user for the group ID
    group_id = input(f"   {yellow}[1;32mEnter the group ID: ")
    print(f"    {red}───────────────────────────────────────────────────────────────\033[0m")

    # Step 5: Ask the user for the number of tokens to process
    try:
        num_tokens = int(input(f"   \033[1;32mEnter Limit: "))
        print(f"    {red}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print("Please enter a valid number for tokens.")
        return

    # Step 6: Check if the requested number of tokens exceeds the available tokens
    if num_tokens > len(tokens):
        print(f"\033[1;31mERROR: Number exceeds available tokens ({len(tokens)}).")
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        return

    # Step 7: Join the group using multithreading and dynamic profile ID retrieval
    join_count = 0
    failed_count = 0
    retries_left = num_tokens  # The number of retries left to perform
    max_workers = 10  # Set maximum number of threads
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        
        # Attempt to join the group for the specified number of tokens
        while join_count < num_tokens and retries_left > 0:
            for token in tokens[:retries_left]:
                access_token = token.split('|')[1]
                profile_id = get_profile_id(access_token)
                
                if profile_id:
                    future = executor.submit(join_group, group_id, profile_id, access_token)
                    future_to_token[future] = token
                else:
                    print(f"\033[1;31m[FAILED] \033[1;37mFailed to retrieve profile ID for token \033[1;33m{token}\033[0m")

            # Process the results of the joins
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                try:
                    success = future.result()
                    if success:
                        join_count += 1
                        print(f"\033[1;32m[SUCCESS] \033[1;37mSuccessfully joined group {group_id}")
                    else:
                        failed_count += 1
                        print(f"{red}[UNSUCCESS] \033[1;FAILED joined group {group_id}")
                    
                    # Stop retrying if we've reached the success limit
                    if join_count >= num_tokens:
                        break
                except Exception as e:
                    print(f"Error processing token {token}: {e}")

            
            retries_left = num_tokens - join_count

        print("\033[1;31m───────────────────────────────────────────────────────────────\033[0m")
        print(f"\033[1;32mTOTAL SUCCESSFUL: {join_count}\033[0m")
        print(f"\033[1;31mTOTAL FAILED: {failed_count}\033[0m")
def live(url):
    # Split the URL by slashes
    parts = url.split('/')
    
    # Ensure that the URL has enough parts
    if len(parts) > 4:
        user_id = parts[3]  # The user/page ID
        video_id = parts[5]  # The video ID
        
        # Combine them with an underscore
        return f"{user_id}_{video_id}"
    else:
        return None  # Return None if the URL format is unexpected
import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan

import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan
import platform
import os
import random
import uuid
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
R = "\033[31m"  # Red
G = "\033[32m"  # Green
Y = "\033[33m"  # Yellow
B = "\033[34m"  # Blue
M = "\033[35m"  # Magenta
P = "\033[36m"  # Cyan
C = "\033[37m"  # White
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import re
purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
def jovan():
    adrkz = "\033[34m "
def jovan():
    adrkz = "\033[34m "
    print(f"""
    {red} 
{blue}╭──────────────────────────────────────────────────────────────────────────╮
{blue}│                                                                     {blue}     │
{blue}│ {hotpink}       ░█████╗░███╗░░██╗███╗░░██╗██╗██╗░░██╗██╗░░██╗██╗░░░██╗{blue}            │
{blue}│  {hotpink}      ██╔══██╗████╗░██║████╗░██║██║╚██╗██╔╝╚██╗██╔╝╚██╗░██╔╝ {blue}           │
{blue}│  {hotpink}      ███████║██╔██╗██║██╔██╗██║██║░╚███╔╝░░╚███╔╝░░╚████╔╝░ {blue}           │
{blue}│ {hotpink}       ██╔══██║██║╚████║██║╚████║██║░██╔██╗░░██╔██╗░░░╚██╔╝░░ {blue}           │
{blue}│  {hotpink}      ██║░░██║██║░╚███║██║░╚███║██║██╔╝╚██╗██╔╝╚██╗░░░██║░░░{blue}            │
{blue}│   {hotpink}     ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░{blue}            │
{blue}│                                                                 {blue}         │
{blue}╰──────────────────{C} D E V E L O P E R  G L I T C H B Y A N N E {blue}──────────────────────────╯
 ╭────────{C}TOOL INFORMATION{B}─────────╮ {blue}   ╭────────{C}USER INFORMATION{B}─────────╮
 │ {red}•{hotpink} OWNER   : {green}Glaizel Anne    {blue}    │   {blue} │ {red}• {hotpink}STATUS   : {green}ACTIVE        {blue}     │
 │{red} • {hotpink}USES    : {green}BOOSTING       {blue}     │ {blue}   │ {red}• {hotpink}COUNTRY  :{green} PHILIPPINES    {blue}    │
 │{red} • {hotpink}NETWORK : {green}ALL NETWORK     {blue}    │   {blue} │ {red}• {hotpink}TELEGRAM : {green}@sevi02         {blue}  │
 │ {red}• {hotpink}VERSION : {green}5.0      {blue}           │{blue}    │ {red}• {hotpink}TOOLS    : {green}PAIDED       {blue}      │
 ╰─────────────────────────────────╯    ╰─────────────────────────────────╯""")
purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
import random
import string
def get_combined_data(url):
    """
    Fetch the response from the given URL and extract the `actrs` number and `post_id`.
    Combine these values and return the result.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        str: The combined string of `actrs` number and `post_id`, or an error message.
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'cache-control': "max-age=0",
        'dpr': "2",
        'viewport-width': "980",
        'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Linux\"",
        'sec-ch-ua-platform-version': "\"\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"131.0.6778.104\", \"Chromium\";v=\"131.0.6778.104\", \"Not_A Brand\";v=\"24.0.0.0\"",
        'sec-ch-prefers-color-scheme': "light",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9",
        'priority': "u=0, i",
        'Cookie': "sb=fuZTZ8Zyl9dXj5TFodlxDrGD; dpr=2; wd=980x1628; datr=fuZTZxL-gtbBjTkfeBq-VVDZ"
    }

    try:
        response = requests.get(url, headers=headers).text

        # Extract `actrs` number
        actrs_match = re.search(r'"actrs\\":\\"(\d+)\\"', response)
        actrs_number = actrs_match.group(1) if actrs_match else None

        # Extract `post_id`
        post_id_match = response.split('"post_id":"')[1].split('"')[0] if '"post_id":"' in response else None

        if actrs_number and post_id_match:
            return f"{actrs_number}_{post_id_match}"
        elif not actrs_number:
            return "actrs number not found!"
        elif not post_id_match:
            return "post_id not found!"

    except Exception as e:
        return f"An error occurred: {str(e)}"
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))

    # Randomly vary the Android OS version, device, and app version for realism
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))  # Updated range for FBAV versions
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])

    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    
    return ua_bgraph

ua_bgraph = generate_user_agent()

def AutoReact2():
    def Reaction(actor_id: str, post_id: str, react: str, token: str) -> bool:
        rui = requests.Session()
        user_agent = generate_user_agent()
        rui.headers.update({"User-Agent": user_agent})        
        feedback_id = str(base64.b64encode(f'feedback:{post_id}'.encode('utf-8')).decode('utf-8'))
        var = {
            "input": {
                "feedback_referrer": "native_newsfeed",
                "tracking": [None],
                "feedback_id": feedback_id,
                "client_mutation_id": str(uuid.uuid4()),
                "nectar_module": "newsfeed_ufi",
                "feedback_source": "native_newsfeed",
                "feedback_reaction_id": react,
                "actor_id": actor_id,
                "action_timestamp": str(time.time())[:10]
            }
        }
        data = {
            'access_token': token,
            'method': 'post',
            'pretty': False,
            'format': 'json',
            'server_timestamps': True,
            'locale': 'id_ID',
            'fb_api_req_friendly_name': 'ViewerReactionsMutation',
            'fb_api_caller_class': 'graphservice',
            'client_doc_id': '2857784093518205785115255697',
            'variables': json.dumps(var),
            'fb_api_analytics_tags': ["GraphServices"],
            'client_trace_id': str(uuid.uuid4())
        }
        pos = rui.post('https://graph.facebook.com/graphql', data=data).json()
        try:
            if react == '0':
                print(f"{green}SUCCESSFULLY REMOVED REACTION FROM {actor_id} ON {post_id}")
                return True
            elif react in str(pos):
                print(f"{green}SUCCESSFULLY REACTED WITH {actor_id} TO {post_id}")
                return True
            else:
                print(f"{red}FAILED REACTED WITH {actor_id} TO {post_id}")
                return False
        except Exception:
            print(f"{red}REACTION FAILED DUE TO AN ERROR.")
            return False

    def process_reaction(actor_id, token, post_id, react):
        global successful_reactions
        if Reaction(actor_id=actor_id, post_id=post_id, react=react, token=token):
            with counter_lock:
                if successful_reactions < react_count:
                    successful_reactions += 1

    def choose_reaction():
        linex()
        print(f"[1] LIKE")
        print(f"[2] LOVE")
        print(f"[3] HAHA")
        print(f"[4] WOW")
        print(f"[5] CARE")
        print(f"[6] SAD")
        print(f"[7] ANGRY")
        print(f"[8] REMOVE REACTION")
        linex()
        rec = input('\x1b[1;32mCHOOSE : ')
        reaction_ids = {
            '1': '1635855486666999',
            '2': '1678524932434102',
            '3': '115940658764963',
            '4': '478547315650144',
            '5': '613557422527858',
            '6': '908563459236466',
            '7': '444813342392137',
            '8': '0'
        }
        return reaction_ids.get(rec)

    def linktradio(post_link: str) -> str:
        patterns = [
            r'/posts/(\w+)',
            r'/videos/(\w+)',
            r'/groups/(\d+)/permalink/(\d+)',
            r'/reels/(\w+)',
            r'/live/(\w+)',
            r'/photos/(\w+)',
            r'/permalink/(\w+)',
            r'story_fbid=(\w+)',
            r'fbid=(\d+)'
        ]        
        for pattern in patterns:
            match = re.search(pattern, post_link)
            if match:
                if pattern == r'/groups/(\d+)/permalink/(\d+)':
                    return match.group(2)
                return match.group(1)
        
        print(f"{red}INVALID POST LINK OR FORMAT")
        return None

    def get_ids_tokens(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    def choose_type():
        clear()
        logo()
        print("[1] A REGULAR POST")
        print("[2] A GROUP POST")
        print("[3] A VIDEO POST")
        print("[4] A PHOTO POST")
        linex()
        choice = input('\x1b[1;32mCHOOSE : ')
        return choice
    actor_ids = get_ids_tokens('/sdcard/ERROR-BOOSTING/tokpid.txt')
    tokens = get_ids_tokens('/sdcard/ERROR-BOOSTING/tokp.txt')    
    choice = choose_type()    
    if choice == '1':
        linex()
        post_link = input('ENTER THE FACEBOOK POST LINK: ')
        post_id = linktradio(post_link)
    elif choice == '2':
        linex()
        post_link = input('ENTER THE FACEBOOK GROUP POST LINK: ')
        post_id = linktradio(post_link)
    elif choice == '3':
        linex()
        post_link = input('ENTER THE FACEBOOK VIDEO POST LINK: ')
        post_id = linktradio(post_link)
    elif choice == '4':
        linex()
        post_link = input('ENTER THE FACEBOOK PHOTO POST LINK: ')
        post_id = linktradio(post_link)
    else:
        print(f'''{red}INVALID CHOICE.''')
        return
    if not post_id:
        return
    react = choose_reaction()
    linex()
    if react:
        global react_count
        react_count = int(input("HOW MANY REACTIONS DO YOU WANT TO SEND? "))
        linex()
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(process_reaction, actor_id, token, post_id, react)
                for actor_id, token in zip(actor_ids, tokens)
            ][:react_count]
            for future in as_completed(futures):
                future.result()
        print(f"{green}{successful_reactions} SUCCESSFUL REACTIONS SENT! YOU'RE AWESOME!{white}")
    else:
        print(f'{red}INVALID REACTION OPTION.{white}')
        
import requests
import random
import concurrent.futures as thread
import os
import string

# Random FB version generation
fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))

# User agent string
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        
        if uid in existing_uids:
            print(f"     {yellow}[INFO] {red}ACCOUNT --> {white}{uid} {red}already exists.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            return

        response = requests.post(url, data=data).json()
        
        print(response)
        if 'access_token' in response:
            token = response['access_token']

            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")

            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: Extracted Account ─────> {uid}.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            success_count.append(uid)
        else:
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT Account ─────> {uid}.")
            print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except Exception as e:
        print(f"     \033[1;31m[ERROR]\033[0m Error extracting account: {uid}. Reason: {str(e)}\033[0m\n")


def proz(accounts_file, token_output_path, extract_type):
    """Process the accounts and extract tokens concurrently."""
    success_count = []

    # Load existing uids from the output file to avoid duplicates
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
        return

import requests
import random
import concurrent.futures as thread
import os
import string

fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def load_existing_tokens(path_file):
    """Load existing accounts or pages from the output file."""
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}  # Set of existing uids or page ids
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token
    
    if uid in existing_tokens:
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
        return

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        response = requests.post(url, data=data).json()
        
        if 'access_token' in response:
            token = response['access_token']

            # Extract Facebook Pages associated with the account token
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}Page ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")

            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")

    except Exception as e:
        print(f"[ERROR] Error extracting account: {uid}. Reason: {str(e)}")

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    pages_data = []
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f'Error: {response.text}')
            return None
        
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        
        url = data.get('paging', {}).get('next')  # Update the URL for the next request

    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
def extraction():

    clear_screen()
    jovan()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {green}CHOICE: ").strip() 
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")
def axl2():
    clear_screen()
    jovan()
    folder_path = "/sdcard/boostphere"  
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    prozc(file_path, account_file, extract_type)
def axl1():
    clear_screen()
    jovan()
    folder_path = "/sdcard/boostphere"
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    token_output_path = account_file

    proz(file_path, token_output_path, extract_type)

def cookie_token():
    clear()
    logo()
    email = input("EMAIL : ")
    password = input("PASSWORD : ") 
    linex()
    
    # Correct function call, ensuring both values are retrieved
    cookie, token = naruto(email, password)

    if cookie:
        print(f"{green}ACCESS TOKEN: {token}")
        linex()
        print(f"{green}COOKIE: {cookie}")
    else:
        print(f"{red}FAILED TO OBTAIN COOKIE AND ACCESS TOKEN.")
        
import requests
import concurrent.futures

# Placeholder functions (You need to define these)
def clear():
    pass

def logo():
    pass

def get_ids_tokens(file_path):
    """ Reads access tokens from a file. """
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: Token file not found.")
        return []

def get_profile_id(username, access_token):
    """ Gets the profile ID from username. """
    url = f"https://graph.facebook.com/v19.0/{username}"
    params = {'access_token': access_token}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('id', None)

def get_profile_username(profile_id, access_token):
    """ Gets the profile username from ID. """
    url = f"https://graph.facebook.com/v19.0/{profile_id}"
    params = {'access_token': access_token, 'fields': 'name'}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('name', 'Unknown')

def remove_facebook_follower():
    clear()
    logo()
    
    access_tokens = get_ids_tokens('/sdcard/ERROR-BOOSTING/tokp.txt')
    if not access_tokens:
        print("No access tokens found.")
        return

    profile_link = input('ENTER THE FACEBOOK PROFILE LINK TO REMOVE FOLLOWERS FROM: ').strip()
    username = profile_link.split('/')[-1]
    profile_id = get_profile_id(username, access_tokens[0])

    if not profile_id:
        print("Error: Could not retrieve profile ID. Check the profile link.")
        return

    try:
        num_to_remove = int(input('HOW MANY FOLLOWERS DO YOU WANT TO REMOVE? '))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    def remove_follower(follower_id, access_token):
        """ Removes a specific follower. """
        try:
            url = f"https://graph.facebook.com/v19.0/{follower_id}"
            params = {'access_token': access_token}
            response = requests.delete(url, params=params)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def handle_removing(access_token):
        """ Handles the removal of followers using a token. """
        nonlocal remove_count
        if remove_count >= num_to_remove:
            return
        
        profile_name = get_profile_username(profile_id, access_token)
        
        followers_url = f"https://graph.facebook.com/v19.0/{profile_id}/subscribers"
        params = {'access_token': access_token}
        response = requests.get(followers_url, params=params)

        if response.status_code != 200:
            print(f"Error fetching followers for {profile_name}.")
            return

        data = response.json()
        followers = data.get('data', [])

        for follower in followers:
            if remove_count >= num_to_remove:
                break
            follower_id = follower.get('id')
            if follower_id and remove_follower(follower_id, access_token):
                print(f"SUCCESS: Removed follower {follower_id} from {profile_name}.")
                remove_count += 1
            else:
                print(f"FAILED: Could not remove follower {follower_id} from {profile_name}.")

    remove_count = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        futures = [executor.submit(handle_removing, token) for token in access_tokens if remove_count < num_to_remove]
        concurrent.futures.wait(futures)

    print(f"SUCCESSFULLY REMOVED {remove_count} followers out of {num_to_remove} requested.")

def follow():
    clear()
    logo()
    print("[1] FOLLOW A FACEBOOK PROFILE/PAGE")
    print("[2] REMOVE FOLLOWERS FROM A FACEBOOK PROFILE/PAGE")
    print("[3] EXIT")
    
    choice = input('CHOOSE: ').strip()
    
    if choice == '1':
        follow_facebook()  # This function should be defined
    elif choice == '2':
        remove_facebook_follower()
    elif choice == '3':
        exit()
    else:
        print("INVALID OPTION.")
        follow()
def update():
    clear()
    logo()
    main_repo_path = '.'
    boosting_repo_path = './BOOSTING'
    try:
        print(f"{green}UPDATING THE MAIN REPOSITORY...")
        subprocess.run(['git', 'pull'], cwd=main_repo_path, check=True)
        print(f"{white}MAIN REPOSITORY UPDATED SUCCESSFULLY.")
    except subprocess.CalledProcessError as e:
        print(f"{red}ERROR OCCURRED WHILE UPDATING THE MAIN REPOSITORY: {e}")
    if not os.path.exists(boosting_repo_path):
        print(f"{red}BOOSTING REPOSITORY NOT FOUND LOCALLY. PLEASE CLONE IT FIRST.")
        return
    try:
        print(f"{green}PULLING THE LATEST CHANGES FROM THE BOOSTING REPOSITORY...")
        subprocess.run(['git', 'pull'], cwd=boosting_repo_path, check=True)
        print(f"{green}BOOSTING REPOSITORY UPDATED SUCCESSFULLY.")
    except subprocess.CalledProcessError as e:
        print(f"{red}ERROR OCCURRED WHILE UPDATING THE BOOSTING REPOSITORY: {e}")
       
def follow():
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO FOLLOW:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    user_id = input(f'''{yellow}  Enter target UID: {green}''')
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of follows, limit is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available followers.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        auto_follow_url = f'''https://graph.facebook.com/v19.0/{user_id}/subscribers'''
        time.sleep(1)
        headers = {
            'Authorization': f'''Bearer {access_token}''',
            'user-agent': W_ueragnt()
        }
        response = requests.post(auto_follow_url, headers=headers)
        if response.ok:
            success_count += 1
            print(f'''{green}  FOLLOWER {i + 1} ---> Successfully Followed!''')
        else:
            failure_count += 1
            print(f'''{red}  FOLLOWER {i + 1} ---> Failed to Follow!''')
    line()
    print(f'''{yellow}  TOTAL : \n''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')
    
import os
import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor


def gettokesz(file_path):
    """Read tokens from the file and return a list of tokens."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip().split('|')[1] for line in lines if '|' in line]


class fbpost:
    def __init__(self, link):
        self.link = link

    def shir(self, token):
        """Shares a post on the user's feed with 'Only Me' privacy."""
        url = "https://graph.facebook.com/me/feed"
        payload = {
            'link': self.link,
            'published': '1',
            'privacy': '{"value":"EVERYONE"}',
            'access_token': token
        }

        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print("Successfully Shared")
                return True
            else:
                pass
                return False
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return False


def sgtz(link, file_path, num_shares):
    start_all = time.time()

    tokens = gettokesz(file_path)
    if len(tokens) < num_shares:
        print("Not enough tokens to meet the requested number of shares.")
        return

    def worker(token):
        fb_poster = fbpost(link)
        fb_poster.shir(token)

    with ThreadPoolExecutor(max_workers=20) as executor:
        for token in tokens[:num_shares]:
            executor.submit(worker, token)

    end_all = time.time()
    print(f"\nSharing started at: {time.ctime(start_all)}")
    print(f"Sharing ended at: {time.ctime(end_all)}")
    print(f"Total duration: {end_all - start_all:.2f} seconds")


def ttsu(*file_paths):
    """Count the number of lines in each provided file."""
    counts = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                counts.append(sum(1 for line in file if line.strip()))
        except FileNotFoundError:
            counts.append(0)
    return counts


def tts():
    """Ensure directories and files exist."""
    file_paths = [
        '/sdcard/boostphere/FRAACCOUNT.txt',
        '/sdcard/boostphere/FRAPAGES.txt',
        '/sdcard/boostphere/RPWACCOUNT.txt',
        '/sdcard/boostphere/RPWPAGES.txt',
    ]

    for file_path in file_paths:
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                pass  # Create an empty file
            print(f"Created file: {file_path}")


def public():
    print("CHOOSE TYPE OF ACCOUNTS TO AUTO SHARE:")
    print("[1] FRA ACCOUNT")
    print("[2] FRA PAGES")
    print("[3] RPW ACCOUNT")
    print("[4] RPW PAGES")
    print("[0] EXIT")
    choice = input("Choice: ")

    file_map = {
        '1': '/sdcard/boostphere/FRAACCOUNT.txt',
        '2': '/sdcard/boostphere/FRAPAGES.txt',
        '3': '/sdcard/boostphere/RPWACCOUNT.txt',
        '4': '/sdcard/boostphere/RPWPAGES.txt'
    }

    file_path = file_map.get(choice)
    if not file_path:
        print("Invalid choice. Exiting.")
        return

    a = input("Enter the post ID to share: ")
    post_id = get_combined_data(a)
    num_shares = int(input("Limit: "))
    link = f"https://www.facebook.com/{post_id}"

    sgtz(link, file_path, num_shares)


def pub():
    tts()
    fra_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    fra_pages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpw_file = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpw_pages_file = '/sdcard/boostphere/RPWPAGES.txt'

    total_accounts, total_pages, rpw_accounts, rpw_pages = ttsu(
        fra_file, fra_pages_file, rpw_file, rpw_pages_file
    )
    jovan()
    print(f"""                 {hotpink} ACCOUNT OVERVIEWS {G} [ ACCOUNT / PAGE ]
          
                            {yellow}FRA ACCOUNT{yellow} : {green}{total_accounts}
                            {yellow}FRA PAGES  {yellow} : {green}{total_pages}
                            {yellow}RPW ACCOUNT{yellow} : {green}{ rpw_accounts}
                            {yellow}RPW PAGES  {yellow} : {green}{rpw_pages}
      {yellow}───────────────────────────────────────────────────────────────\033[0m[0m""")
    print(f"     {blue}[1] {yellow}EXTRACT ACCOUNT")
    print(f"     {blue}[2] {yellow}AUTO SHARE ")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f'    {yellow}Enter Choice: ')

    if choice == '2':
        public()






# Function to clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




def extraction():

    clear_screen()
    jovan()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {green}CHOICE: ").strip() 
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"     {red}INVALID CHOICE")
def main():
    open('/sdcard/boostphere/FRAACCOUNT.txt', 'a').write('')
    open('/sdcard/boostphere/FRAPAGES.txt', 'a').write('')
    open('/sdcard/boostphere/RPWACCOUNT.txt', 'a').write('')
    open('/sdcard/boostphere/RPWACCOUNT.txt', 'a').write('')
    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages = '/sdcard/boostphere/RPWPAGES.txt'
    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts,rpwpages)
    jovan()
    print(f""" {blue}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m""")
    print(f""" {blue}┃                        {hotpink} ACCOUNT STORAGE               {blue}                  ┃""")
    print(f""" {blue}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
                               {green} ACCOUNT{yellow} : {green}{total_accounts} """)

                            
    print(f"{blue}┏━━━━━━━━━━━━━━━━━━━━━━ {green}A C C O U N T S T O R E{blue} ━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"{blue}┃  {green}[01] {hotpink} STORE ACCOUNT                        {yellow}- {green}[ 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 ]   {blue}             ┃")
    print(f"{blue}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ")
    print(f"{blue}┏━━━━━━━━━━━━━━━━━━━━━━ {green}T O O L  S E R V I C E S{blue} ━━━━━━━━━━━━━━━━━━━━━━━━━━┓")  
    print(f"{blue}┃  {green}[02]  {hotpink}𝐕𝐀𝐋𝐈𝐃𝐀𝐓𝐄 {green}ACCOUNT                     {yellow}- {green}[ 𝐓𝐎𝐊𝐄𝐍 ]     {blue}             ┃")
    print(f"{blue}┃  {green}[03]  {hotpink}𝐀𝐔𝐓𝐎 {green}𝐒𝐇𝐀𝐑𝐄 𝐕1                        {yellow}- {green}[ BOT SHARE ] {blue}             ┃") 
    print(f"{blue}┃  {green}[04]  {hotpink}𝐀𝐔𝐓𝐎 {green}𝐒𝐇𝐀𝐑𝐄 𝐕2                        {yellow}- {green}[ WITH NOTIFICATION ]{blue}      ┃") 
    print(f"{blue}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print(f"{blue}┏━━━━━━━━━━━━━━━━━━━━━━ {green}A C C O U N T  R E S E T{blue} ━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"{blue}┃  {green}[05]{hotpink}  𝐑𝐄𝐒𝐄𝐓 𝐓𝐎𝐎𝐋𝐒                          {yellow}- {green}[ 𝐏𝐀𝐆𝐄 𝐎𝐑 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 ]      {blue}  ┃")
    print(f"{blue}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
    choice = input(f"     {green} CHOICE💎 : ").strip()         
#C:\Users\Dont touch my pc\Desktop\OPENSOURCE\sy.py
    if choice == '1':
        extraction()
    if choice == '2':
        check()
    if choice == '3':
        main2()
    if choice == '4':
        pub()
    if choice == '5':
    	clear_text_files()
    else:
        print("Invalid choice, exiting.")






if __name__ == "__main__":
       main()
   
    
    
    