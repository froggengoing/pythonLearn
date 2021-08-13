import keyword

# 单行注释
'''
多行注释
多行注释
'''
if True:
    print('true')
print('我是''最棒的')
print('hello',
      'world')
a = 4
b = 2
c = a + \
    b
print(c)
# print(keyword.kwlist)
e = ['1',
     '2', '3']
print(e)
f = (1,
     2,
     3)
print(f)
g = {1,
     2,
     3}
print(g)
s = "hello"
print(s * 3)
str = '123456789'
# [2,6)步长为2，结果35
print(str[2:6:2])
# [2,8)截取,默认步长为1,结果345678
print(str[2:8])
# [2,最后),步长为1，3456789
print(str[2:])
# [2,-1),从第二位到倒数第二位
print(str[2:-1])
# 下表为8的字符
print(str[8])
print("数字：" + str)
print("重复数字：" + str * 2)
print("hello");print("world")
str2="""我是多行文本
我是第二行
我是第三行
"""
print(str2)
n1 = 100
if n1 < 1000:
    print(True)
import sys
print(sys.path)
from sys import path
print(path)

