import bs4
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import time
import pymysql
import json
import random
import urllib3
def build_request(parse_url):
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    request = urllib.request.Request(url=parse_url, headers=header)
    content = urllib.request.urlopen(request).read().decode()
    #  with open('pg_%s.html'% page,'wb') as fp :
    #  fp.write(content)

    return content
