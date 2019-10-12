# coding=gbk
import re;

import numpy as np #存储大型矩阵
import pandas as pd #数据集 统计
import matplotlib as mp
from pylab import mpl
from pyecharts import Geo #地图包
from pyecharts import Bar
import matplotlib.pyplot as plt
import pyecharts_snapshot

from wordcloud import wordcloud
import jieba
import pymysql
import BaiduMapApi
import time
import Get_Distance
from scipy import optimize
import math

#记得下载seaborn扩展包

'''

house = pd.read_csv('house_price.csv', encoding='gbk')
address = house['address']

'''
mpl.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文
plt.rcParams['axes.unicode_minus']=False#用来正常显示负号
class require_data_inf(object):
    mysql_host = 'the_second_house'
    mysql_name = 'localhost'
    mysql_user = 'root'
    mysql_port = 3306
    mysql_password = '1025058706zfr'
    #dbconn = pymysql.connect(self.mysql_name, self.mysql_user, self.mysql_password, self.mysql_host, charset='utf8')
    #cursor = dbconn.cursor()
    dbconn = pymysql.connect(mysql_name, mysql_user, mysql_password, mysql_host, charset='utf8')
    cursor = dbconn.cursor()
    def __init__(self):pass
    def close_conn(self):
         self.dbconn.close()

    def show_TotalPrice(self):

        self.cursor.execute("select total_price from inf where id >=0 and id<=10;")
        result = self.cursor.fetchall()
        #创建价格数组
        data_list = []
        for n in result:
            result_str = (str(n[0]).split('万人民币'))[0]
            result_int = float(result_str)
            # print(type(result_int))
            data_list.append(result_int)
        print(data_list)
        #创建dataframe
        #df = pd.DataFrame({'total_price': data_list})

    def show_Constuction_area(self):pass
    def show_TotalPriceAndCAbyUsingScatter(self):

        self.cursor.execute("select total_price,construction_area from inf ;")
        result = self.cursor.fetchall()

        #处理价格和面积列表

        price_list=[]
        area_list=[]
        for n in result:
        #print(n[1])
        #print(type(price_int[0]))

          #处理价格

          price=n[0].split('万人民币')

          price_int=float(price[0])
          price_list.append(price_int)




          #处理建筑面积
          area=n[1].split('㎡')
          area_int=float(area[0])
          area_list.append(area_int)

        #print(area_list)
        #print(price_list)

        #画个散点图图看一看
        '''
        plt.scatter(area_list,price_list,s=4,c='r',marker='^',alpha=0.2)
        #s是面积，c是颜色,marker,alpha是透明度,可以更好的看到数据集中
        plt.xlabel("construction_area",fontsize=10)
        plt.ylabel("total_price",fontsize=10)
        plt.title("price&area")
        plt.show()
        '''
        area_array=np.array(area_list)
        price_array=np.array(price_list)

        plt.scatter(area_array, price_array, s=6, c='r', marker='^', alpha=0.3)
        # s是面积，c是颜色,marker,alpha是透明度,可以更好的看到数据集中
        plt.xlabel("construction_area", fontsize=10)
        plt.ylabel("total_price", fontsize=10)
        plt.title("price&area")
        plt.show()
        #

        #print(price_list)
    def linechart(self):




        self.cursor.execute("select year,unit_price from the_second_house_info_des  where year!='未知年建';")
        result = self.cursor.fetchall()
        #处理单位价格与建筑年代数据
        unit_price_list =[]
        years_list=[]
        for e in result:
            unit_price=int(e[1].split('元/平米')[0])
            year=int(e[0])
            unit_price_list.append(unit_price)
            years_list.append(year)
        #print(unit_price_list)
        #print(years_list)
        #可以将列表转换成数组
        unit_price_list=np.array(unit_price_list)
        years_list=np.array(years_list)
        plt.plot(years_list,unit_price_list)

        plt.show()
    def block_chart(self):
        self.cursor.execute("select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%江宁%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%鼓楼%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%建邺%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%玄武%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%栖霞%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%秦淮%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%浦口%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%六合%' union select left(location,2),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%溧水%' union select left(location,3),round(avg(replace(unit_price,'元/平米',''))) from inf where location like'%雨花台%' ;")
        result = self.cursor.fetchall()
        #处理行政区与单位价格数据
        unit_price_list = []
        location = []
        for e in result:
            unit_price = int(e[1])

            unit_price_list.append(unit_price)
            location.append(e[0])
        #print(unit_price_list)
        #print(location)

        '''
        Pyechart
        
        bar=Bar('price&zone')
        kwargs= {

            'name':'价格',
            'y_axis':unit_price_list,
            'x_axis':location

        }
        bar.add(**kwargs)
        bar.render(path='F:\python\job_of_python\ershoufang\\bar01.jpg')
        '''
        #竖
        #pl=plt.bar(x=location,height=unit_price_list)
        #横
        pl = plt.barh(y=location, width=unit_price_list,label='价格')
        #matplotlib绘制图像的时候显示中文时候，中文会变成小方格子
        #使用字体管理器

        plt.ylabel("南京各行政区", fontsize=10)
        plt.xlabel("行政区平均二手房价 元/每平方", fontsize=10)
        plt.title("demo")
        plt.legend()
        plt.show()

    def Max_Min_Avg_priceInNanjing(self):
        self.cursor.execute('select left(location,2),max(replace(unit_price,"元/平米","")+0) from inf;')
        max=[]
        max=self.cursor.fetchall()
        print("样本集中二手房价最高的地区为： "+str(max[0][0])+",价格为： "+str(max[0][1])+"元/平米\n")
        self.cursor.execute('select left(location,2),min(replace(unit_price,"元/平米","")) from inf;')
        min=[]
        min=self.cursor.fetchall()
        print("样本集中二手房价最低的地区为： " + min[0][0] + ",价格为： " + min[0][1] + "元/平米\n")
        self.cursor.execute('select round(avg(replace(unit_price,"元/平米",""))) from inf;')
        avg=[]
        avg=self.cursor.fetchall()
        print("样本集中二手房平均价： "+str(int(avg[0][0]))+"元/平米")
    def NumAndPrice(self):
        #直方图
        self.cursor.execute('select replace(unit_price,"元/平米","")as price from inf ;')
        price_set=[]
        result_set=self.cursor.fetchall()

        for ps in result_set:
            price_set.append(int(ps[0]))
        price_set=np.array(price_set)
        #print(np.mean(price_set))




        plt.xlim(0,120000)
        plt.ylim(0,250)
        plt.title("南京市二手房价分析")
        plt.xlabel('二手房价格（元/平米）')
        plt.ylabel('二手房数量')
        plt.hist(price_set,bins=60)
        plt.vlines(round(np.mean(price_set)),0,250,colors='red',label='平均价格',linewidth=1.0,linestyles='--')
        plt.vlines(round(np.median(price_set)),0,250,colors='red',label='中位数价格',linewidth=1.0)
        plt.legend()

        plt.show()

    def Zone_Price_ByPandas(self):
        #用pandas获取DataFrame类型数据
        sql="select left(location,2) as zone,round(avg(replace(unit_price,'元/平米','')))as price from inf where location like'%江宁%' union select left(location,2) as zone,round(avg(replace(unit_price,'元/平米',''))) as price from inf where location like'%鼓楼%' union select left(location,2) as zone,round(avg(replace(unit_price,'元/平米',''))) price from inf where location like'%建邺%' union select left(location,2) zone ,round(avg(replace(unit_price,'元/平米',''))) price  from inf where location like'%玄武%' union select left(location,2) as zone,round(avg(replace(unit_price,'元/平米',''))) as price from inf where location like'%栖霞%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price  from inf where location like'%秦淮%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price from inf where location like'%浦口%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price  from inf where location like'%六合%' union select left(location,2) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price  from inf where location like'%溧水%' union select left(location,3) as zone ,round(avg(replace(unit_price,'元/平米',''))) as price  from inf where location like'%雨花台%' ;"
        df= pd.read_sql(sql=sql,con=self.dbconn)
        pp=df
        pp.plot(kind='barh')
    def Box(self):
        sql='select left(location,2) as zone,(replace(unit_price,"元/平米","")+0) as price from inf;'
        df = pd.read_sql(sql=sql, con=self.dbconn)
        df.boxplot(column='price',by='zone')
        plt.show()

    def linearfitting(self,x, A, B):
        return A*x + B
    def Scatter_each_zone(self):
          #处理各个地区的房价数据集
          zone=['江宁','鼓楼','建邺','玄武','栖霞','秦淮','浦口','六合','溧水','雨花台']
          color=['orange','coral','darkblue','gold','greenyellow','lightpink','limegreen','maroon','navy']
          marker=['.','o','v','^','<','>','*','h','H']


          sql_list=[]

          data_dir={}

          for i in zone:
                sql_list.append('select unit_price,left(location,'+str(len(i))+'),construction_area from inf where location like"%'+i+'%";')
             #print(sql_list)
          for i in range(0,9):
              price_dir=[]
              area_dir=[]
              self.cursor.execute(sql_list[i])
              result=self.cursor.fetchall()
              for j in result:
                  price_dir.append(int(j[0].split('元/平米')[0]))
                  area_dir.append(round (float(j[2].split('㎡')[0])))


              price_dir=np.array(price_dir)
              area_dir=np.array(area_dir)


              #print(dir)
              data_dir.update(
                  {
                      zone[i]:
                      {

                         'price':price_dir,
                          'area':area_dir
                      }
                  }


              )



          #print(data_dir[zone[0]]['area'])
          for i in range(0,9):
              x=data_dir[zone[i]]['area']
              x=np.array(x)
              print(x)




              #print(data_dir)
              y=data_dir[zone[i]]['price']
              y=np.array(y)
              print(y)


              #plt.scatter(x,y,c=color[i],s=20,label=zone[i],marker=marker[i],alpha=0.9)
              #记得下载SciPy模块，进行最小二乘拟合线性拟合
              A,B= optimize.curve_fit(self.linearfitting, x, y)[0]
              print(A,B)

              xx = np.arange(0,2000,100)
              yy = A * xx + B
              plt.plot(xx, yy, c=color[i], marker=marker[i], label=zone[i], linewidth=2)





          plt.legend(loc=1,bbox_to_anchor=(1.138,1.0),fontsize=12)
          plt.xlim(100,300)
          plt.ylim(0,120000)
          plt.title('demo')
          plt.xlabel('房屋面积（平方米）',fontsize=20)
          plt.ylabel('房屋单价（元/平方米）',fontsize=16)
          plt.show()

          print(len(data_dir))

    def MapHot(self):

        self.cursor.execute('select coummunity_name,unit_price from inf;')
        result = self.cursor.fetchall()
        #处理地名和价格
        location_dir=[]
        price_dir=[]
        #print(result)
        for r in result:
            price_dir.append(int(r[1].split('元/平米')[0]))
            location_dir.append(r[0])

        #print(price_dir)
        #print(location_dir)


        coor=[]
        for add in location_dir:
            loc=BaiduMapApi.html(add).get_location()
            #print(type(list(loc)[0]))
            #print(type(list(loc)))
            coor.append(list(loc))
            #print(coor)

            #print(coor)
            #time.sleep(1)
        coord_column= pd.Series(coor,name='coord')
        save= pd.DataFrame({'coord':coord_column})
        save.to_csv('coord.csv',encoding="gbk",columns=['coord'],header=True,index=False)







            #print(coordinate)

        #print(coor)
        #热力图未完成
    def Distance_G(self):

        self.cursor.execute('select coummunity_name as cn,left(location,2) as lo,replace(unit_price,"元/平米","")as price from inf;')
        result = self.cursor.fetchall()
        #print(result)
        # 处理价格和面积列表

        price_list = []
        distance_G=[]

        for n in result:

            # 处理价格
            price_int = int(n[2])
            price_list.append(price_int)

            #处理房子小区名称
            com=n[0]
            # 获取此小区的坐标
            h=BaiduMapApi.html(com)
            l=h.get_location()
            #print(l)
            #print(type(l))
            #获取此小区距离当地政府的距离
            #先拿到此小区所在的行政区
            zone=n[1]
            #print(type(zone))
            G_l=Get_Distance.goverment_location(zone,'南京')
            print(G_l)
            D=Get_Distance.getDistance(l[1],l[0],G_l[1],G_l[0])












            exit()
    def house_type(self):
        count=0
        self.cursor.execute('select house_type,count(house_type) from inf group by house_type;')
        result=self.cursor.fetchall()
        sql='select house_type,count(house_type) as count from inf where house_type!="暂无数据"  group by house_type ;'
        #df=pd.read_sql(sql=sql,con=self.dbconn)
        df1=pd.read_sql(sql=sql,con=self.dbconn)
        for i in range(0,len(df1)):
            if df1['count'][i]==1:count+=1
        #print(count)
        df2=df1[~df1['count'].isin([1])] #删除数量是1的行
        df2=df2.append([{'house_type':'其它','count':23}],ignore_index=True)
        df2=df2.sort_values(by='count',ascending=False)
        #print(df2)
        df2.plot(x='house_type',y='count',kind='bar',label='count')
        plt.ylabel('每种二手房的数量', fontsize=10)
        plt.xlabel('二手房类型', fontsize=10)
        plt.ylim(0,800)
        plt.show()
        '''
        list_c=[]
        list_t=[]
        for r in result:
            list_c.append(r[1])
            list_t.append(r[0])

        #print(list_c)
        #print(list_t)

        pl=plt.bar(height=list_c,x=list_t,label='数量')
        plt.ylabel('每种二手房的数量',fontsize=10)
        plt.xlabel('二手房类型',fontsize=10)
        plt.legend()
        #plt.show()
        
        '''



def main():
  rd=require_data_inf()
  #rd.show_TotalPriceAndCAbyUsingScatter() # 房价和房屋面积之间的关系
  #rd.linechart()
  #rd.block_chart() #各个地区的平均房价
  #rd.Max_Min_Avg_priceInNanjing() #南京二手房最高（低）价是多少，在哪里，二手房中位数和平均数
  #rd.NumAndPrice()#南京二手房价格分布
  #rd.Zone_Price_ByPandas()
  #rd.Box() #南京各个地区房价分布图

  #rd.Scatter_each_zone()#每个地区的房价线性拟合
  #rd.Distance_G()
  #rd.MapHot()
  #rd.block_chart()
  #rd.house_type()
  rd.close_conn()



if __name__ == '__main__':
     main()

