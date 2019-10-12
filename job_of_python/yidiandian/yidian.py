#将标题和内容保存到html文件中


import urllib.request
import urllib.parse
import re




def handle_request(url,page=None):
    if page!=None:
      url = url+ str(page) + '.html'
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    #打印一下url看对不对
    print(url)
    request = urllib.request.Request(url=url,headers=header)
    return request








def get_text(a_href):
    request = handle_request(a_href)

    #发送请求，获得响应
    content = urllib.request.urlopen(request).read().decode()
    #解析内容
    pattern = re.compile(r'<div class="neirong">(.*?)</div>',re.S)
    lt = pattern.findall(content)
    #如果不写这个正则，内容里的图片标签会保留但不会显示，因为url不完整，所以索性全部删掉,将清空多余垃圾后的text返回
    text = lt[0]
    pat = re.compile(r'<img .*?>',re.S)
    text = pat.sub('',text)

    return text







def parse_content(content):
    # 可以先粘贴标签，在分析怎么用正则
   #pattern = re.compile(r'<a href="/lizhi/qianming/20190241246.html"><b>我不知道年少轻狂，我只知道胜者为王——追梦赤子心</b></a>')
   pattern = re.compile(r'<a href="(/lizhi/qianming/\d+\.html)"><b>(.*?)</b></a>')
   lt = pattern.findall(content)
   '''
   print(lt)
   print(len(lt))
   '''
   for href_title in lt :
       #获取内容的连接
       a_href = 'http://www.yikexun.cn' + href_title[0]
       #获取标题
       title = href_title[1]
       #print(a_href)
       #print(title)

   #还取出a标签中的链接，发出请求取得内容，列表中的元素都是元组，元组中第一个元素就是第一个小括号匹配到的内容，第二个元素同理

       
       text = get_text(a_href)
       string = '<h1>%s</h1>%s' % (title,text)
       with open('lizhi.html','a',encoding='utf-8') as fp: #写w的话，每次往里面写都会先清空以前的内容，换成a即可,参数为b时，只能写入二进制
           fp.write(string)                                #默认是gbk,要用utf-8,否则是乱码









def main():
    quotation_url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'

    start_page = int(input("Input the start page : "))
    end_page = int(input("input the end page : "))
    for page in range(start_page,end_page + 1):
#根据URL和page去生成指定的request

        request = handle_request(quotation_url,page)
        #发送请求
        content= urllib.request.urlopen(request).read().decode()#此处应留一手细节，F12查看网站的编码
        #解析内容
        parse_content(content)

if __name__ == '__main__':
   main()