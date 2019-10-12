from bs4 import BeautifulSoup
import requests
import json
#
class html(object):
    soup=None
    address=''
    def __init__(self,address):

        url_0='http://api.map.baidu.com/geocoder/v2/?address='
        ak='ejgVqGQaT7jtEGrCHarG455D1SVQIZBU'
        self.address=address
        city='南京'
        baiduAPI_url=url_0+address+'&city='+city+'&output=json&pois=1&ak='+ ak
        header = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

        }

        html = requests.get(baiduAPI_url,headers=header).content
        self.soup= BeautifulSoup(html,'lxml')
        #获取到的html {"status":0,"result":{"location":{"lng":118.73472389538607,"lat":32.15347772467399},"precise":0,"confidence":60,"comprehension":100,"level":"UNKNOWN"}}
    def get_location(self):
        response = self.soup.select('p')[0].get_text()
        response=json.loads(response)
        try:
            lng= response['result']['location']['lng']
            lat= response['result']['location']['lat']
            #print(type(lng),type(lat))
            l=[lng,lat]


        except BaseException:

            return [0,0]
        else:return l
        #print(type(response))


def main():
    h=html('天润城第十街区')
    h.get_location()



if __name__ == '__main__':
    main()

