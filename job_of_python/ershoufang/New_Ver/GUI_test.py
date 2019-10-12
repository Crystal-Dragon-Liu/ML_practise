import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QComboBox,QTextBrowser,QTableWidget,QTableWidgetItem,QHeaderView,QProgressBar,QHBoxLayout,QVBoxLayout
import Thread_TEST
from  PyQt5.QtCore import QThread
import threading
from queue import Queue
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
import requests
from bs4 import BeautifulSoup
import requests
from lxml import etree
import time
import json
import Url_List
import Build_Request
import ParseHomePage
import Parse_Each_Community
import random
#import Thread_TEST
import Get_Subway_latlng
import DataBase_Connect
import test_1
import DataInsert
#存放采集线程的列表
g_crawl_list=[]
g_parse_list=[]
id=0

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
        print("---------准备爬取第%s页----------"%page)
        url=self.url+str(page)+'/'
        content=Build_Request.build_request(url)
        self.data_queue.put(content)
      print('%s------线程结束' % self.name)





        #拼接，发送请求
        #将响应内容存放到data_queue中

class ParseThread(threading.Thread):
    def __init__(self,name,data_queue,l_list,lock,d,result_signal):
        super(ParseThread,self).__init__()
        self.name=name
        self.data_queue=data_queue
        self.l_list=l_list
        self.lock=lock
        self.d=d
        self.result_signal=result_signal

    def run(self):
        #取数据 从data_queue中取出一页数据

         print('%s---------线程启动'%self.name)
         while 1:

             try:


               data=self.data_queue.get()
               self.par(data)
             except Exception as e:
               break


         print("%s------线程结束"%self.name)
    def par(self,data):

        ll=[]
        a_href=ParseHomePage.ParseHomePage(data)
        for i in a_href:
            content_2 = Build_Request.build_request(i)
            inf = Parse_Each_Community.ParseEachCommunity(content_2,self.l_list)
            print("——————————————————————————获取"+inf['小区名称' ]+"的信息——————————————————————————")
            self.result_signal.emit(inf['小区名称'],inf['单价'],inf['总价'],inf['房屋户型'],inf['建筑年代'])
            #print("坐标----lng: "+str(inf['坐标']['lng'])+"  lat: "+str(inf['坐标']['lat']))
            ll.append(inf)
            time.sleep(random.randint(0,3))
            #count=count+1

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

    #crawl_name=['crawl1','crawl2','crawl3','crawl4','crawl5','crawl6','crawl7','crawl8','crawl9','crawl10']
    crawl_name=['c1','c2','c3']
    for name in crawl_name:
        g_crawl_list.append(CrawlThread(name,page_queue,data_queue,url))
        print("创建"+name+"采集线程")

def create_parse_thread(data_queue,l_list,lock,d,result_signal):
    #parse_name = ['parse1', 'parse2', 'parse3','parse4','parse5','parse6','parse7','parse8','parse9','parse10']
    parse_name=['p1','p2','p3']
    for name in parse_name:
        g_parse_list.append(ParseThread(name,data_queue,l_list,lock,d,result_signal))
        print("创建"+name+"解析线程")

class CT(QThread):
    finished_signal=pyqtSignal()
    log_signal=pyqtSignal(str)
    result_signal=pyqtSignal(str,str,str,str,str)
    def __init__(self):
        super(CT,self).__init__()


    def run(self):
        #Thread_TEST.main()
        url = 'https://nj.lianjia.com/ershoufang/pg'

        page_queue, data_queue = create_queue()

        dbconn = DataBase_Connect.open_connect()
        cursor = dbconn.cursor()
        l_list = Get_Subway_latlng.get_subway_site(cursor)
        # DataBase_Connect.close_connect(dbconn)
        lock = threading.Lock()
        d = open('F:/python/job_of_python/ershoufang/New_Ver/Crawling_demo_3.json', 'a')

        # 把锁也传递进去

        # 创建采集线程和解析线程
        create_crawl_thread(page_queue, data_queue, url)
        time.sleep(3)
        create_parse_thread(data_queue, l_list, lock, d,self.result_signal)
        # 启动线程
        for tcrawl in g_crawl_list:
            tcrawl.start()
            #print("启动一个采集线程")
            self.log_signal.emit('启动一个采集线程')

        for tparse in g_parse_list:
            tparse.start()
            #print("启动一个解析线程")
            self.log_signal.emit('启动一个解析线程')
        # 主线程等待子线程结束

        for tcrawl in g_crawl_list:
            tcrawl.join()
            #print("结束一个采集线程")
            self.log_signal.emit('结束一个采集线程')

        for tparse in g_parse_list:
            tparse.join()
            #print("结束一个解析线程")
            self.log_signal.emit('结束一个解析线程')

        print('主线程和子线程运行结束')
        d.close()
        '''
           try:
            with open("F:/python/job_of_python/ershoufang/New_Ver/Crawling_demo_3.json", "r") as fp:
              di = json.load(fp)
        except Exception as e:
            print('json格式转化失败')
        
        '''

        DataBase_Connect.close_connect(dbconn)
        self.log_signal.emit('爬取数据结束')
        self.finished_signal.emit()#发射信号




class CrawlWindow(QWidget):
    def __init__(self):
        super(CrawlWindow,self).__init__()
        self.resize(800,600)
        self.setWindowTitle("Second-hand house")
        #self.setWindowIcon()
        self.start_btn=QPushButton(self)
        self.stop_btn=QPushButton(self)
        self.save_combobox=QComboBox(self)
        self.table=QTableWidget(self)
        self.log_browser=QTextBrowser(self)
        self.progressbar=QProgressBar(self)

        self.h_layout=QHBoxLayout()
        self.v_layout=QVBoxLayout()

        self.crawl_thread=CT()

        #对控件进行调整
        self.btn_init()
        self.combobox_init()
        self.table_init()
        self.progressbar_init()
        self.layout_init()
        self.crawl_init()







    def crawl_init(self):
        self.crawl_thread.finished_signal.connect(self.finish_slot)
        self.crawl_thread.log_signal.connect(self.set_log_slot)
        self.crawl_thread.result_signal.connect(self.set_result_slot)
    def btn_init(self):
        self.start_btn.setText("开始爬取")
        self.stop_btn.setText("停止爬取")
        self.stop_btn.setEnabled(False)
        self.start_btn.clicked.connect(lambda:self.btn_slot(self.start_btn))
        self.stop_btn.clicked.connect(lambda: self.btn_slot(self.stop_btn))
    def combobox_init(self):
        save_list=['另存为','MySQL','CSV','TXT','JSON']
        self.save_combobox.addItems(save_list)
        self.save_combobox.setEnabled(False)
    def table_init(self):
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['小区名称','单价','总价','房屋类型','建筑年代'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def progressbar_init(self):
        self.progressbar.setRange(0,2320)
        self.progressbar.setValue(0)
    def layout_init(self):
        self.h_layout.addWidget(self.start_btn)
        self.h_layout.addWidget(self.stop_btn)
        self.h_layout.addWidget(self.save_combobox)
        self.v_layout.addWidget(self.table)
        self.v_layout.addWidget(self.log_browser)
        self.v_layout.addWidget(self.progressbar)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
    def btn_slot(self,btn):
        if btn==self.start_btn:
            self.log_browser.clear()
            self.log_browser.append('<font color="red">开始爬取</font>')
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.save_combobox.setEnabled(False)
            self.crawl_thread.start()
            print("线程开始")
        else:
            self.log_browser.append('<font color="red">停止爬取</font>')
            self.stop_btn.setEnabled(False)
            self.start_btn.setEnabled(True)
            self.save_combobox.setEnabled(True)
            self.crawl_thread.terminate()

            print("线程终止")
    def finish_slot(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.save_combobox.setEnabled(True)
        self.crawl_thread.terminate()
    def set_log_slot(self,new_log):
        self.log_browser.append(new_log)
    def set_result_slot(self,name,unit_price,total_price,house_type,year):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row,0,QTableWidgetItem(name))
        self.table.setItem(row, 1, QTableWidgetItem(unit_price))
        self.table.setItem(row, 2, QTableWidgetItem(total_price))
        self.table.setItem(row, 3, QTableWidgetItem(house_type))
        self.table.setItem(row, 4, QTableWidgetItem(year))





if __name__=='__main__':
    app=QApplication(sys.argv)
    window=CrawlWindow()
    window.show()
    sys.exit(app.exec_())