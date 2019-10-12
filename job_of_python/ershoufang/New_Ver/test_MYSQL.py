#coding=utf-8
import json
import DataBase_Connect
#dbconn=DataBase_Connect()
import os
import DataInsert
with open("F:/python/job_of_python/ershoufang/New_Ver/Crawling_demo_1.json", 'a') as f:
    f.write(']')
    f.seek(-1,os.SEEK_END)
    f.truncate()

f.close()
#dbconn=DataBase_Connect.open_connect()
#DataInsert.Insert_Data(dbconn,di)