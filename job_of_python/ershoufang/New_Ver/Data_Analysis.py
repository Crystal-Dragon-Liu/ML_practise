# coding=gbk
import re;

import numpy as np #存储大型矩阵
import pandas as pd #数据集 统计
import matplotlib as mp
from pylab import mpl
from pyecharts import Geo #地图包
from pyecharts import Bar
import matplotlib.pyplot as plt
import ScatterToLine
import pyecharts_snapshot



import pymysql
import BaiduMapApi
import time
import Get_Distance
from scipy import optimize
import math
import seaborn
mpl.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文
plt.rcParams['axes.unicode_minus']=False#用来正常显示负号
def getDbconn():
    mysql_host = 'the_second_house'
    mysql_name = 'localhost'
    mysql_user = 'root'
    mysql_port = 3306
    mysql_password = '1025058706zfr'
    dbconn = pymysql.connect(mysql_name, mysql_user, mysql_password, mysql_host, charset='utf8')

    return dbconn
def closeDbconn(dbconn):
    dbconn.close()
#散点图
def show_PriceAndArea_Scatter(cursor):
    font_1={

        'size':23
    }
    cursor.execute("select total_price,construction_area from the_second_house_final_f_t ;")
    result=cursor.fetchall()
    # 处理价格和面积列表

    price_list = []
    area_list = []
    for n in result:
        #处理价格
        price = n[0].split('万人民币')
        price_int = float(price[0])
        price_list.append(price_int)
        # 处理建筑面积
        area = n[1].split('㎡')
        area_int = float(area[0])
        area_list.append(area_int)

    area_array = np.array(area_list)
    price_array = np.array(price_list)

    plt.scatter(area_array, price_array, s=6, c='r', marker='^', alpha=0.3)
    # s是面积，c是颜色,marker,alpha是透明度,可以更好的看到数据集中
    plt.xlabel("建筑面积（㎡）", fontsize=30)
    plt.ylabel("总价（万人民币）", fontsize=30)
    plt.title("面积——价格",fontsize=30)
    plt.tick_params(labelsize=30)
    plt.show()
#线性拟合
def Line_TotalPriceAndArea():

    l=ScatterToLine.ScatterToLine()
    l.Line_Area_Price()
#条形图
def block_chart_Avg_price_each_zone(cursor):
    cursor.execute(
        "select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%江宁%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%鼓楼%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%建邺%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%玄武%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%栖霞%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%秦淮%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%浦口%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%六合%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%溧水%' union select left(location,3),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%雨花台%' ;")

    result = cursor.fetchall()
    # 处理行政区与单位价格数据
    unit_price_list = []
    location = []
    for e in result:
        unit_price = int(e[1])

        unit_price_list.append(unit_price)
        location.append(e[0])
    pl = plt.barh(y=location, width=unit_price_list, label='价格')

    plt.ylabel("南京各行政区", fontsize=30)
    plt.xlabel("行政区平均二手房价 元/每平方", fontsize=30)
    #plt.title("demo")
    plt.tick_params(labelsize=30)
    plt.legend()
    plt.show()
#条形图改进版
def block_panda_Avg_price_each_zone(cursor):

    sql="select left(location,2) as zone,round(avg(replace(unit_price,'元/平米',''))) as price  from the_second_house_final_f_t where location like'%江宁%' union select left(location,2) as zone,round(avg(replace(unit_price,'元/平米',''))) as price from the_second_house_final_f_t where location like'%鼓楼%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米','')))  as price from the_second_house_final_f_t where location like'%建邺%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price from the_second_house_final_f_t where location like'%玄武%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price from the_second_house_final_f_t where location like'%栖霞%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price  from the_second_house_final_f_t where location like'%秦淮%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price from the_second_house_final_f_t where location like'%浦口%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price from the_second_house_final_f_t where location like'%六合%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price  from the_second_house_final_f_t where location like'%溧水%' union select left(location,3) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price from the_second_house_final_f_t where location like'%雨花台%' ;"
    df=pd.read_sql(sql=sql,con=getDbconn())
    df=df.sort_values(by='price',ascending=False)
    df.plot(x='zone',y='price',kind='bar',label='价格',color='orange')
    plt.ylabel('行政区平均二手房价 （元/每平方）', fontsize=30)
    plt.xlabel('行政区', fontsize=30)
    plt.legend(fontsize=30)
    plt.tick_params(labelsize=22)
    plt.show()

    print(df)
#计算相关重要数据
def Max_Min_Avg_priceInNanjing(cursor):
    cursor.execute('select left(location,2),max(replace(unit_price,"元/平米","")+0) from the_second_house_final_f_t;') #一手细节，+0可以避免得不到最高价格
    max = []
    max = cursor.fetchall()
    print("样本集中二手房价最高的地区为： " + str(max[0][0]) + ",价格为： " + str(max[0][1]) + "元/平米\n")
    cursor.execute('select left(location,2),min(replace(unit_price,"元/平米","")+0) from the_second_house_final_f_t;')
    min = []
    min = cursor.fetchall()
    print("样本集中二手房价最低的地区为： " + min[0][0] + ",价格为： " + str(min[0][1]) + "元/平米\n")
    cursor.execute('select round(avg(replace(unit_price,"元/平米",""))) from the_second_house_final_f_t;')
    avg = []
    avg = cursor.fetchall()
    print("样本集中二手房平均价： " + str(int(avg[0][0])) + "元/平米")#
#直方图
def NumAndPrice(cursor):
    cursor.execute('select replace(unit_price,"元/平米","")as price from inf ;')
    price_set = []
    result_set = cursor.fetchall()

    for ps in result_set:
        price_set.append(int(ps[0]))
    price_set = np.array(price_set)
    # print(np.mean(price_set))

    plt.xlim(0, 120000)
    plt.ylim(0, 250)
    #plt.title("南京市二手房价分析")
    plt.xlabel('二手房价格（元/平米）',fontsize=30)
    plt.ylabel('二手房数量',fontsize=30)
    plt.hist(price_set, bins=60)
    plt.vlines(round(np.mean(price_set)), 0, 250, colors='red', label='平均价格', linewidth=1.0, linestyles='--')
    plt.vlines(round(np.median(price_set)), 0, 250, colors='red', label='中位数价格', linewidth=1.0)
    plt.tick_params(labelsize=30)
    plt.legend()

    plt.show()
#箱型图
def Box(self):
        sql='select left(location,2) as zone,(replace(unit_price,"元/平米","")+0) as price from the_second_house_final_f_t;'
        df = pd.read_sql(sql=sql, con=getDbconn())
        df.boxplot(column='price',by='zone')
        plt.tick_params(labelsize=30)
        plt.show()
#每个地区房价分布，散点图展示
def linearfitting(self,x, A, B):
        return A*x + B
def Scatter_Each_Zone(cursor):
    zone = ['江宁', '鼓楼', '建邺', '玄武', '栖霞', '秦淮', '浦口', '六合', '溧水', '雨花台']
    color = ['orange', 'coral', 'darkblue', 'gold', 'greenyellow', 'lightpink', 'limegreen', 'maroon', 'navy']
    marker = ['.', 'o', 'v', '^', '<', '>', '*', 'h', 'H']

    sql_list = []

    data_dir = {}

    for i in zone:
        sql_list.append('select unit_price,left(location,' + str(
            len(i)) + '),construction_area from the_second_house_final_f_t where location like"%' + i + '%";')
    # print(sql_list)
    for i in range(0, 9):
        price_dir = []
        area_dir = []
        cursor.execute(sql_list[i])
        result = cursor.fetchall()
        for j in result:
            price_dir.append(int(j[0].split('元/平米')[0]))
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

    # print(data_dir[zone[0]]['area'])
    for i in range(0, 9):
        x = data_dir[zone[i]]['area']
        x = np.array(x)
        print(x)

        # print(data_dir)
        y = data_dir[zone[i]]['price']
        y = np.array(y)
        print(y)

        plt.scatter(x,y,c=color[i],s=20,label=zone[i],marker=marker[i],alpha=0.9)
        # 记得下载SciPy模块，进行最小二乘拟合线性拟合
        '''
         A, B = optimize.curve_fit(linearfitting, x, y)[0]
        print(A, B)

        xx = np.arange(0, 2000, 100)
        yy = A * xx + B
        plt.plot(xx, yy, c=color[i], marker=marker[i], label=zone[i], linewidth=2)
        '''

    plt.legend(loc=1, bbox_to_anchor=(1.138, 1.0), fontsize=20)
    plt.xlim(100, 300)
    plt.ylim(0, 120000)
    #plt.title('demo')
    plt.xlabel('房屋面积（平方米）', fontsize=30)
    plt.ylabel('房屋单价（元/平方米）', fontsize=30)
    plt.tick_params(labelsize=30)
    plt.show()

    print(len(data_dir))
#线性拟合
def ScattertoLine_Each_Zone():
    l=ScatterToLine.ScatterToLine()
    l.Line_Each_Zone()
def house_type(cursor):
    count = 0
    cursor.execute('select house_type,count(house_type) from inf group by house_type;')
    result = cursor.fetchall()
    sql = 'select house_type,count(house_type) as count from inf where house_type!="暂无数据"  group by house_type ;'
    # df=pd.read_sql(sql=sql,con=self.dbconn)
    df1 = pd.read_sql(sql=sql, con=getDbconn())
    for i in range(0, len(df1)):
        if df1['count'][i] == 1: count += 1
    # print(count)
    df2 = df1[~df1['count'].isin([1])]  # 删除数量是1的行
    df2 = df2.append([{'house_type': '其它', 'count': 23}], ignore_index=True)
    df2 = df2.sort_values(by='count', ascending=False)
    # print(df2)
    df2.plot(x='house_type', y='count', kind='bar', label='count',color='orange')
    plt.ylabel('每种二手房的数量', fontsize=10)
    plt.xlabel('二手房类型', fontsize=10)
    plt.ylim(0, 800)
    plt.show()
def distance_price(cursor):
    cursor.execute('select replace(unit_price,"元/平米","") as price,round(subway) from the_second_house_final_f where subway!="未知";')
    result = cursor.fetchall()
    #处理价格和距离
    price_list = []
    d_list=[]
    for n in result:
        unit_price=int(n[0])
        price_list.append(unit_price)
        d_list.append(int(n[1]))
    #print(price_list)
    #print(d_list)
    price_array=np.array(price_list)
    d_array=np.array(d_list)
    plt.scatter(d_array,price_array,s=6,c='orange',marker='^',alpha=1)
    plt.xlim(0,1000)
    plt.xlabel("离地铁站的距离（m）", fontsize=10)
    plt.ylabel("二手房每平米价格（元/平方米）", fontsize=10)
    plt.title("地铁站距离——价格")
    plt.show()
def distance_price_f(cursor):
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
        cursor.execute(sql_list[i])
        result = cursor.fetchall()
        for j in result:
            price_dir.append(round(int(j[0].split('元/平米')[0])))
            dis_dir.append(round(float(j[2])))

        price_dir = np.array(price_dir)
        area_dir = np.array(dis_dir)
        #print(price_dir)
        #print(area_dir)
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
    for i in range(0, 9):
        x = data_dir[zone[i]]['dis']
        x = np.array(x)
        print(len(x))

        # print(data_dir)
        y = data_dir[zone[i]]['price']
        y = np.array(y)


        plt.scatter(x,y,c=color[i],s=20,label=zone[i],marker=marker[i],alpha=0.9)
        # 记得下载SciPy模块，进行最小二乘拟合线性拟合
        '''
         A, B = optimize.curve_fit(linearfitting, x, y)[0]
        print(A, B)

        xx = np.arange(0, 2000, 100)
        yy = A * xx + B
        plt.plot(xx, yy, c=color[i], marker=marker[i], label=zone[i], linewidth=2)
        '''

    plt.legend(loc=1, bbox_to_anchor=(1.138, 1.0), fontsize=20)
    plt.xlim(100, 3000)
    plt.ylim(15000, 90000)
    #plt.title('demo')
    plt.xlabel('与最近地铁站之间的距离（米）', fontsize=30)
    plt.ylabel('房屋单价（元/平方米）', fontsize=30)
    plt.tick_params(labelsize=30)
    plt.show()

    #print(len(data_dir))
def distance_price_f_line():
  l=ScatterToLine.ScatterToLine()
  l.Line_Distance()



dbconn=getDbconn()
cursor=dbconn.cursor()
#distance_price(cursor)
#show_PriceAndArea_Scatter(cursor)
#Scatter_Each_Zone(cursor)
#ScattertoLine_Each_Zone()
#Line_TotalPriceAndArea()
#block_chart_Avg_price_each_zone(cursor)
#block_panda_Avg_price_each_zone(cursor)
#Max_Min_Avg_priceInNanjing(cursor)
#NumAndPrice(cursor)
#Box(cursor)
#house_type(cursor)
distance_price_f(cursor)
#distance_price_f_line()
