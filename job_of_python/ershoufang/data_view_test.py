'''

import re
import numpy as np #存储大型矩阵
import pandas as pd #数据集 统计
import matplotlib as mpl
from pyecharts import Geo #地图包
import pyecharts
import matplotlib.pyplot as plt

from wordcloud import wordcloud
import jieba
import pymysql
'''

'''
#第一种创建
a = [1,2,3,4]
#将列表转换成ndarray对象
x1=np.array(a)
#第二种创建
x=np.arange(11)
#1到11
mysql_host = 'the_second_house'
mysql_name = 'localhost'
mysql_user = 'root'
mysql_port = 3306
mysql_password = '1025058706zfr'
dbconn = pymysql.connect(mysql_name, mysql_user, mysql_password, mysql_host, charset='utf8')
cursor = dbconn.cursor()
cursor.execute("select total_price from inf where id >=0 and id<=10;")
#result_test=cursor.fetchone()
#获取一行

result = cursor.fetchall()
data_list=[]
for n in result:
 result_str=(str(n[0]).split('万人民币'))[0]
 result_int=int(result_str)
 #print(type(result_int))
 data_list.append(result_int)
#print(data_list)

#print(df)
da=np.array(data_list)

#x=np.random.randint(1,100,10) 随机生成数组

#print(da.max())
#print(da.min())
#y=np.sort(da)
#print(y)# y是新生成的数组，da本身不变化
#y=da.sort()
#da本身会发生变化








#panda 的DATAFRAME   df=pd.DataFrame({'total_price':data_list})


#da[-1] 最后一个
#da[0:5]第一个到第六个
#da[5:]从5开始到最后一个
#双冒号 da[::2]以2为步长选取数字
#常用函数  np.func(x)
#print(str(result[0]).split(cut))
#print(len(result))
#pandas_result=pd.DataFrame(result[])
#print
#print((str(result[0]).split(cut))[0])
cursor.close()
dbconn.commit()
dbconn.close()

'''


import re;
import numpy as np #存储大型矩阵
import pandas as pd #数据集 统计
import matplotlib as mpl
from pyecharts import Geo #地图包
import pyecharts
import matplotlib.pyplot as plt

#散点图
'''

plt.scatter(area_list,price_list,s=4,c='r',marker='^',alpha=0.2)
        #s是面积，c是颜色,marker,alpha是透明度,可以更好的看到数据集中
        plt.xlabel("construction_area",fontsize=10)
        plt.ylabel("total_price",fontsize=10)
        plt.title("price&area")
        plt.show()
        
        area_array=np.array(area_list)
        price_array=np.array(price_list)

        plt.scatter(area_array, price_array, s=6, c='r', marker='^', alpha=0.3)
        # s是面积，c是颜色,marker,alpha是透明度,可以更好的看到数据集中
        plt.xlabel("construction_area", fontsize=10)
        plt.ylabel("total_price", fontsize=10)
        plt.title("price&area")
        plt.show()
'''
x=np.linespace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()