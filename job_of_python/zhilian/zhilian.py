import urllib.request
import urllib.parse
import json
import time
import xlwt
from bs4 import BeautifulSoup


#https://sou.zhaopin.com/?jl=635&sf=0&st=0&kw=Python&kt=3
#https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=635&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.51945765&x-zp-page-request-id=b626f2609ac242e4ae197262c0614530-1551001756258-686152
#https://sou.zhaopin.com/c/i/sou?pageSize=90&cityId=635&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java&kt=3&_v=0.18022491&x-zp-page-request-id=c3eda47f19054802b151dbdb2a7ef8e0-1551002498128-323351
#https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=635&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java&kt=3&_v=0.52361649&x-zp-page-request-id=3b1638bca9e044dea1fe451690a6a1b9-1551011340525-85187
class ZhaoPin(object):
    url = 'https://fe-api.zhaopin.com/c/i/sou?'
    items =[]

    def __init__(self, jl, kw, start_page, end_page):
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page



    #拼接指定url,生成请求对象
    def handle_request(self,page):
       #拼接并编码
       data = {
           'start':(page-1)*90,
           'pageSize':'90',
           'cityId':'635',
           'workExperience':'-1',
           'education':'-1',
           'companyType':'-1',
           'employmentType':'-1',
           'jobWelfareTag':'-1',
	       'kw':self.kw,
           'kt':'3',


       }
       url_now = self.url + urllib.parse.urlencode(data)
       print(url_now)
       #构建请求对象
       headers={

           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
           'Cookie': 'adfbid=0; adfbid2=0; ZP_OLD_FLAG=false; dywec=95841923; sajssdk_2015_cross_new_user=1; sts_deviceid=1691e88a2a8443-05efb25ec2bb82-b781636-2073600-1691e88a2a9620; sts_sg=1; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0E3w90KqiAs0ARZFT00000rXdj-C00000IoUQN6.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15yRduHf1rHbvnj0snj9hnyf0IHdjn1DsnjKawjR1nRndPYfvwH0zwb7Knb7awWK7rDwan0K95gTqFhdWpyfqn1D4PHczPjb3PiusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1Ydn1bdn0%26tpl%3Dtpl_11535_18778_14772%26l%3D1510913511%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3195224985_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D228%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D3121; __utmc=269921210; _jzqc=1; _jzqckmp=1; acw_tc=3ccdc15815509956375931621e27d8e7c5c9ef9114f3566a9cf659cf4ee7ca; jobRiskWarning=true; LastCity=%E5%8D%97%E4%BA%AC; LastCity%5Fid=635; dywea=95841923.2964615747507528700.1550995465.1551001397.1551010358.3; __utmt=1; sts_sid=1691f6be529e5-0a7221de28b951-b781636-2073600-1691f6be52a5f2; _jzqa=1.1257878145966947600.1550995465.1550995465.1551010359.2; _jzqy=1.1550995465.1551010359.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.-; _jzqb=1.1.10.1551010359.1; __xsptplus30=30.2.1551010359.1551010359.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23f1yz2snX57iEWJFDP4_4FVX1gxQ6r8bo%23; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221026556290%22%2C%22%24device_id%22%3A%221691e88a211fea-017976b64b1091-b781636-2073600-1691e88a2135df%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%221691e88a211fea-017976b64b1091-b781636-2073600-1691e88a2135df%22%7D; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; dywez=95841923.1551010368.3.4.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utma=269921210.1596512407.1550995465.1551010359.1551010368.4; __utmz=269921210.1551010368.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1550995465,1551010359,1551010368; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1551010377; dyweb=95841923.4.10.1551010358; __utmb=269921210.3.10.1551010368; ZL_REPORT_GLOBAL={%22/resume/new%22:{%22actionid%22:%22795f65ea-c948-4177-bb3e-0bd491311afb%22%2C%22funczone%22:%22addrsm_ok_rcm%22}%2C%22sou%22:{%22actionid%22:%22d244ab6c-5071-48cf-93a6-7d7802c5501b-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22//jobs%22:{%22actionid%22:%2290ebfc43-f56d-47e7-927c-fd21065d27cc-jobs%22%2C%22funczone%22:%22dtl_best_for_you%22}}; sts_evtseq=13'
       }
       request = urllib.request.Request(url_now,headers=headers)


       return request

    def parse_content(self,jsonb):
        for row in range(len(jsonb["data"]["results"])):
         list = {
            '职位名称':jsonb["data"]["results"][row]["jobName"],
             '工资':jsonb["data"]["results"][row]["salary"],
             '工作经验需求':jsonb["data"]["results"][row]["workingExp"]["name"],
             '所需学历':jsonb["data"]["results"][row]["eduLevel"]["name"],
             '福利': jsonb["data"]["results"][row]["welfare"],
             '全职/兼职':jsonb["data"]["results"][row]["emplType"],
            '公司名称':jsonb["data"]["results"][row]["company"]["name"],
            '公司总人数':jsonb["data"]["results"][row]["company"]["size"]["name"],
             '工作地点':jsonb["data"]["results"][row]["city"]["display"],

             '更新日期':jsonb["data"]["results"][row]["timeState"]


         }
         self.items.append(list)
        return self.items





    def run(self):
        for page in range(self.start_page,self.end_page+1):
            print("----------正在爬取第%s页--------"% page)
            response = self.handle_request(page)
            #发送请求，获取内容
            content = urllib.request.urlopen(response).read().decode()
            #别忘了看编码

            #print(type(content))

            jsonb = json.loads(content)
            #print(jsonb)
            result = self.parse_content(jsonb) #解析内容

            print('----------第%s页爬取结束--------'% page)
            time.sleep(2)
        print(result)
        strr = json.dumps(result,ensure_ascii=False)

        with open('zhilian1.text','w',encoding='utf8') as fp:
            fp.write(strr)
def main():


    #需要输入一些信息
    '''
    jl = input("input the location u want : ")
    kw = input('input the keyword of your work : ')
    start_page = int(input("请输入要爬取的初始页码: "))
    end_page = int(input("请输入结束页码 : "))

    '''
    jl = '南京'
    kw = 'Python'
    start_page = int(input("请输入要爬取的初始页码: "))
    end_page = int(input("请输入结束页码 : "))
    #创建一个对象 ，启动爬取
    spider = ZhaoPin(jl,kw,start_page,end_page)
    spider.run()

if __name__ == '__main__':


        main()
