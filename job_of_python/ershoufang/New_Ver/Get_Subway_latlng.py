import pymysql
import numpy as np
import pandas as pd
import DataBase_Connect
def get_subway_site(cursor):
    '''


    mysql_host = 'the_second_house'
    mysql_name = 'localhost'
    mysql_user = 'root'
    mysql_port = 3306
    mysql_password = '1025058706zfr'
    # dbconn = pymysql.connect(self.mysql_name, self.mysql_user, self.mysql_password, self.mysql_host, charset='utf8')
    # cursor = dbconn.cursor()
    dbconn = pymysql.connect(mysql_name, mysql_user, mysql_password, mysql_host, charset='utf8')
    cursor = dbconn.cursor()

    '''

    cursor.execute('select metro_line_name,lng,lat from metro_line_station where lng!="" and lat!="";')
    result = cursor.fetchall()
    l_list=[]
    for r in result:
        l_list.append([float(r[2]),float(r[1])])
    #df=pd.DataFrame({'location':l_list})
    return l_list

