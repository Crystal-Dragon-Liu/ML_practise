from bs4 import BeautifulSoup
#转化本地文件
#soup = BeautifulSoup(open('本地文件‘))
#转化网络文件
#soup = BeautifulSoup('字符串类型或字节类型’，‘lxml'）

#生成对象
soup = BeautifulSoup(open('exer.html',encoding='utf8'),'lxml')
# print(soup)
print(type(soup)) #可以看出这个soup是BS的一个对象，而不是字符串，只是其中封装了string方法
#根据标签名进行查找
#print(soup.a)
#print(type(soup.a)) #<class 'bs4.element.Tag'> 通过标签名查找，只能找到的是第一个a标签内容
#print(soup.a['href']) #用此办法获得属性的内容
#print(soup.a['target'])
#print(soup.a['title'])
#print(soup.a.attrs) #打印所有（属性：值）的字典
#print(soup.a.html) 不对
#print(soup.a.string)#获取属性内容
#print(soup.a.text)#获取属性内容
#print(soup.a.get_string)#获取属性内容
#测试

#print(soup.div.text)

'''
result 


        安慕希
        希腊风味酸奶
巴氏杀菌
        黄桃+燕麦

'''
#print(soup.div.string)
'''
result
 
 
 div标签中要是还有其他标签的话
 就是none
 如果div中只有字符串，就显示字符串
 string比较脆弱
 


'''
#print(soup.div.get_text)

'''
result

<bound method Tag.get_text of <div>
        安慕希
        <p>希腊风味酸奶</p>
<p>巴氏杀菌</p>
        黄桃+燕麦

    </div>>


'''
'''


soup.find('a') #找到第一个符合要求的a标签
print(soup.find('a',title='qing'))
print(soup.find('a',class_='four'))
print(soup.find('a',id="feng"))

'''

#soup的对象也能使用find,去指定的div里面去查找符合要求的节点
#find找到的都是第一个符合要求的标签
'''
div = soup.find('div',class_="tang")
print(div.find('a',class_="zong"))

'''

#print(soup.findAll('a'))
#findall也可以一级一级找
'''
div = soup.find('div',class_="tang")
print(div.find_all('a'))


'''
'''
div = soup.find('div',class_="tang")
#print(div.find_all(['a','div']) #找到所有的div和a
print(div.find_all('a',limit=2)) #找到所有的a,取前两个
'''


#select
#根据选择器 选择指定的内容
#常见的选择器：标签选择器，类选择器，id选择器组合选择器层级选择器伪类选器属性选择器

#   .dudu
#  #kaka
#    a,.dudu,.meme,#lala 组合选择器
#层级选择器
#     div .dud #lala .meme .xixi  可以下面好多级
 #  div >p >a > .lala  只能是下面一级，结构清晰

#print(soup.select('.song'))
#print(soup.select('div > li > a > .aa'))
#print(soup.select('.aa')[0].text) #要加下标0
#print(soup.select('.aa')[0]['href'])
#select 选择器返回的永远是列表
div = soup.find('div',class_="tang")
#在div里用select找东西
print(div.select('.four')[0].text)
