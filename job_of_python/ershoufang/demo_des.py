import bs4
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import time
import pymysql
import json
import random
class second_hand_house(object):
    url = 'https://nj.lianjia.com/ershoufang/pg'
    #url = 'https://nj.lianjia.com/ershoufang/'
    data_sum = 2246

    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page

    def database_connectionAnd_create(self):
        mysql_host = 'the_second_house'
        mysql_name = 'localhost'
        mysql_user = 'root'
        mysql_port = 3306
        mysql_password = '1025058706zfr'
        dbconn = pymysql.connect(mysql_name, mysql_user, mysql_password, mysql_host, charset='utf8')
        cursor = dbconn.cursor()
        # cursor.execute('create table student(id int PRIMARY KEY NOT NULL,coummunity_name varchar(50),location varchar(50),total_price float(5,2),unit_price float(5,2),house_type varchar(50),floor varchar(20))')
        cursor.execute(
            'create table the_second_house_info_des(id int PRIMARY KEY NOT NULL,coummunity_name varchar(50),location varchar(50),total_price varchar(50),unit_price varchar(50),house_type varchar(50),floor varchar(20),construction_area varchar(20),house_structure varchar(50),inner_area varchar(20),building_type varchar(20),house_orientation varchar(20),building_structure varchar(20),renovation varchar(20),ladder_ratio varchar(20),elevator varchar(20),year_of_property_rights varchar(20),year varchar(20))')
        cursor.close()
        dbconn.commit()
        dbconn.close()
    def database_connectionAnd_insert(self, id_, community_name, location, total_price, unit_price, house_type, floor,
                                      construction_area, house_structure, inner_area, building_type, house_orientation,
                                      building_structure, renovation, ladder_ratio, elevator, year_of_property_rights,year):

        mysql_host = 'the_second_house'
        mysql_name = 'localhost'
        mysql_user = 'root'
        mysql_port = 3306
        mysql_password = '1025058706zfr'
        dbconn = pymysql.connect(mysql_name, mysql_user, mysql_password, mysql_host, charset='utf8')
        cursor = dbconn.cursor()
        cursor.execute(
            'insert into the_second_house_info_des values(' + id_ + ',"' + community_name + '","' + location + '","' + total_price + '","' + unit_price + '","' + house_type + '","' + floor + '","' + construction_area + '","' + house_structure + '","' + inner_area + '","' + building_type + '","' + house_orientation + '","' + building_structure + '","' + renovation + '","' + ladder_ratio + '","' + elevator + '","' + year_of_property_rights + '","'+year+'")')
        cursor.close()
        dbconn.commit()
        dbconn.close()

    def database_insert(self):
        pass

    def parse_content_detail(self, content):
        '''
        with open('contain.html','wb') as fp:
          fp.write(content)

        '''

        global sum
        the_whole_information = {
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
            # '户型区间信息': {'客厅': '', '卧室A': '', '卧室B': '', '卧室C': '', '厨房': '', '卫生间': '', '阳台': '', }
            '建筑年代':''

        }
        soup = BeautifulSoup(content, "lxml")






        # print(type(soup))


        # 小区名称

        div_community_name = soup.find('div', class_='communityName')
        #print(div_community_name)

        realname = div_community_name.find('a', class_='info')
        community_name = realname.string





        # print(community_name)
        the_whole_information['小区名称'] = community_name

        div_area = soup.find('div', class_="aroundInfo")

        # 小区地点

        # print(div_area)
        area = div_area.find('span', class_='info')
        area_information = area.text
        # print(area.text)
        # print(area)
        s = "".join(area.text.split())
        # print(s)

        the_whole_information['小区地点'] = s

        '''
        area_detail = area.find_all('a',target='_blank')
    
        area_information = ''
        for label in range(0,len(area_detail)):
            area_information=area_information+' '+area_detail[label].string
        print(area_information)
    
        '''

        # 房价

        div_price = soup.find('div', class_='price')
        # print(div_price)
        span_total_price = div_price.find('span', class_='total')
        total_price = span_total_price.string + '万人民币'
        # print(total_price)
        span_unit_value = soup.find('span', class_='unitPriceValue')
        unit_price = span_unit_value.text
        # print(unit_price)

        the_whole_information['总价'] = total_price
        the_whole_information['单价'] = unit_price

        # 房子信息

        div_house_content = soup.find('div', class_='base')
        house_info_dir = {
        }
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
            # print(type(result_content[0]))
        # print(house_info_dir)

        # div_intro = soup.find('div',class_='introContent showbasemore')
        # print(div_intro)
        # the_whole_information['']
        # if '' in house_info_dir:
        # else: the_whole_information['']='暂无数据'

        # 年份
        div_tranaction = soup.find('div', class_='transaction')
        div_dd = div_tranaction.find_all('li')
        # print(div_dd)
        # print(div_tranaction)
        # test='<div class="introContent">.*<ul><li><span class="label">挂牌时间</span><span>(.*?)</span></li>.*</ul>.*</div>'
        div__ = div_dd[0].find_all('span')
        #print(div__[1].text)
            # print(type(div__[1].text))


        #建筑年份
        div_x=soup.find('div',class_='area')
        div_y=div_x.find('div',class_='subInfo')
        year=(div_y.text)[0:4]
        the_whole_information['建筑年代']=year



        if '房屋户型' in house_info_dir:
            the_whole_information['房屋户型'] = house_info_dir['房屋户型']
        else:
            the_whole_information['房屋户型'] = '暂无数据'

        if '所在楼层' in house_info_dir:
            the_whole_information['所在楼层'] = house_info_dir['所在楼层']
        else:
            the_whole_information['所在楼层'] = '暂无数据'

        if '建筑面积' in house_info_dir:
            the_whole_information['建筑面积'] = house_info_dir['建筑面积']
        else:
            the_whole_information['建筑面积'] = '暂无数据'

        if '户型结构' in house_info_dir:
            the_whole_information['户型结构'] = house_info_dir['户型结构']
        else:
            the_whole_information['户型结构'] = '暂无数据'

        if '套内面积' in house_info_dir:
            the_whole_information['套内面积'] = house_info_dir['套内面积']
        else:
            the_whole_information['套内面积'] = '暂无数据'

        if '建筑类型' in house_info_dir:
            the_whole_information['建筑类型'] = house_info_dir['建筑类型']
        else:
            the_whole_information['建筑类型'] = '暂无数据'

        if '房屋朝向' in house_info_dir:
            the_whole_information['房屋朝向'] = house_info_dir['房屋朝向']
        else:
            the_whole_information['房屋朝向'] = '暂无数据'

        if '建筑结构' in house_info_dir:
            the_whole_information['建筑结构'] = house_info_dir['建筑结构']
        else:
            the_whole_information['建筑结构'] = '暂无数据'

        if '装修情况' in house_info_dir:
            the_whole_information['装修情况'] = house_info_dir['装修情况']
        else:
            the_whole_information['装修情况'] = '暂无数据'

        if '梯户比例' in house_info_dir:
            the_whole_information['梯户比例'] = house_info_dir['梯户比例']
        else:
            the_whole_information['梯户比例'] = '暂无数据'

        if '配备电梯' in house_info_dir:
            the_whole_information['配备电梯'] = house_info_dir['配备电梯']
        else:
            the_whole_information['配备电梯'] = '暂无数据'

        if '产权年限' in house_info_dir:
            the_whole_information['产权年限'] = house_info_dir['产权年限']
        else:
            the_whole_information['产权年限'] = '暂无数据'

        house_intro_dir = {

        }

        div_base = soup.find_all('div', class_='baseattribute clear')
        '''
            for i in div_base:
            string = str(i)
            #print(i)
            pattern = re.compile(r'<div class="name">(.*?)</div>',re.S)
            result_type = pattern.findall(string)
            print(result_type[0])
            pattern = re.compile(r'<div class="content">(.*?)</div>',re.S)
            result_content = pattern.findall(string)
            re_left = result_content[0].lstrip()
            re_right = re_left.rstrip()
    
    
            house_in_dir={
                result_type[0]:re_right
    
            }
            house_intro_dir.update(house_in_dir)
            #print(house_intro_dir[result_type[0]])
    
        '''
        # print(the_whole_information['小区名称'])
        # print(house_info_dir['户型结构'])

        # 户型分间
        '''
         div_des = soup.find('div',class_='des')
        if len(div_des):
         div_apartment = div_des.find_all('div',class_='list')
         #print(div_apartment[0])
         #print(div_apartment)
         div_list = div_apartment[0].find_all('div',class_='row')
         dir_row = {
    
    
         }
         #print(div_list)
    
         room_list = []
              for i in div_list:
              div_row = i.find_all('div',class_='col')
              #print(div_row)
    
              room_list_1 = []
              #这里有问题！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
              for j in div_row:
    
                string = str(j)
                pattern =re.compile(r'<div class="col">(.*?)</div>',re.S)
                re_row = pattern.findall(string)
                #print(re_row[0])
                room_list_1.append(re_row[0])
              room_list.append(room_list_1)
                   for i in div_list:
              div_row = i.find_all('div',class_='col')
              #print(div_row)
    
              room_list_1 = []
              #这里有问题！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
              for j in div_row:
    
                string = str(j)
                pattern =re.compile(r'<div class="col">(.*?)</div>',re.S)
                re_row = pattern.findall(string)
                #print(re_row[0])
                room_list_1.append(re_row[0])
              room_list.append(room_list_1)
         #print(room_list)
         #输入信息
         '''
        '''the_whole_information['户型区间信息']['客厅']='面积：'+room_list[0][1]+' 方向 :'+room_list[0][2]+'窗户：'+room_list[0][3]
         the_whole_information['户型区间信息']['卧室A'] = '面积：' + room_list[1][1] + ' 方向 :' + room_list[1][2] + '窗户：' + room_list[1][3]
         the_whole_information['户型区间信息']['卧室B'] = '面积：' + room_list[2][1] + ' 方向 :' + room_list[2][2] + '窗户：' + room_list[2][3]
         the_whole_information['户型区间信息']['卧室C'] = '面积：' + room_list[3][1] + ' 方向 :' + room_list[3][2] + '窗户：' + room_list[3][3]
         the_whole_information['户型区间信息']['厨房'] = '面积：' + room_list[4][1] + ' 方向 :' + room_list[4][2] + '窗户：' + room_list[4][3]
         the_whole_information['户型区间信息']['卫生间'] = '面积：' + room_list[5][1] + ' 方向 :' + room_list[5][2] + '窗户：' + room_list[5][3]
         the_whole_information['户型区间信息']['阳台'] = '面积：' + room_list[6][1] + ' 方向 :' + room_list[6][2] + '窗户：' + room_list[6][3]
    
        '''

        '''
         #---------------------------------------------------------将roomlist内容装入the_whole_information里--------------------------------------------------------------------------
    
    
    
    
    
    
        else:
            room_list=['无户型分间信息']
            the_whole_information['户间区间信息']=room_list[0]
            #print(room_list[0])
        '''

        # print(type(the_whole_information))
        print("------------------------------------------正在爬取" + the_whole_information["小区名称"] + "小区某二手房的信息----------------------------------------------")
        #print(the_whole_information)

        # print(type(str(the_whole_information['小区名称'])))
        #self.database_connectionAnd_create()


        self.database_connectionAnd_insert(str(self.data_sum), str(the_whole_information['小区名称']),
                                           str(the_whole_information['小区地点']), str(the_whole_information['总价']),
                                           str(the_whole_information['单价']), str(the_whole_information['房屋户型']),
                                           str(the_whole_information['所在楼层']), str(the_whole_information['建筑面积']),
                                           str(the_whole_information['户型结构']), str(the_whole_information['套内面积']),
                                           str(the_whole_information['建筑类型']), str(the_whole_information['房屋朝向']),
                                           str(the_whole_information['建筑结构']), str(the_whole_information['装修情况']),
                                           str(the_whole_information['梯户比例']), str(the_whole_information['配备电梯']),
                                           str(the_whole_information['产权年限']),str(the_whole_information['建筑年代']))
        self.data_sum += 1
        






        # 交易属性

        '''
    
        div_house_trade = soup.find('div',class_='transaction')
        house_trade_dir={
    
    
    
        }
        div_house_trade_deep = div_house_trade.find('div',class_='content')
    
        for i in div_house_trade_deep.find_all('li'):
            print(i)
            string = str(i)
            pattern = re.compile(r'<span class="label">(.*?)</span>',re.S)
            result_attribute = pattern.findall(string)
            print(result_attribute[0])
            pattern = re.compile(r'<span>(.*?)</span>', re.S)
            result_attribute_value = pattern.findall(string)
            print(result_attribute_value[0])
    
            tr_dir = {
                result_attribute[0]:result_attribute_value[0]
    
            }
            house_trade_dir.update(tr_dir)
        print(house_trade_dir)
    
        '''

        '''
        result= div_house_content.find_all('li')[0]
    
        #result = div_house_content.find_all(text=re.compile(r'<span class="label">.*?</span>(.*?)',re.S))
    
        #print(str(result))
        pattern1 = re.compile(r'<li><span class="label">(.*?)</span>.*?</li>',re.S)
        result_type = pattern1.findall(str(result))
        print(result_type[0])
        pattern = re.compile(r'<li>.*?</span>(.*?)</li>',re.S)
        result_fin=pattern.findall(str(result))
        print(result_fin[0])
    
        '''

    def build_request(self, parse_url):
        header = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

        }
        request = urllib.request.Request(url=parse_url, headers=header)
        content = urllib.request.urlopen(request).read().decode()
        #  with open('pg_%s.html'% page,'wb') as fp :
        #  fp.write(content)
        return content
    def parse_content_law1(self,content):

        soup=BeautifulSoup(content,'lxml')
        com_href_div = soup.find('div', class_='communityName')
        realname = com_href_div.find('a', class_='info')
        community_href = 'https://nj.lianjia.com'+realname['href']
        #print(community_href)
        content_detail=self.build_request(community_href)
        return content_detail




    def parse_content_law2(self,pc):
        soup=BeautifulSoup(pc,'lxml')
        h=soup.find('div',class_='goodSellHeader clear')
        a=h.find('a',class_='fr')
        #print(a['href'])
        return a['href']
    def page_output(self,content_lv1):
        soup = BeautifulSoup(content_lv1,'lxml')
        div_page_box=soup.find('div',class_='page-box house-lst-page-box')
        page=div_page_box['page-data']
        dir=json.loads(page)#字符串转换为字典
        #print(type(dir))
        #print(type(dir['totalPage']))
        total_page=dir['totalPage']
        urlset=[]
        url_set=str(div_page_box['page-url'])
        for i in range(1,total_page+1):
            url=url_set.replace('{page}',str(i))
            url='https://nj.lianjia.com'+url
            urlset.append(url)
        #print(urlset)
        return urlset


    def parse_content_final(self,d_content):
        soup = BeautifulSoup(d_content,'lxml')
        a_href = soup.find_all('a',class_="title")
        for k in a_href:
            content= self.build_request(k['href'])
            parse_content = self.parse_content_detail(content)
            time.sleep(3)
#首页的每一行都是一个小区
    def parse_content(self, content):
        soup = BeautifulSoup(content, 'lxml')
        # print(type(soup))
        # a_content = soup.find_all('a',class_="title")
        # for k in a_content:
        # print(k.string)
        a_herf = soup.find_all('a', class_="title")
        for k in a_herf:
            # print(type(k['href']))
            content = self.build_request(k['href'])
            #用这个content继续解析每个小区其中的若干个二手房
            pc=self.parse_content_law1(content)

            pc_1_url=self.parse_content_law2(pc)
            content_lv1=self.build_request(pc_1_url)


            page_num=self.page_output(content_lv1)
            #print(page_num)

            for url in page_num:
                d_content=self.build_request(url)
                parse_c=self.parse_content_final(d_content)





            time.sleep(random.randint(0,3))

#首页
    def run(self):
        #url_detail=['gulou','jianye','qinhuai','xuanwu','yuhuatai','qixia','jiangning','pukou','liuhe','lishui','gaochun']
        #for detail in url_detail:

          for page in range(self.start_page, self.end_page + 1):
            print("-------------crawling the %s page-----------" % page)
            parse_url = self.url +str(page) + '/'
            #print(parse_url)
            content = self.build_request(parse_url)

            # print(content)
            parse_content = self.parse_content(content)
            time.sleep(random.randint(0,2))


def main():
    start_page = int(input("input the start page :  "))
    end_page = int(input("input the end page :  "))
    spider = second_hand_house(start_page, end_page)
    spider.run()


if __name__ == '__main__':
    main()
