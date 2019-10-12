import bs4
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import time
import pymysql
import json
import random
import Url_List
import Build_Request
import ParseHomePage
import Parse_Each_Community
import GetLocation
import Get_Subway_latlng
import Data_Analysis
import threading
from queue import Queue
import requests
from lxml import etree
import DataBase_Connect

id_=448
page=16
url='https://nj.lianjia.com/ershoufang/pg'
url_list=Url_List.get_Page_list(url)
print(url_list)
#test
dbconn=DataBase_Connect.open_connect()
cursor=dbconn.cursor()
l_list=Get_Subway_latlng.get_subway_site(cursor)

def p(page,l_list,u):
    print("-------------开始爬取第%s页--------------" % page)
    page += 1
    content_1 = Build_Request.build_request(u)
    a_href = ParseHomePage.ParseHomePage(content_1)

    # print(a_href)每一页都有很多个a_href
    for i in a_href:
        content_2 = Build_Request.build_request(i)
        # with open('F:\\python\\job_of_python\\ershoufang\\New_Ver\\pg.html', 'wb') as fp:
        # fp.write(content_2)

        inf = Parse_Each_Community.ParseEachCommunity(content_2, l_list)

