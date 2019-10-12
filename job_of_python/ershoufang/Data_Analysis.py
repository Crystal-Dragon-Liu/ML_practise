# coding=gbk
import re;

import numpy as np #�洢���;���
import pandas as pd #���ݼ� ͳ��
import matplotlib as mp
from pylab import mpl
from pyecharts import Geo #��ͼ��
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

#�ǵ�����seaborn��չ��

'''

house = pd.read_csv('house_price.csv', encoding='gbk')
address = house['address']

'''
mpl.rcParams['font.sans-serif']=['SimHei']#����������ʾ����
plt.rcParams['axes.unicode_minus']=False#����������ʾ����
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
        #�����۸�����
        data_list = []
        for n in result:
            result_str = (str(n[0]).split('�������'))[0]
            result_int = float(result_str)
            # print(type(result_int))
            data_list.append(result_int)
        print(data_list)
        #����dataframe
        #df = pd.DataFrame({'total_price': data_list})

    def show_Constuction_area(self):pass
    def show_TotalPriceAndCAbyUsingScatter(self):

        self.cursor.execute("select total_price,construction_area from inf ;")
        result = self.cursor.fetchall()

        #����۸������б�

        price_list=[]
        area_list=[]
        for n in result:
        #print(n[1])
        #print(type(price_int[0]))

          #����۸�

          price=n[0].split('�������')

          price_int=float(price[0])
          price_list.append(price_int)




          #���������
          area=n[1].split('�O')
          area_int=float(area[0])
          area_list.append(area_int)

        #print(area_list)
        #print(price_list)

        #����ɢ��ͼͼ��һ��
        '''
        plt.scatter(area_list,price_list,s=4,c='r',marker='^',alpha=0.2)
        #s�������c����ɫ,marker,alpha��͸����,���Ը��õĿ������ݼ���
        plt.xlabel("construction_area",fontsize=10)
        plt.ylabel("total_price",fontsize=10)
        plt.title("price&area")
        plt.show()
        '''
        area_array=np.array(area_list)
        price_array=np.array(price_list)

        plt.scatter(area_array, price_array, s=6, c='r', marker='^', alpha=0.3)
        # s�������c����ɫ,marker,alpha��͸����,���Ը��õĿ������ݼ���
        plt.xlabel("construction_area", fontsize=10)
        plt.ylabel("total_price", fontsize=10)
        plt.title("price&area")
        plt.show()
        #

        #print(price_list)
    def linechart(self):




        self.cursor.execute("select year,unit_price from the_second_house_info_des  where year!='δ֪�꽨';")
        result = self.cursor.fetchall()
        #����λ�۸��뽨���������
        unit_price_list =[]
        years_list=[]
        for e in result:
            unit_price=int(e[1].split('Ԫ/ƽ��')[0])
            year=int(e[0])
            unit_price_list.append(unit_price)
            years_list.append(year)
        #print(unit_price_list)
        #print(years_list)
        #���Խ��б�ת��������
        unit_price_list=np.array(unit_price_list)
        years_list=np.array(years_list)
        plt.plot(years_list,unit_price_list)

        plt.show()
    def block_chart(self):
        self.cursor.execute("select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%����%' union select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%��¥%' union select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%����%' union select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%����%' union select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%��ϼ%' union select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%�ػ�%' union select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%�ֿ�%' union select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%����%' union select left(location,2),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%��ˮ%' union select left(location,3),round(avg(replace(unit_price,'Ԫ/ƽ��',''))) from inf where location like'%�껨̨%' ;")
        result = self.cursor.fetchall()
        #�����������뵥λ�۸�����
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

            'name':'�۸�',
            'y_axis':unit_price_list,
            'x_axis':location

        }
        bar.add(**kwargs)
        bar.render(path='F:\python\job_of_python\ershoufang\\bar01.jpg')
        '''
        #��
        #pl=plt.bar(x=location,height=unit_price_list)
        #��
        pl = plt.barh(y=location, width=unit_price_list,label='�۸�')
        #matplotlib����ͼ���ʱ����ʾ����ʱ�����Ļ���С������
        #ʹ�����������

        plt.ylabel("�Ͼ���������", fontsize=10)
        plt.xlabel("������ƽ�����ַ��� Ԫ/ÿƽ��", fontsize=10)
        plt.title("demo")
        plt.legend()
        plt.show()

    def Max_Min_Avg_priceInNanjing(self):
        self.cursor.execute('select left(location,2),max(replace(unit_price,"Ԫ/ƽ��","")+0) from inf;')
        max=[]
        max=self.cursor.fetchall()
        print("�������ж��ַ�����ߵĵ���Ϊ�� "+str(max[0][0])+",�۸�Ϊ�� "+str(max[0][1])+"Ԫ/ƽ��\n")
        self.cursor.execute('select left(location,2),min(replace(unit_price,"Ԫ/ƽ��","")) from inf;')
        min=[]
        min=self.cursor.fetchall()
        print("�������ж��ַ�����͵ĵ���Ϊ�� " + min[0][0] + ",�۸�Ϊ�� " + min[0][1] + "Ԫ/ƽ��\n")
        self.cursor.execute('select round(avg(replace(unit_price,"Ԫ/ƽ��",""))) from inf;')
        avg=[]
        avg=self.cursor.fetchall()
        print("�������ж��ַ�ƽ���ۣ� "+str(int(avg[0][0]))+"Ԫ/ƽ��")
    def NumAndPrice(self):
        #ֱ��ͼ
        self.cursor.execute('select replace(unit_price,"Ԫ/ƽ��","")as price from inf ;')
        price_set=[]
        result_set=self.cursor.fetchall()

        for ps in result_set:
            price_set.append(int(ps[0]))
        price_set=np.array(price_set)
        #print(np.mean(price_set))




        plt.xlim(0,120000)
        plt.ylim(0,250)
        plt.title("�Ͼ��ж��ַ��۷���")
        plt.xlabel('���ַ��۸�Ԫ/ƽ�ף�')
        plt.ylabel('���ַ�����')
        plt.hist(price_set,bins=60)
        plt.vlines(round(np.mean(price_set)),0,250,colors='red',label='ƽ���۸�',linewidth=1.0,linestyles='--')
        plt.vlines(round(np.median(price_set)),0,250,colors='red',label='��λ���۸�',linewidth=1.0)
        plt.legend()

        plt.show()

    def Zone_Price_ByPandas(self):
        #��pandas��ȡDataFrame��������
        sql="select left(location,2) as zone,round(avg(replace(unit_price,'Ԫ/ƽ��','')))as price from inf where location like'%����%' union select left(location,2) as zone,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) as price from inf where location like'%��¥%' union select left(location,2) as zone,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) price from inf where location like'%����%' union select left(location,2) zone ,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) price  from inf where location like'%����%' union select left(location,2) as zone,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) as price from inf where location like'%��ϼ%' union select left(location,2) as zone ,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) as price  from inf where location like'%�ػ�%' union select left(location,2) as zone ,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) as price from inf where location like'%�ֿ�%' union select left(location,2) as zone ,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) as price  from inf where location like'%����%' union select left(location,2) as zone ,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) as price  from inf where location like'%��ˮ%' union select left(location,3) as zone ,round(avg(replace(unit_price,'Ԫ/ƽ��',''))) as price  from inf where location like'%�껨̨%' ;"
        df= pd.read_sql(sql=sql,con=self.dbconn)
        pp=df
        pp.plot(kind='barh')
    def Box(self):
        sql='select left(location,2) as zone,(replace(unit_price,"Ԫ/ƽ��","")+0) as price from inf;'
        df = pd.read_sql(sql=sql, con=self.dbconn)
        df.boxplot(column='price',by='zone')
        plt.show()

    def linearfitting(self,x, A, B):
        return A*x + B
    def Scatter_each_zone(self):
          #������������ķ������ݼ�
          zone=['����','��¥','����','����','��ϼ','�ػ�','�ֿ�','����','��ˮ','�껨̨']
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
                  price_dir.append(int(j[0].split('Ԫ/ƽ��')[0]))
                  area_dir.append(round (float(j[2].split('�O')[0])))


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
              #�ǵ�����SciPyģ�飬������С��������������
              A,B= optimize.curve_fit(self.linearfitting, x, y)[0]
              print(A,B)

              xx = np.arange(0,2000,100)
              yy = A * xx + B
              plt.plot(xx, yy, c=color[i], marker=marker[i], label=zone[i], linewidth=2)





          plt.legend(loc=1,bbox_to_anchor=(1.138,1.0),fontsize=12)
          plt.xlim(100,300)
          plt.ylim(0,120000)
          plt.title('demo')
          plt.xlabel('���������ƽ���ף�',fontsize=20)
          plt.ylabel('���ݵ��ۣ�Ԫ/ƽ���ף�',fontsize=16)
          plt.show()

          print(len(data_dir))

    def MapHot(self):

        self.cursor.execute('select coummunity_name,unit_price from inf;')
        result = self.cursor.fetchall()
        #��������ͼ۸�
        location_dir=[]
        price_dir=[]
        #print(result)
        for r in result:
            price_dir.append(int(r[1].split('Ԫ/ƽ��')[0]))
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
        #����ͼδ���
    def Distance_G(self):

        self.cursor.execute('select coummunity_name as cn,left(location,2) as lo,replace(unit_price,"Ԫ/ƽ��","")as price from inf;')
        result = self.cursor.fetchall()
        #print(result)
        # ����۸������б�

        price_list = []
        distance_G=[]

        for n in result:

            # ����۸�
            price_int = int(n[2])
            price_list.append(price_int)

            #������С������
            com=n[0]
            # ��ȡ��С��������
            h=BaiduMapApi.html(com)
            l=h.get_location()
            #print(l)
            #print(type(l))
            #��ȡ��С�����뵱�������ľ���
            #���õ���С�����ڵ�������
            zone=n[1]
            #print(type(zone))
            G_l=Get_Distance.goverment_location(zone,'�Ͼ�')
            print(G_l)
            D=Get_Distance.getDistance(l[1],l[0],G_l[1],G_l[0])












            exit()
    def house_type(self):
        count=0
        self.cursor.execute('select house_type,count(house_type) from inf group by house_type;')
        result=self.cursor.fetchall()
        sql='select house_type,count(house_type) as count from inf where house_type!="��������"  group by house_type ;'
        #df=pd.read_sql(sql=sql,con=self.dbconn)
        df1=pd.read_sql(sql=sql,con=self.dbconn)
        for i in range(0,len(df1)):
            if df1['count'][i]==1:count+=1
        #print(count)
        df2=df1[~df1['count'].isin([1])] #ɾ��������1����
        df2=df2.append([{'house_type':'����','count':23}],ignore_index=True)
        df2=df2.sort_values(by='count',ascending=False)
        #print(df2)
        df2.plot(x='house_type',y='count',kind='bar',label='count')
        plt.ylabel('ÿ�ֶ��ַ�������', fontsize=10)
        plt.xlabel('���ַ�����', fontsize=10)
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

        pl=plt.bar(height=list_c,x=list_t,label='����')
        plt.ylabel('ÿ�ֶ��ַ�������',fontsize=10)
        plt.xlabel('���ַ�����',fontsize=10)
        plt.legend()
        #plt.show()
        
        '''



def main():
  rd=require_data_inf()
  #rd.show_TotalPriceAndCAbyUsingScatter() # ���ۺͷ������֮��Ĺ�ϵ
  #rd.linechart()
  #rd.block_chart() #����������ƽ������
  #rd.Max_Min_Avg_priceInNanjing() #�Ͼ����ַ���ߣ��ͣ����Ƕ��٣���������ַ���λ����ƽ����
  #rd.NumAndPrice()#�Ͼ����ַ��۸�ֲ�
  #rd.Zone_Price_ByPandas()
  #rd.Box() #�Ͼ������������۷ֲ�ͼ

  #rd.Scatter_each_zone()#ÿ�������ķ����������
  #rd.Distance_G()
  #rd.MapHot()
  #rd.block_chart()
  #rd.house_type()
  rd.close_conn()



if __name__ == '__main__':
     main()

