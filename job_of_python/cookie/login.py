import urllib.request
import urllib.parse
'''
header = {

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'Cookie': 'anonymid=jsec5j19kx87sy; wp_fold=0; depovince=GS; jebecookies=6731028e-f4ca-49f0-9c70-5a143eb4424d|||||; _r01_=1; JSESSIONID=abc9pqFo8zfKmbiLpepKw; ick_login=34f362df-2912-4414-bc89-c3779b8f2512; _de=14ADE3C9C0F656C72D2D4872F8512B03; p=729a2658dda3432fd42c1440b3b3472a2; first_login_flag=1; ln_uact=13016985988; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=12767354b0402cb10b977f74e518f78a2; societyguester=12767354b0402cb10b977f74e518f78a2; id=969817042; xnsid=f0eec444; loginfrom=syshome; jebe_key=b68fd2dc-e796-43cf-a77d-00b7125bb605%7C886810e6f5f4327b7bd238e6a56e92c8%7C1550735982266%7C1%7C1550735981716'


}
url = 'http://www.renren.com/969817042/profile'
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request)
print(response.read().decode())

'''






'''

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019141641142'
form_data = {

'email':'13016985988',
'icode':'',
'origURL':'http://www.renren.com/home',
'domain':'renren.com',
'key_id':'1',
'captcha_type':'web_login',
'password':'67b7fb56fa6039865b56e5c8e4972c585048ad77e8f4a38aecfac3e92070d3a0',
'rkey':'16adeb344c1be5466a7a7fa374129963',
'f':'http%3A%2F%2Fwww.renren.com%2F969817042%2Fprofile'

}
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

}
form_data_encode = urllib.parse.urlencode(form_data).encode()
request = urllib.request.Request(url=post_url,headers=header)
response = urllib.request.urlopen(request,data=form_data_encode)
print(response.read().decode())
#登陆成功后，再发get请求进入登录后的页面
get_url = 'http://www.renren.com/969817042/profile'
request = urllib.request.Request(get_url,headers= header)
response = urllib.request.urlopen(request)
print(response.read().decode())
#这样不行，要通过代码，将cookie存储起来，然后用cookie登陆登录后的页面

'''




'''


#用代码存储cookie
import http.cookiejar
#第一步，创建cookie的对象
cj = http.cookiejar.CookieJar() # 用来保存cookie
#第二步，通过cookiejar 创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
#第三步，根据handler创建opener
opener = urllib.request.build_opener(handler)



post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019141641142'
form_data = {

'email':'13016985988',
'icode':'',
'origURL':'http://www.renren.com/home',
'domain':'renren.com',
'key_id':'1',
'captcha_type':'web_login',
'password':'67b7fb56fa6039865b56e5c8e4972c585048ad77e8f4a38aecfac3e92070d3a0',
'rkey':'16adeb344c1be5466a7a7fa374129963',
'f':'http%3A%2F%2Fwww.renren.com%2F969817042%2Fprofile'

}
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

}
form_data_encode = urllib.parse.urlencode(form_data).encode()
request = urllib.request.Request(url=post_url,headers=header)
#response = urllib.request.urlopen(request,data=form_data_encode)
#改
response=opener.open(request,data=form_data_encode)
#第一次发一个post,服务端会为你设置cookie，会保存到opener的cj里
print(response.read().decode())
#登陆成功后，再发get请求进入登录后的页面
get_url = 'http://www.renren.com/969817042/profile'
request = urllib.request.Request(get_url,headers= header)
#response = urllib.request.urlopen(request)
#改
response = opener.open(request) #因为上一次请求已经保存了cookie，所以这次使用这个opener请求响应时会带着那个保存的cookie

print(response.read().decode())



'''


