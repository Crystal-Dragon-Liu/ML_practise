import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QComboBox,QTextBrowser,QTableWidget,QTableWidgetItem,QHeaderView,QProgressBar,QHBoxLayout,QVBoxLayout,QMessageBox
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
    def __init__(self,name,page_queue,data_queue,url,log_signal):
        super(CrawlThread,self).__init__()
        self.name=name
        self.page_queue=page_queue
        self.data_queue=data_queue
        self.url=url
        self.ifdo=True
        self.log_signal=log_signal
    def stop(self):
        self.ifdo=False
    def run(self):
        #要一直跑下面的代码，否则效率太低
      #print('%s------线程启动' % self.name)
      self.log_signal.emit('%s------线程启动' % self.name)
      while self.ifdo==True:
        if self.page_queue.empty():break
        #从队列中取出页码
        page=self.page_queue.get()
        #print("---------准备爬取第%s页----------"%page)
        self.log_signal.emit("---------准备爬取第%s页----------"%page)
        url=self.url+str(page)+'/'
        content=Build_Request.build_request(url)
        self.data_queue.put(content)

      #print('%s------线程结束' % self.name)
      self.log_signal.emit('%s------线程结束' % self.name)





        #拼接，发送请求
        #将响应内容存放到data_queue中

class ParseThread(threading.Thread):
    def __init__(self,name,data_queue,l_list,lock,result_signal,log_signal):
        super(ParseThread,self).__init__()
        self.name=name
        self.data_queue=data_queue
        self.l_list=l_list
        self.lock=lock

        self.result_signal=result_signal
        self.log_signal=log_signal
        self.ifdo =True
    def stop(self):
        self.ifdo=False
    def run(self):
        #取数据 从data_queue中取出一页数据

         #print('%s---------线程启动'%self.name)
         self.log_signal.emit('%s---------线程启动'%self.name)
         while self.ifdo == True:

             try:


               data=self.data_queue.get()
               self.par(data)
             except Exception as e:
               break


         #print("%s------线程结束"%self.name)
         self.log_signal.emit("%s------线程结束"%self.name)
    def par(self,data):
      if self.ifdo==True:
        ll=[]
        a_href=ParseHomePage.ParseHomePage(data)
        for i in a_href:
            content_2 = Build_Request.build_request(i)
            inf = Parse_Each_Community.ParseEachCommunity(content_2,self.l_list)
            #print("——————————————————————————获取"+inf['小区名称' ]+"的信息——————————————————————————")
            self.result_signal.emit(inf['小区名称'],inf['小区地点'],inf['总价'],inf['单价'],inf['房屋户型'],inf['所在楼层'],inf['建筑面积'],inf['户型结构'],inf['套内面积'],inf['建筑类型'],inf['房屋朝向'],inf['建筑结构'],inf['装修情况'],inf['梯户比例'],inf['配备电梯'],inf['产权年限'],inf['建筑年代'],str(inf['坐标']['lng']),str(inf['坐标']['lat']),str(inf['地铁距离']),str(inf['政府距离']))
            #print("坐标----lng: "+str(inf['坐标']['lng'])+"  lat: "+str(inf['坐标']['lat']))
            ll.append(inf)
            time.sleep(random.randint(0,3))
            #count=count+1

        self.lock.acquire()
        #for inf in ll:
           #self.d.write(json.dumps(inf,ensure_ascii=False)+',\n')

        self.lock.release()
      else:
          print("线程被终止")
          exit()

        #解析内容即可

def create_queue():
    #创建页码队列
    page_queue=Queue()
    for page in range(1,4):
        page_queue.put(page)
    #创建内容队列

    data_queue=Queue()

    return page_queue,data_queue

def create_crawl_thread(page_queue,data_queue,url,log_signal):
    #实例化采集线程

    crawl_name=['crawl1','crawl2','crawl3','crawl4','crawl5','crawl6','crawl7','crawl8','crawl9','crawl10']
    #crawl_name=['c1','c2','c3']
    #crawl_name=['c1','c2']
    for name in crawl_name:
        g_crawl_list.append(CrawlThread(name,page_queue,data_queue,url,log_signal))
        print("创建"+name+"采集线程")

def create_parse_thread(data_queue,l_list,lock,result_signal,log_signal):
    parse_name = ['parse1', 'parse2', 'parse3','parse4','parse5','parse6','parse7','parse8','parse9','parse10']
    #parse_name=['p1','p2','p3']
    parse_name=['p1','p2']
    for name in parse_name:
        g_parse_list.append(ParseThread(name,data_queue,l_list,lock,result_signal,log_signal))
        print("创建"+name+"解析线程")

class CT(QThread):
    finished_signal=pyqtSignal()
    log_signal=pyqtSignal(str)
    result_signal=pyqtSignal(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
    def __init__(self):
        super(CT,self).__init__()


    def run(self):
        #Thread_TEST.main()
        url = 'https://nj.lianjia.com/ershoufang/pg'

        page_queue, data_queue = create_queue()

        dbconn = DataBase_Connect.open_connect()
        cursor = dbconn.cursor()
        l_list = Get_Subway_latlng.get_subway_site(cursor)
        DataBase_Connect.close_connect(dbconn)
        # DataBase_Connect.close_connect(dbconn)
        lock = threading.Lock()
        #d = open('F:/python/job_of_python/ershoufang/New_Ver/Crawling_demo_3.json', 'a')
        #d.write('[')
        # 把锁也传递进去

        # 创建采集线程和解析线程
        create_crawl_thread(page_queue, data_queue, url,self.log_signal)
        time.sleep(3)
        create_parse_thread(data_queue, l_list, lock,self.result_signal,self.log_signal)
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
        #此处删除一个逗号

        #d.write(']')
        #d.close()
        '''
           try:
            with open("F:/python/job_of_python/ershoufang/New_Ver/Crawling_demo_3.json", "r") as fp:
              di = json.load(fp)
        except Exception as e:
            print('json格式转化失败')
        
        '''


        self.log_signal.emit('爬取数据结束')
        self.finished_signal.emit()#发射信号




class CrawlWindow(QWidget):
    log_signal_log=pyqtSignal(str)
    def __init__(self):
        super(CrawlWindow,self).__init__()
        self.resize(1600,800)
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
        self.MySQLinsert_init()






    #保存到数据库
    def combobox_slot(self,text):
        if text=='存入MySQL':
            self.save_to_MySQL_2()

    def save_to_MySQL(self):
        dbconn = DataBase_Connect.open_connect()
        cursor = dbconn.cursor()


        try:
            with open("F:/python/job_of_python/ershoufang/New_Ver/Crawling_demo_3.json", "r") as fp:
                di = json.load(fp)
                DataInsert.Insert_Data(dbconn,di)
                QMessageBox.Information(self,'已将爬取的json文件存入数据库',QMessageBox.Ok)#提示已将数据存入数据库
        except Exception as e:
            print('json格式转化失败')
    def save_to_MySQL_2(self):
        dbconn=DataBase_Connect.open_connect()
        cursor=dbconn.cursor()

        for row in range(self.table.rowCount()):
            name = self.table.item(row,0).text()
            #print(name)
            location=self.table.item(row,1).text()
            total_price=self.table.item(row,2).text()
            unit_price=self.table.item(row,3).text()
            house_type=self.table.item(row,4).text()
            floor=self.table.item(row,5).text()
            construction_area=self.table.item(row,6).text()
            house_structure=self.table.item(row,7).text()
            inner_area=self.table.item(row,8).text()
            building_type=self.table.item(row,9).text()
            house_orientation=self.table.item(row,10).text()
            building_structure=self.table.item(row,11).text()
            renovation=self.table.item(row,12).text()
            ladder_ratio=self.table.item(row,13).text()
            elevator=self.table.item(row,14).text()
            year_of_property_rights=self.table.item(row,15).text()
            year=self.table.item(row,16).text()
            lng=self.table.item(row,17).text()
            lat=self.table.item(row,18).text()
            subway=self.table.item(row,19).text()
            gov=self.table.item(row,20).text()
            cursor.execute(
                'insert into the_second_house_final_f_t values(' + str(row) + ',"' + name + '","' + location + '","' + total_price+ '","' + unit_price + '","' + house_type + '","' + floor + '","' + construction_area + '","' + house_structure + '","' + inner_area + '","' + building_type + '","' + house_orientation + '","' + building_structure + '","' + renovation + '","' + ladder_ratio + '","' + elevator + '","' + year_of_property_rights + '","' + year + '","' + lng + '","' + lat + '","' + subway + '","' + gov + '")')
            dbconn.commit()
            self.log_signal_log.emit('将'+name+'存入数据库成功')
        self.log_signal_log.emit('导入数据库完成')

        cursor.close()
        dbconn.close()
    def MySQLinsert_init(self):
        self.log_signal_log.connect(self.set_log_slot)
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
        save_list=['另存为','存入MySQL']
        self.save_combobox.addItems(save_list)
        self.save_combobox.setEnabled(False)
        self.save_combobox.currentTextChanged.connect(self.combobox_slot)
    def table_init(self):
        self.table.setColumnCount(21)
        self.table.setHorizontalHeaderLabels(['小区名称','小区地点','总价','单价','房屋户型','所在楼层','建筑面积','户型结构','套内面积','建筑类型','房屋朝向','建筑结构','装修情况','梯户比例','配备电梯','产权年限','建筑年代','纬度','经度','地铁距离','政府距离',])
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
            for c in g_crawl_list:
                c.stop()
            for p in g_parse_list:
                p.stop()

            print("线程终止")
    def finish_slot(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.save_combobox.setEnabled(True)
        self.crawl_thread.terminate()
    def set_log_slot(self,new_log):
        self.log_browser.append(new_log)
    def set_result_slot(self,name,location,total_price,unit_price,house_type,floor,construction_area,house_structure,inner_area,building_type,house_orientation,building_structure,renovation,ladder_ratio,elevator,year_of_property_rights,year,lng,lat,subway,gov):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row,0,QTableWidgetItem(name))
        self.table.setItem(row, 1, QTableWidgetItem(location))
        self.table.setItem(row, 2, QTableWidgetItem(total_price))
        self.table.setItem(row, 3, QTableWidgetItem(unit_price))
        self.table.setItem(row, 4, QTableWidgetItem(house_type))
        self.table.setItem(row, 5, QTableWidgetItem(floor))
        self.table.setItem(row, 6, QTableWidgetItem(construction_area))
        self.table.setItem(row, 7, QTableWidgetItem(house_structure))
        self.table.setItem(row, 8, QTableWidgetItem(inner_area))
        self.table.setItem(row, 9, QTableWidgetItem(building_type))
        self.table.setItem(row, 10, QTableWidgetItem(house_orientation))
        self.table.setItem(row, 11, QTableWidgetItem(building_structure))
        self.table.setItem(row, 12, QTableWidgetItem(renovation))
        self.table.setItem(row, 13, QTableWidgetItem(ladder_ratio))
        self.table.setItem(row, 14, QTableWidgetItem(elevator))
        self.table.setItem(row, 15, QTableWidgetItem(year_of_property_rights))
        self.table.setItem(row, 16, QTableWidgetItem(year))
        self.table.setItem(row, 17, QTableWidgetItem(lng))
        self.table.setItem(row, 18, QTableWidgetItem(lat))
        self.table.setItem(row, 19, QTableWidgetItem(subway))
        self.table.setItem(row, 20, QTableWidgetItem(gov))
        self.progressbar.setValue(row+1)





if __name__=='__main__':
    app=QApplication(sys.argv)
    window=CrawlWindow()
    window.show()
    sys.exit(app.exec_())