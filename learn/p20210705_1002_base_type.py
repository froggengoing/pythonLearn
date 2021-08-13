a, b, c, d = 100, 100.0, True, 3j + 4
print(a, b, c, d)
print(type(a), type(b), type(d), type(d))
print(d.real)
print(d.imag)
if (a == b):
    print("float==int")
else:
    print("float!=int")

print(isinstance(a, int))
print(isinstance(a, float))

# 列表
l1 = [1, 2, 3, 4, 5, 6, 7]
print(type(l1))
print(l1)
# 截取[1,最后)
print(l1[1:])
# 截取[1,3)
print(l1[1:3])
# 截取[1,-1),-1表示倒数第一
print(l1[1:-1])
# 截取[1,6),步长为2
print(l1[1:6:2])
# 集合相加
print(l1 + l1)
# list重复
print(l1 * 3)

# 长度
print(len(l1))
# 遍历
for value in l1:
    print(value)
# enumerate遍历
for k,v in enumerate(["a",'v',"c"]):
    print('enumerate',k,v)
l1[2] = 10
print(l1)

# 元祖
t1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(t1)
print(t1[2:])
t2 = ()
print(type(t2), " ", t2)
t3 = (2)
print(type(t3), " ", t3)
t4 = (2,)
print(type(t4), " ", t4)
# set
s1 = {1, 2, 4}
print(s1)
# 去除list中重复元素
sl3 = [1, 2, 2, 2, 3]
s2 = set(sl3)
print(s2)
# 空集合创建
print(type(set()))
print(type({}))
# 判断元素是否存在集合
if 2 in s1:
    print('2 存在与集合', s1)
s3 = set('123456')
s4 = set('456789')
s5 = {'456789'}
print(s3)
print(s4)
print(s5)

# 差集
print(s3 - s4)
# 并集
print(s3 | s4)
# 交集
print(s3 & s4)
# 非
print(s3 ^ s4)

# 字典
d1={}
d1['hello']='world'
d1['one']='two'
d2={'one':'one-value','two':'two-value'}
# 遍历
for key in d1.keys():
    print(key," ",d1[key])
for value in d1.values():
    print(value)
for kv in d1.items():
    print(kv)
for kv in d2.items():
    print(kv)
for k, v in d2.items():
    print('第四：',k, v)
# 直接构建字典
d3=dict([('one', 'one-value'),('two', 'two-value')])
for kv in d3.items():
    print(kv)
d4=dict(hello='world',one='two')
for kv in d4.items():
    print(kv)
#神奇的语法
d5={x: x**2 for x in (2, 4, 6)}
for kv in d5.items():
    print(kv)
