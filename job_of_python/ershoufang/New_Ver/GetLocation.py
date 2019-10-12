from bs4 import BeautifulSoup
import requests
import json


def get_location(address):
    soup = None

    url_0 = 'http://api.map.baidu.com/geocoder/v2/?address='
    ak = 'ejgVqGQaT7jtEGrCHarG455D1SVQIZBU'
    ak2='5zgXz4yXU2xskMGlaWnUDKSnmlS4V3Fs'
    city = '南京'

    baiduAPI_url = url_0 + str(address) + '&city=' + city + '&output=json&pois=1&ak=' + ak
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    html = requests.get(baiduAPI_url, headers=header).content
    soup = BeautifulSoup(html, 'lxml')
    response = soup.select('p')[0].get_text()
    response = json.loads(response)
    try:
        lng = response['result']['location']['lng']
        lat = response['result']['location']['lat']
        # print(type(lng),type(lat))
        l = [lng, lat]
        return l


    except BaseException:

        return [0, 0]


