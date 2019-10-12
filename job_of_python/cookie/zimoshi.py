import re
'''
string = '<p><div><span>猪八戒</span></div></p>'
pattern = r'<\w+><\w+>\w+</\w+><\w+>' #此时如果string变成<p><div><div>猪八戒</div></div></p>
#也会匹配成功，所以上面 这个pattern不对
pattern_1 = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')
ret = pattern_1.search(string)
print(ret)

#贪婪
string= '<div><div>rulai</div></div></div>'
pattern_1 = re.compile(r'<div>.*</div>')
ret = pattern_1.search(string)
print(ret)
pattern_1 = re.compile(r'<div>.*?</div>')
ret = pattern_1.search(string)
print(ret)
'''
string = '''hate is beautiful feel
love you very much
love she 
love her
'''
#多行匹配
pattern = re.compile(r'^love',re.M)
ret = pattern.findall(string)
print(ret)
string_1 = """<div>沁园春-雪
北国风光
千里冰封
万里雪飘
望长城内外
惟余莽莽
大河上下
顿失滔滔
山舞银蛇
原驰蜡象
欲与天公试比高</div>
"""

#用正则匹配这里面的内容
pattern = re.compile(r'<div>(.*?)</div>',re.S) #/w不能匹配换行


ret = pattern.findall(string_1)
#print(ret)
#替换 re.sub(正则表达式，替换内容，字符串）
string = '''i love you
,you love me
 ,ye
 '''
def fn(a):
      #把匹配的对象拿出来
      ret = int(a.group())
      return str(ret-10)
pattern = re.compile(r'love')
ret = pattern.sub('hate',string)
# ret = pattern.sub(r'love','hate',string) 也可以
#print(ret)
string = "i love the 175 girls"
pattern = re.compile(r'\d+')
ret = pattern.sub(fn,string)
print(ret)