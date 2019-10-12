
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
from multiprocessing import Process
import threading
import multiprocessing

multiprocessing.freeze_support()
def p(a_href):


   content_2=Build_Request.build_request(a_href)
 #with open('F:\\python\\job_of_python\\ershoufang\\New_Ver\\pg.html', 'wb') as fp:
  #fp.write(content_2)

   inf=Parse_Each_Community.ParseEachCommunity(content_2,l_list)
   print(inf['小区名称']+" lng:"+str(inf['坐标']['lng'])+" lat:"+str(inf['坐标']['lat']))
   time.sleep(random.randint(1, 3))
 #print(inf)
   #a=GetLocation.get_location('南农大小区')
 #print(a)
 #url='https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=walk&c=315&sn=1$$a1c44059697d43599222e0c2$$13219934,3745840$$%E8%8C%B6%E8%8A%B1%E9%87%8C%E5%B0%8F%E5%8C%BA$$0$$$$&en=1$$14e62cf755192ee8dbd891ed$$13219843,3745770$$%E4%BA%91%E9%94%A6%E8%B7%AF$$0$$$$&sc=315&ec=315&pn=0&rn=5&version=6&run=0&spath_type=1&da_src=&da_src=pcmappg.searchBox.button&tn=B_NORMAL_MAP&nn=0&auth=2NO1ef%3DGBSAVxfOTNFgJX1IyQYH%40cQ41uxHHHVNxLLRt1qo6DF%3D%3DCy1uVt1GgvPUDZYOYIZuVt1cv3uxztnGg4%40PBFQE300b0z8yPWv3GuxNtg3yw8mdwJL4ORUY9cf0IcEWe1GD8zv7u%40ZPuVteuztghxehwzJJJWPWVVGvrvUU2KJGs99XvMF&u_loc=13236676,3729221&ie=utf-8&l=19&b=(13219384.125,3745545.2499999995;13220343.125,3746049.7499999995)&t=1555071686471'





if __name__ == '__main__':
    url = 'https://nj.lianjia.com/ershoufang/pg'
    url_list = Url_List.get_Page_list(url)
    # test
    dbconn = DataBase_Connect.open_connect()
    cursor = dbconn.cursor()
    l_list = Get_Subway_latlng.get_subway_site(cursor)

    content_1 = Build_Request.build_request(url_list[0])
    a_href = ParseHomePage.ParseHomePage(content_1)
    pool=multiprocessing.Pool(processes=30)
    for i in a_href:
        pool.apply_async(p,(i,))
    pool.join()
    pool.close()
    pool.join()



    DataBase_Connect.close_connect(dbconn)
