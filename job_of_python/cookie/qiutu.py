import urllib.request
import urllib.parse
import re
import os
import time
url = 'https://www.qiushibaike.com/pic/page/2/'
def handle_request(page,url):  #根据页码生成不同的请求对象
    url += str(page) + '/'
    print(url)
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

    }
    request = urllib.request.Request(url=url,headers=headers)
    return request






def download_image(content):

   '''


   pattern = re.compile(r'<img src="(.*?)" .*?>')
    lt = pattern.findall(content)
    print(lt)
   :param content:
   :return:
       #这样做，会把不符合要求的imgurl也获取，所以要做个限制，如只有在div class = thumb 中的img才符合要求

   '''



   #不需要的元素用.*？不加括号，要用的需要加括号
   # 后面这个不行，不会匹配下一行的东西pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>')
   pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>',re.S)
   lt = pattern.findall(content)
   print(len(lt))
   #依此下载链接

   for image_src in lt:
       image_src = 'https:'+ image_src
       #发送请求下载图片
       dirname = 'qiutu'
       if not os.path.exists(dirname):
           os.mkdir(dirname)
       filename = image_src.split('/')[-1]
       filepath = dirname+'/'+filename
       print('%s图片正在下载。。。。' % filename)
       urllib.request.urlretrieve(image_src,filepath)
       print('%s图片下载完成。。。。' % filename)
       time.sleep(1)
















def main(
):
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入起始页码: '))
    end_page = int(input('请输入结束页码: '))
    for page in range(start_page,end_page+1):
        print('第%s页开始下载' % page)

        #生成请求对象

        request  = handle_request(page,url)
        content = urllib.request.urlopen(request).read().decode()
        #解析内容，提取所有的图片连接，下载图片,用正则

        download_image(content)
        url = 'https://www.qiushibaike.com/pic/page/'
        print('第%s页下载完成' % page)
        time.sleep(2)












if __name__ == '__main__':
        main()