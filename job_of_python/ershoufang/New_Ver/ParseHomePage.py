import bs4
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import time
import pymysql
import json
import random

def ParseHomePage(content):
    soup = BeautifulSoup(content, 'lxml')
    a_herf = soup.find_all('a', class_="title")
    herf_list=[]
    for a in a_herf:
        herf_list.append(a['href'])

    return herf_list
    #解析每个a包含的网页











