from bs4 import BeautifulSoup
from urllib import request
import re
import pandas as pd
import numpy as np
import urllib.parse as urp
from xml.etree import ElementTree
import time
import requests
import json
import math
EARTH_REDIUS=6378.137
def get_location_subway(name,city):
    my_ak='ejgVqGQaT7jtEGrCHarG455D1SVQIZBU'
    tag=urp.quote('地铁站')# 编码
    query=urp.quote(name)
    city=urp.quote(city)
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    try:
        url='http://api.map.baidu.com/place/v2/search?query='+query+'&tag='+tag+'&region='+city+'&output=json&ak='+my_ak
        print(url)
        html = requests.get(url=url, headers=header).content.decode()
        #print(html)
        soup = BeautifulSoup(html, 'lxml')
        response=soup.select('p')[0].get_text()
        #print(response)
        response=json.loads(response)
        #print(type(response))
        #print(response)
        try:
            subway_lng=response["results"][0]['location']['lng']
            subway_lat=response["results"][0]['location']['lat']
            return subway_lng,subway_lat

        except:
            return 0,0


    except:
        return 0,0

    #http://api.map.baidu.com/geocoder/v2/?address=%E5%85%AD%E5%90%88%E5%8C%BA%E6%94%BF%E5%BA%9C&city=%E5%8D%97%E4%BA%AC&output=json&pois=1&ak=ejgVqGQaT7jtEGrCHarG455D1SVQIZBU
def goverment_location(zone,city):
    url_0 = 'http://api.map.baidu.com/geocoder/v2/?address='
    ak = 'ejgVqGQaT7jtEGrCHarG455D1SVQIZBU'
    baiduAPI_url = url_0 + zone + '区政府&city=' + city + '&output=json&pois=1&ak=' + ak
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    html = requests.get(baiduAPI_url, headers=header).content.decode()
    soup = BeautifulSoup(html, 'lxml')
    response = soup.select('p')[0].get_text()
    response=json.loads(response)
    try:
            lng= response['result']['location']['lng']
            lat= response['result']['location']['lat']
            #print(type(lng),type(lat))



    except BaseException:

            return [0,0]
    else:return [lng,lat]

#print(list(get_location_subway('天润城地铁站','南京')))


def rad(d):
    return d*math.pi/180.0


def getDistance(lat1,lng1,lat2,lng2):
    radlat1=rad(lat1)
    radlat2=rad(lat2)
    a=radlat1-radlat2
    b=rad(lng1)-rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radlat1) * math.cos(radlat1) * math.pow(math.sin(b / 2), 2)))
    ss = s * EARTH_REDIUS*10**3
    return ss
