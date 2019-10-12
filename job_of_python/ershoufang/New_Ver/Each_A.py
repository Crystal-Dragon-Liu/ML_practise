import bs4
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import time
import pymysql
import json
import random
import Build_Request
def parseA(a_href):
  content =Build_Request.build_request(a_href)
  return content


