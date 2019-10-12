import bs4
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import time
import pymysql
import json
import random
import GetLocation
import Get_Distance
import getDistance
import Get_Subway_latlng

import start


def get_community_name(soup):
 div=soup.find('div',class_='communityName')
 realname = div.find('a',class_='info')
 community_name =realname.string
 return community_name
def get_location(soup):
    div_area = soup.find('div', class_="aroundInfo")
    area = div_area.find('span', class_='info')
    area_information = area.text
    s = "".join(area.text.split())
    return s
def get_unit_price(soup):


    span_unit_value = soup.find('span', class_='unitPriceValue')
    unit_price = span_unit_value.text
    return unit_price
def get_total_price(soup):
    div_price = soup.find('div', class_='price')
    span_total_price = div_price.find('span', class_='total')
    total_price = span_total_price.string + '万人民币'
    return total_price
def get_lngAndlat(community_name):
    return GetLocation.get_location(community_name)
def get_subway(lng,lat,l_list):


   d= getDistance.getdistance(l_list,lng,lat)


   return d
def get_G(zone,city,name):
    location1=Get_Distance.goverment_location(zone,city)
    location2=location2= GetLocation.get_location(name)
    return Get_Distance.getDistance(location1[1],location1[0], location2[1],location2[0])
def get_year(soup):
    div_x = soup.find('div', class_='area')
    div_y = div_x.find('div', class_='subInfo')
    year = (div_y.text)[0:4]
    return year
def ParseEachCommunity(content,l_list):
    the_whole_information= {
        '小区名称': '',
        '小区地点': '',
        '总价': '',
        '单价': '',
        '房屋户型': '',
        '所在楼层': '',
        '建筑面积': '',
        '户型结构': '',
        '套内面积': '',
        '建筑类型': '',
        '房屋朝向': '',
        '建筑结构': '',
        '装修情况': '',
        '梯户比例': '',
        '配备电梯': '',
        '产权年限': '',
        '坐标':{'lng':'','lat':''},
        '地铁距离':'',
        '政府距离':'',
        '建筑年代':''


        }
    soup = BeautifulSoup(content, "lxml")
    the_whole_information['小区名称']=get_community_name(soup)
    the_whole_information['坐标']['lng']=get_lngAndlat(the_whole_information['小区名称'])[0]
    the_whole_information['坐标']['lat']=get_lngAndlat(the_whole_information['小区名称'])[1]
    the_whole_information['建筑年代']=get_year(soup)
    try:
     the_whole_information['地铁距离']=get_subway(the_whole_information['坐标']['lng'],the_whole_information['坐标']['lat'],l_list)
    except TypeError:the_whole_information['地铁距离']='未知'
    the_whole_information['小区地点'] = get_location(soup)
    try:
     the_whole_information['政府距离'] =get_G(the_whole_information['小区地点'], '南京', the_whole_information['小区名称'])
    except TypeError:the_whole_information['政府距离']='未知'
    the_whole_information['总价']=get_total_price(soup)
    the_whole_information['单价']=get_unit_price(soup)
    div_house_content = soup.find('div', class_='base')
    house_info_dir = {}
    for i in div_house_content.find_all('li'):
        # print(i)
        string = str(i)
        pattern = re.compile(r'<li><span class="label">(.*?)</span>.*?</li>', re.S)
        result_type = pattern.findall(string)
        pattern = re.compile(r'<li>.*?</span>(.*?)</li>', re.S)
        result_content = pattern.findall(string)
        di = {
            result_type[0]: result_content[0]
        }
        house_info_dir.update(di)
    if '房屋户型' in house_info_dir:the_whole_information['房屋户型'] = house_info_dir['房屋户型']
    else: the_whole_information['房屋户型']='暂无数据'

    if '所在楼层' in house_info_dir:the_whole_information['所在楼层'] = house_info_dir['所在楼层']
    else: the_whole_information['所在楼层']='暂无数据'

    if '建筑面积' in house_info_dir:the_whole_information['建筑面积'] = house_info_dir['建筑面积']
    else: the_whole_information['建筑面积']='暂无数据'


    if '户型结构' in  house_info_dir:the_whole_information['户型结构'] = house_info_dir['户型结构']
    else :the_whole_information['户型结构']='暂无数据'

    if '套内面积' in house_info_dir:the_whole_information['套内面积'] = house_info_dir['套内面积']
    else: the_whole_information['套内面积'] = '暂无数据'

    if '建筑类型' in house_info_dir:the_whole_information['建筑类型'] = house_info_dir['建筑类型']
    else: the_whole_information['建筑类型']='暂无数据'

    if '房屋朝向' in house_info_dir:the_whole_information['房屋朝向'] = house_info_dir['房屋朝向']
    else: the_whole_information['房屋朝向']='暂无数据'

    if '建筑结构' in house_info_dir:the_whole_information['建筑结构'] = house_info_dir['建筑结构']
    else: the_whole_information['建筑结构']='暂无数据'

    if '装修情况' in house_info_dir:the_whole_information['装修情况'] = house_info_dir['装修情况']
    else: the_whole_information['装修情况'] = '暂无数据'

    if '梯户比例' in house_info_dir:the_whole_information['梯户比例'] = house_info_dir['梯户比例']
    else: the_whole_information['梯户比例']='暂无数据'

    if '配备电梯' in house_info_dir:the_whole_information['配备电梯'] = house_info_dir['配备电梯']
    else: the_whole_information['配备电梯']='暂无数据'

    if '产权年限' in house_info_dir:the_whole_information['产权年限'] = house_info_dir['产权年限']
    else: the_whole_information['产权年限']='暂无数据'

    house_intro_dir = {


    }
    #清洗
    if int(the_whole_information['政府距离']) > 20000: the_whole_information['政府距离'] = '未知'
    if float(the_whole_information['地铁距离']) > 10000: the_whole_information['地铁距离'] = '未知'
    if type(the_whole_information['政府距离'])==None:the_whole_information['地铁距离']='未知'
    if the_whole_information['坐标']['lng']==0:the_whole_information['坐标']['lng']='未知'
    if the_whole_information['坐标']['lat']==0:the_whole_information['坐标']['lat']='未知'
    return the_whole_information




