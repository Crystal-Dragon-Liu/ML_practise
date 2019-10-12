'''import requests
import json
import time
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
header = {
#  'Accept': 'application/json, text/javascript, */*; q=0.01',
#  'Accept-Encoding': 'gzip, deflate, br',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'Connection': 'keep-alive',
#   'Content-Length': '25',
#   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': '_ga=GA1.2.348973812.1548917094; user_trace_token=20190131144454-b754b1d6-2523-11e9-b895-5254005c3644; LGUID=20190131144454-b754b75f-2523-11e9-b895-5254005c3644; _gid=GA1.2.1698486268.1548917094; hasDeliver=0; index_location_city=%E5%85%A8%E5%9B%BD; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; WEBTJ-ID=20190201160502-168a816f29d52c-093a014949c51d-b781636-2073600-168a816f29ebae; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1548983156,1548990953,1548991768,1549008303; _gat=1; LGSID=20190201160502-13ed2ab5-25f8-11e9-b899-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E9%2588%258E%25E7%25B6%25B2%26rsv_spt%3D1%26rsv_iqid%3D0xe857fbc5000d3deb%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D8%26rsv_sug1%3D8%26rsv_sug7%3D101%26rsv_sug2%3D0%26inputT%3D1538%26rsv_sug4%3D2276; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; _putrc=ECAEC3E3E8C1020C123F89F2B170EADC; JSESSIONID=ABAAABAAAFCAAEG920362C722CEA41B264772DC5912ACDB; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B75988; gate_login_token=07591a03cceca4bc9bd62bcf39cbd814012445a92053d6ef773dd75e0d59fc52; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549008317; LGRID=20190201160516-1c248583-25f8-11e9-bf34-525400f775ce; SEARCH_ID=b09cb322ce1a4df18c5ddc2d264d7431',
'Host': 'www.lagou.com',
#  'Origin': 'https://www.lagou.com',
'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#  'X-Anit-Forge-Code': '0',
#  'X-Anit-Forge-Token':'None',
#  'X-Requested-With':'XMLHttpRequest'

}
data = {
    'first':True,
    'pn':'1',
    'kd':'python'
}
h = requests.post(url=url,headers=header,data=data)
print(h.status_code)
time.sleep(1)
result = h.json()
print(result)
'''
'''
header = {
        'Host':'bj.lianjia.com',
        'Referer':'https://bj.lianjia.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=sousuo&ljref=pc_sem_baidu_ppzq_x',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
import requests
url = "https://bj.lianjia.com/ershoufang/pg2/"
res = requests.get(url,headers=header).text
'''
import urllib.request

'''url = 'http://www.baidu.com'
# send the request
response = urllib.request.urlopen(url=url)
'''

#response.read() #讀取内容，是二進制格式
#response.geturl()
#response.getheader()
#response.getcode() 獲取狀態碼
#response.readlines() 按行讀取
#print(response.getheaders())
'''image_url = 'https://www.baidu.com/img/bd_logo1.png?qua=high&where=super'
image_url_1 = 'http://file.fangao.cc/flash02.jpg'
response = urllib.request.urlopen(url=image_url_1)
with open('fangao.jpg','wb') as fp:
    fp.write(response.read())
'''
'''
with open('baidu.html','w',encoding='utf8') as fp:
    fp.write(response.read().decode())
'''

# image_url_2 = 'http://desk.fd.zol-img.com.cn/t_s1920x1080/g5/M00/0C/08/ChMkJ1wjXBmIcH-JAAzzJdTYUmgAAuALwAeeN8ADPM9256.jpg'




# urllib.request.urlretrieve(image_url_2,'spider.jpg')


import urllib.parse
import urllib.request
# url衹能由特定的字符組成，字母，數字，下劃綫
# 如果出現其他如中文，要編碼

'''
url = 'http://www.baidu.com/index.html?name=狗蛋&pwd=1223456'
ret = urllib.parse.quote(url) # 編碼
# print(ret)
ret = urllib.parse.unquote(url) # 解碼
# print(ret)
data = {
    "name":"A",
    "age":16

}'''
# 遍歷字典,在url後面加東西
# 第一種笨辦法
'''
list= []
for k,v in data.items():
    list.append(k+"=" + str(v))
    query_string = '&'.join(list)
url = url + '?' + query_string

'''
#第二種
'''
query_string = urllib.parse.urlencode(data)
url = url +'?' + query_string

print(url)

'''

'''
#生成url
word = input("input a keyword : ")
url = 'http://www.baidu.com/s?'
data = {

    "ie":"utf-8",
    "f":8,
    "rsv_bp":0,
    "rsv_idx":1,
    "tn":"baidu",
    "wd":word
}
query_string = urllib.parse.urlencode(data)
print(query_string)
url += query_string
print(url)
#生成html文件
response = urllib.request.urlopen(url)
filename = word+'.html'
with open(filename,'wb') as fp:
    fp.write(response.read())


'''
'''
url = 'http://www.baidu.com/'
#add / to be the compete url
response = urllib.request.urlopen(url)
print(response.read().decode())


'''

 #構建請求對象

# urllib.request.Request()
'''
header = {
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'


}
url = 'http://www.baidu.com/'
request =urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request)
print(response.read().decode())



'''
import requests

'''
url = "http://bj.lianjia.com/ershoufang/"
header = {
'Host':'bj.lianjia.com',
        'Referer':'https://bj.lianjia.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=sousuo&ljref=pc_sem_baidu_ppzq_x',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'Cookie': 'lianjia_uuid=d008fd9a-e8f3-4876-b5b5-fe0e46ef7ca5; _smt_uid=5c544e53.54491df4; UM_distinctid=168a951f5c9752-03ec8c29aaeb1d-b781636-1fa400-168a951f5ca1fe; _ga=GA1.2.1760907363.1549028952; _jzqx=1.1549882905.1549882905.1.jzqsr=bj%2Elianjia%2Ecom|jzqct=/ershoufang/.-; ljref=pc_sem_baidu_ppzq_x; select_city=110000; all-lj=3d0b35ab17a07d475f1852d271de56f8; lianjia_ssid=891ee7a6-e2b3-409e-b1f7-734199cf3dca; TY_SESSION_ID=762d3fbd-9e15-4e60-8ce2-a32d65e65ba1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1549205375,1549444182,1549881007,1550401013; CNZZDATA1253477573=1813032561-1549026602-https%253A%252F%252Fwww.baidu.com%252F%7C1550395665; _jzqa=1.1508165168149026800.1549028947.1549882905.1550401014.7; _jzqc=1; _jzqy=1.1549028947.1550401014.5.jzqsr=baidu.jzqsr=baidu|jzqct=%E9%8F%88%E5%AE%B6%E7%B6%B2; _jzqckmp=1; _qzjc=1; CNZZDATA1254525948=1500743320-1549023703-https%253A%252F%252Fwww.baidu.com%252F%7C1550397732; CNZZDATA1255633284=1641699023-1549025429-https%253A%252F%252Fwww.baidu.com%252F%7C1550397582; CNZZDATA1255604082=535039947-1549024894-https%253A%252F%252Fwww.baidu.com%252F%7C1550397739; _gid=GA1.2.1878986908.1550401016; _qzja=1.1900676550.1549028947383.1549882904766.1550401013587.1550401015787.1550401037048.0.0.0.39.7; _qzjb=1.1550401013587.3.0.0.0; _qzjto=3.1.0; _jzqb=1.3.10.1550401014.1; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1550401037'
}
response = requests.get(url = url, headers=header,verify=False)
print(response.status_code)
with open('lianjia.html','wb') as fp:
    fp.write(response.content)


'''
'''
# 關於證書的解決
import ssl
ssl._create_default_https_context = ssl._create_unverified_context()
'''







'''
post_url = 'https://fanyi.baidu.com/sug'
# 構建post表單
word = input("input a keyword: ")
fro_data = {

    'kw':word



}

# 發送請求
header = {



    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',


}


#發送請求
requests = urllib.request.Request(post_url,headers=header)
#post直接寫表單數據會報錯，需要處理一下

form_data = urllib.parse.urlencode(fro_data).encode()
#順便變成字節類型
response  = urllib.request.urlopen(requests,data=form_data)
print(response.read().decode())

'''
import urllib.request
import urllib.parse
'''

post_url = 'https://fanyi.baidu.com/v2transapi'

header = {
'Host': 'fanyi.baidu.com',
'Connection': 'keep-alive',
'Content-Length': '119', # 發送請求時瀏覽器算出來的内容長度，如果值不對，請求就失敗了，所以盡量別加
'Accept': '*/*',
'Origin': 'https://fanyi.baidu.com',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'https://fanyi.baidu.com/?aldtype=85',
#'Accept-Encoding': 'gzip, deflate, br',  這裏代表壓縮格式，應該省掉這個頭，因爲我不會解壓
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'BAIDUID=C31000BD531C57D6E02FAA2ABF0E8DB0:FG=1; BIDUPSID=C31000BD531C57D6E02FAA2ABF0E8DB0; PSTM=1546599415; BDUSS=RTNEVLdmQyM1ZDaU50OHpDNUdwbE8xWlhhdFVucUN4UjJ-SDIwM2Y1dzNSVzljQVFBQUFBJCQAAAAAAAAAAAEAAACjMA6AWkpETE1NMTk5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADe4R1w3uEdcTD; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1550478235,1550478270,1550495621; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1550495621; H_PS_PSSID=1460_21108_26350'




}
data = {


    'from':'en',
    'to':'zh',
    'query':'baby',
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'72100.391829',# 加密簽名
    'token':'94e1108832e0dd5ad077c02db4bc3348' # 加密
}

request = urllib.request.Request(url=post_url,headers=header)
data_encode = urllib.parse.urlencode(data).encode()
response = urllib.request.urlopen(request,data=data_encode)
print(response.read().decode())

'''















'''

# ajax get
douban_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
# 可以觀察出，第一頁是20， limit是一次刷的電影數量
page = int(input("想要第幾頁的數據 ： "))
number = 20
data = {

    'start':(page -1)* number,
    'limit':number

}
#拼接url 將字典轉化爲query_string
query_string = urllib.parse.urlencode(data)
douban_url  +=query_string
header = {

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'



}

request = urllib.request.Request(url=douban_url,headers=header)
response = urllib.request.urlopen(request)
print(response.read().decode())



'''












'''
KFC_URL = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers = {


'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
request = urllib.request.Request(url=KFC_URL,headers=headers)
city = input("要查看餐廳所在的城市 ： ")

for page in range(1,30) :
  
  from_data = {

  'cname': city,
  'pid':'' ,
  'pageIndex': page,
  'pageSize':'10'


              }
  from_data_encode = urllib.parse.urlencode(from_data).encode()

  response = urllib.request.urlopen(request,data=from_data_encode)
  print(response.read().decode()+"\n")

'''












'''
url_set = {



}
#循环 依此爬取每一页

tieba_url = 'http://tieba.baidu.com/f?ie=utf-8'
#输入起始页码，输入结束页码，在当前文件夹中创建一个以吧名为名的文件夹
import os


ba_name = input("请输入要爬取的吧名 : ")
start_page = int(input("请输入要爬取的初始页码: "))
end_page = int(input("请输入结束页码 : "))
# 创建文件夹
if not os.path.exists(ba_name):

  os.mkdir(ba_name)

for page in range(start_page,end_page+1) :
  #page就是当前页

  data= {

    'kw':ba_name,
    'pn':(page-1)*50

  }
  data_url = urllib.parse.urlencode(data)
  tieba_url += data_url
  url_set[page] = tieba_url
  print(tieba_url+"\n")
  tieba_url = 'http://tieba.baidu.com/f?ie=utf-8'
  header = {

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

}
  print('第%s页开始下载' % page)
  request = urllib.request.Request(url_set[page])
  response = urllib.request.urlopen(request)
  #生成文件名
  filename = ba_name +'_' + str(page) + ".html"
  filepath = ba_name +'/' +filename
  #写
  with open(filepath,'wb') as fp:
    fp.write(response.read())
  print('第%s页结束下载' % page)


'''


#代理
#正向代理：替客户端发送请求，代理客户端获取数据
#反向代理：代理服务端提供数据

#配置：
#浏览器配置

   
#代码配置












'''
#URLError和HTTPError类都在urllib.error中
#异常练习

url_error = 'https://blog.csdn.net/zcf1784266476/article/details/7133594'
try:

  response = urllib.request.urlopen(url=url_error)
  print(response)

except urllib.error.HTTPError as e:
  print(e)
  print(e.code)
except urllib.error.URLError as e :
  print(e)
#两个同时捕获时，将HTTPerror写在上面，HTTPerror 是URLerror的子类






#handler 处理器、自定义Opener

#   urlopen()  给一个URL， 发送请求，获取响应，无法自己定制头部



1'''
import urllib.error
import urllib.request
import urllib.parse


#Request

url = 'http://www.baidu.com/'

header = {

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

}











'''
#handler
#创建headler
handler = urllib.request.HTTPHandler()
#通过handler创建一个opener
opener = urllib.request.build_opener(handler)
#opener是一个对象，一会发送请求的时候，直接使用opener的方法即可
#构建请求对象
requests = urllib.request.Request(url,headers=header)

#发送请求
response = opener.open(requests)
print(response.read().decode())


'''


'''#ip 101.89.132.131  80
#代码配置代理
import urllib.request
import urllib.parse
#创建handler
handler = urllib.request.ProxyHandler({'http':'101.89.132.131:80'})
opener = urllib.request.build_opener(handler)
data = {
    'wd':'东莞'

}
url = 'https://www.baidu.com/s?ie=UTF-8&wd=IP'
query_string = urllib.parse.urlencode(data)
url+=query_string
print(url)

header = {

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

}
request = urllib.request.Request(url,headers=header)
response = opener.open(request)
with open('dong.html','wb') as fp:
    fp.write(response.read())
    
    '''
