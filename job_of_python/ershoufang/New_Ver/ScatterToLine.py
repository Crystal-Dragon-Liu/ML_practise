# coding=gbk
import re;

import numpy as np  # 存储大型矩阵
import pandas as pd  # 数据集 统计
import matplotlib as mp
from pylab import mpl
#from pyecharts import Geo  # 地图包
#from pyecharts import Bar
import matplotlib.pyplot as plt
import pyecharts_snapshot



import pymysql
import BaiduMapApi
import time
import Get_Distance
from scipy import optimize
import math

# 记得下载seaborn扩展包

'''

house = pd.read_csv('house_price.csv', encoding='gbk')
address = house['address']

'''
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class ScatterToLine(object):
    mysql_host = 'the_second_house'
    mysql_name = 'localhost'
    mysql_user = 'root'
    mysql_port = 3306
    mysql_password = '1025058706zfr'
    # dbconn = pymysql.connect(self.mysql_name, self.mysql_user, self.mysql_password, self.mysql_host, charset='utf8')
    # cursor = dbconn.cursor()
    dbconn = pymysql.connect(mysql_name, mysql_user, mysql_password, mysql_host, charset='utf8')
    cursor = dbconn.cursor()

    def __init__(self):
        pass

    def close_conn(self):
        self.dbconn.close()



    def linearfitting(self, x, A, B):
        return A * x + B

    def Line_Each_Zone(self):
        # 处理各个地区的房价数据集
        zone = ['江宁', '鼓楼', '建邺', '玄武', '栖霞', '秦淮', '浦口', '六合', '溧水', '雨花台']
        color = ['orange', 'coral', 'darkblue', 'gold', 'greenyellow', 'lightpink', 'limegreen', 'maroon', 'navy']
        marker = ['.', 'o', 'v', '^', '<', '>', '*', 'h', 'H']

        sql_list = []

        data_dir = {}

        for i in zone:
            '''
            sql_list.append('select unit_price,left(location,' + str(
                len(i)) + '),construction_area from inf where location like"%' + i + '%";')
            '''

            sql_list.append('select total_price,left(location,' + str(
                len(i)) + '),construction_area from the_second_house_final_f where location like"%' + i + '%";')
        # print(sql_list)
        for i in range(0, 9):
            price_dir = []
            area_dir = []
            self.cursor.execute(sql_list[i])
            result = self.cursor.fetchall()
            for j in result:
                price_dir.append(float(j[0].split('万人民币')[0]))
                #price_dir.append(round(int(j[0].split('元/平米')[0])))
                area_dir.append(round(float(j[2].split('㎡')[0])))

            price_dir = np.array(price_dir)
            area_dir = np.array(area_dir)

            # print(dir)
            data_dir.update(
                {
                    zone[i]:
                        {

                            'price': price_dir,
                            'area': area_dir
                        }
                }

            )


        for i in range(0, 7):
            x = data_dir[zone[i]]['area']
            x = np.array(x)
            print(len(x))

            # print(data_dir)
            y = data_dir[zone[i]]['price']
            y = np.array(y)
            #print(y)

            # plt.scatter(x,y,c=color[i],s=20,label=zone[i],marker=marker[i],alpha=0.9)
            # 记得下载SciPy模块，进行最小二乘拟合线性拟合
            A,B = optimize.curve_fit(self.linearfitting, x, y)[0]
            #print(A, B)

            xx = np.arange(0, 2000, 100)
            yy = A * xx + B
            plt.plot(xx, yy, c=color[i], marker=marker[i], label=zone[i], linewidth=2)

        plt.legend(loc=1, bbox_to_anchor=(1.138, 1.0), fontsize=20)
        plt.xlim(100, 600)
        #plt.ylim(0,120000)
        plt.ylim(0, 3000)
        #plt.title('demo')
        plt.xlabel('房屋面积（平方米）', fontsize=30)
        plt.ylabel('房屋总价（万人民币）', fontsize=30)
        plt.tick_params(labelsize=30)
        plt.show()

        #print(len(data_dir))
    def Line_Area_Price(self):

        self.cursor.execute("select total_price,construction_area from the_second_house_final_f_t;")
        result = self.cursor.fetchall()
        price_list = []
        area_list = []
        for n in result:
            #处理价格
            price = n[0].split('万人民币')

            price_int = float(price[0])
            price_list.append(price_int)
            #处理面积
            area = n[1].split('㎡')
            area_int = float(area[0])
            area_list.append(area_int)
        #print(price_list)
        area_array = np.array(area_list)

        price_array = np.array(price_list)
        #print(price_array)
        A,B=optimize.curve_fit(self.linearfitting,area_array,price_array)[0]
        xx=np.arange(0,20000,100)
        yy=A*xx+B
        plt.plot(xx, yy, c='orange', marker='o', label='价格', linewidth=2)
        plt.xlim(50,300)
        plt.ylim(0,1000)
        #plt.title('demo')
        plt.xlabel('房屋面积（平方米）', fontsize=30)
        plt.ylabel('房屋总价（万元）', fontsize=30)
        plt.tick_params(labelsize=30)
        plt.show()

    def Line_Distance(self):
        zone = ['江宁', '鼓楼', '建邺', '玄武', '栖霞', '秦淮', '浦口', '六合', '溧水', '雨花台']
        color = ['orange', 'coral', 'darkblue', 'gold', 'greenyellow', 'lightpink', 'limegreen', 'maroon', 'navy']
        marker = ['.', 'o', 'v', '^', '<', '>', '*', 'h', 'H']

        sql_list = []

        data_dir = {}

        for i in zone:
            sql_list.append('select unit_price,left(location,' + str(
                len(i)) + '),subway from the_second_house_final_f where location like"%' + i + '%" and subway!="未知";')
        for i in range(0, 9):
            price_dir = []
            dis_dir = []
            self.cursor.execute(sql_list[i])
            result = self.cursor.fetchall()
            for j in result:
                price_dir.append(round(int(j[0].split('元/平米')[0])))
                dis_dir.append(round(float(j[2])))

            price_dir = np.array(price_dir)
            area_dir = np.array(dis_dir)
            # print(price_dir)
            # print(area_dir)
            # print(dir)
            data_dir.update(
                {
                    zone[i]:
                        {

                            'price': price_dir,
                            'dis': area_dir
                        }
                }

            )
        for i in range(0, 7):
            x = data_dir[zone[i]]['dis']
            x = np.array(x)
            print(len(x))

            # print(data_dir)
            y = data_dir[zone[i]]['price']
            y = np.array(y)

            #plt.scatter(x, y, c=color[i], s=20, label=zone[i], marker=marker[i], alpha=0.9)
            # 记得下载SciPy模块，进行最小二乘拟合线性拟合

            A, B = optimize.curve_fit(self.linearfitting, x, y)[0]
            print(A, B)

            xx = np.arange(0, 2000, 100)
            yy = A * xx + B
            plt.plot(xx, yy, c=color[i], marker=marker[i], label=zone[i], linewidth=2)


        plt.legend(loc=1, bbox_to_anchor=(1.138, 1.0), fontsize=12)
        plt.xlim(100, 1400)
        plt.ylim(15000, 90000)
        plt.title('demo')
        plt.xlabel('与最近地铁站之间的距离（米）', fontsize=20)
        plt.ylabel('房屋单价（元/平方米）', fontsize=16)
        plt.show()



