import threading
from queue import Queue
import requests
from lxml import etree
import time
import json
import Url_List
import Build_Request
import ParseHomePage
import Parse_Each_Community
import random
import Get_Subway_latlng
import DataBase_Connect
import test_1
import DataInsert
#存放采集线程的列表
g_crawl_list=[]
g_parse_list=[]
id=0
page_now=0
#from job_of_python.ershoufang import GUI_test
#存放解析线程的列表
class CrawlThread(threading.Thread):
    def __init__(self,name,page_queue,data_queue,url):
        super(CrawlThread,self).__init__()
        self.name=name
        self.page_queue=page_queue
        self.data_queue=data_queue
        self.url=url

    def run(self):
        #要一直跑下面的代码，否则效率太低
      print('%s------线程启动' % self.name)
      while 1:
        if self.page_queue.empty():
          break
        #从队列中取出页码
        page=self.page_queue.get()
        page_now=page

        print("---------准备爬取第%s页----------"%page)
        url=self.url+str(page)+'/'
        content=Build_Request.build_request(url)
        self.data_queue.put(content)
      print('%s------线程结束' % self.name)





        #拼接，发送请求
        #将响应内容存放到data_queue中

class ParseThread(threading.Thread):
    def __init__(self,name,data_queue,l_list,lock,d):
        super(ParseThread,self).__init__()
        self.name=name
        self.data_queue=data_queue
        self.l_list=l_list
        self.lock=lock
        self.d=d

    def run(self):
        #取数据 从data_queue中取出一页数据

         print('%s---------线程启动'%self.name)
         while 1:

           try:


            data=self.data_queue.get()
            self.par(data)
           except Exception as e:break

         print("%s------线程结束"%self.name)
    def par(self,data):

        ll=[]
        a_href=ParseHomePage.ParseHomePage(data)
        for i in a_href:
            content_2 = Build_Request.build_request(i)
            inf = Parse_Each_Community.ParseEachCommunity(content_2,self.l_list)
            print("——————————————————————————获取"+inf['小区名称' ]+"的信息——————————————————————————")
            #print("坐标----lng: "+str(inf['坐标']['lng'])+"  lat: "+str(inf['坐标']['lat']))
            ll.append(inf)
            time.sleep(random.randint(0,3))

        self.lock.acquire()
        for inf in ll:
         self.d.write(json.dumps(inf,ensure_ascii=False)+',\n')

        self.lock.release()

        #解析内容即可

def create_queue():
    #创建页码队列
    page_queue=Queue()
    for page in range(1,101):
        page_queue.put(page)
    #创建内容队列

    data_queue=Queue()

    return page_queue,data_queue

def create_crawl_thread(page_queue,data_queue,url):
    #实例化采集线程

    crawl_name=['crawl1','crawl2','crawl3','crawl4','crawl5','crawl6','crawl7','crawl8','crawl9','crawl10']
    for name in crawl_name:
        g_crawl_list.append(CrawlThread(name,page_queue,data_queue,url))
        print("创建"+name+"采集线程")

def create_parse_thread(data_queue,l_list,lock,d):
    parse_name = ['parse1', 'parse2', 'parse3','parse4','parse5','parse6','parse7','parse8','parse9','parse10']
    for name in parse_name:
        g_parse_list.append(ParseThread(name,data_queue,l_list,lock,d))
        print("创建"+name+"解析线程")





def main():
    #创建队列
    url='https://nj.lianjia.com/ershoufang/pg'

    page_queue,data_queue=create_queue()



    dbconn=DataBase_Connect.open_connect()
    cursor = dbconn.cursor()
    l_list = Get_Subway_latlng.get_subway_site(cursor)
    #DataBase_Connect.close_connect(dbconn)
    lock=threading.Lock()
    d=open('F:/python/job_of_python/ershoufang/New_Ver/Crawling_demo_1.json','a')
    d.write('[')

    #把锁也传递进去



    #创建采集线程和解析线程
    create_crawl_thread(page_queue,data_queue,url)
    time.sleep(3)
    create_parse_thread(data_queue,l_list,lock,d)
    #启动线程
    for tcrawl in g_crawl_list:
        tcrawl.start()
        print("启动一个采集线程")

    for tparse in g_parse_list:
        tparse.start()
        print("启动一个解析线程")
    #主线程等待子线程结束

    for tcrawl in g_crawl_list:
        tcrawl.join()
        print("结束一个采集线程")

    for tparse in g_parse_list:
        tparse.join()
        print("结束一个解析线程")

    print('主线程和子线程运行结束')
    d.write(']')
    d.close()
    with open("F:/python/job_of_python/ershoufang/New_Ver/Crawling_demo_1.json", "r") as fp:

        di = json.load(fp)


    #DataInsert.Insert_Data(dbconn,di)
    #DataBase_Connect.close_connect(dbconn)













if __name__ == '__main__':
   main()