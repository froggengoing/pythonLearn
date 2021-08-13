# number、string、tuple为不可变类型
# 值传递，对传参修改，对原来的值没有影响
def change(a):
    print(id(a))
    a = 10
    print(id(a))


a = 5
print(id(5))
change(a)
print(id(a))

## string也是值传递
print("------str-------")


def changeStr(s: str):
    print(s)
    print(id(s))
    ns = s.replace('34', "000")
    print('新生产的str：', ns)
    print(s)
    print(id(s))


b = '123456'
print(id(b))
changeStr(b)
print(id(b))

# list为引用传递
print("------list-------")


def changeList(l: list):
    l.append([2, 3, 4])


l1 = [0, 1]
print(l1)
print(id(l1))
changeList(l1)
print(l1)
print(id(l1))


# 关键字参数
def pringStr(a, b):
    print(a, " : ", b)


pringStr(b='我是b', a='我是a')


# 默认值
def printDefaultStr(s1='默认值', s2='前面有默认值，后面的参数有必须有默认值'):
    print(s1, '==', s2)


printDefaultStr()


# 不定长参数，tuple
def printTuple(s1, *t1):
    print(s1, "==", type(t1))
    for value in t1:
        print(value)


# 不定长参数，dict
def printDict(s1, **d1):
    print(s1, '==', type(d1))
    for k, v in d1.items():
        print(k, '=', v)


printTuple('元祖不定长参数：', 2, 3, 4, 'hello')
printDict('字典不定长参数：', a=2, b=3, hello=4)


# 星号单独出现，则后面的参数都必须使用关键字参数
def printSingle(a, b, *, c):
    print(a, b, c)


# 运行期报错
# printSingle(1, 2, 3)
# 星号后的参数必须使用关键字
printSingle(1, 2, c=3)

# lambda 只能访问自己的参数列表，不能访问其他变量
# lambda 主体是一个表达式，只能做有限的逻辑封装
y1 = lambda x1, x2: x1 + x2
print(y1(2,4))

def func1():
    return 1

print(func1())
