import requests
from bs4 import BeautifulSoup

import os
import re
import string
import sys
import urllib.error
import urllib.parse
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from fake_useragent import UserAgent


import threading
import queue
import time

# Define the base URL of the faculty directory page
base_url = 'https://www.sjtu.edu.cn'

def valid_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    s = ''.join(c for c in s if c in valid_chars)
    return s

def add_page_to_folder(page, content):  
    index_filename = 'index.txt'  
    folder = 'html' 
    filename = valid_filename(page)  
    index = open(index_filename, 'a')
    index.write(str(page) + '\t' + str(filename) + '\n')
    index.close()
    if not os.path.exists(folder):  
        os.mkdir(folder)
    f = open(os.path.join(folder, filename), 'w')
    f.write(str(content))
    f.close()


def get_page(page):
    content = ''
    try:
        req = urllib.request.Request(page)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0")
        content = urllib.request.urlopen(req,timeout = 1).read()
    except:
        pass
    return content.decode('utf-8')

option = webdriver.ChromeOptions()
option.add_argument('user-agent: "Mozilla/5.0 (X11; Linux x86_64)\
    AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36"')

ua = UserAgent().random
print(ua)

option.add_argument('headless')

driver = webdriver.Chrome(options=option)
driver.get(base_url)
result= driver.find_element(By.CLASS_NAME, 'TopLine')
result.click()

selenium_page = driver.page_source
driver.quit()
soup = BeautifulSoup(selenium_page, 'html.parser')

print(selenium_page[:10000])

# content = get_page(base_url)
# print(content[:10000])

# soup = BeautifulSoup(content[:10000], 'html.parser')

# soup = BeautifulSoup(response.text, 'html.parser')
