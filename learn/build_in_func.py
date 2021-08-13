#!/usr/bin/python3

# 返回绝对值
print(abs(-500))
print('===========================')
# all(iterable)
# iterable -- 元组或列表。
# 如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
print(all([1, 2, 3, 4, 5, 6]))  # 列表
print(all([1, 2, 3, 0, 5, 6]))
print(all((1, 2, 3, 4, 5, 6)))  # 元祖
print(all((1, 2, 3, 0, 5, 6)))
print('===========================')
# iterable -- 元组或列表。
# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
print(any([0, 0, 0, 0, 0, 5]))
print('===========================')
# ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串,
# 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。
print(ascii("我"))
print(ascii('runoob'))
print('===========================')

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
print(bin(10))

print('===========================')
print(bool(10))
print(bool(-1))
print(bool(0))
print(bool(False))
print(bool(None))
print(bool(''))
print('===========================')
# chr() 用一个整数作参数，返回一个对应的字符。
# 10 进制也可以是 16 进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)。
# 当前整数对应的 ASCII 字符。
print(chr(112))
print(chr(256))
print(chr(0x56))
print(chr((5 * 16 + 6)))
print(chr(8364))
print('===========================')


# classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
# 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
class Class_Method_Test(object):
    bar = 1

    def fun1(self):
        print(self.bar)

    @classmethod
    def fun2(cls):
        print(cls.bar)
        cls().fun1()


Class_Method_Test.fun2()
print("====")
Class_Method_Test().fun2()
print("====")
Class_Method_Test().fun1()
print('===========================')


# delattr(clz, 'foobar') 相等于 del clz.foobar。
class Coordinate:
    x = 10
    y = 20
    z = 30


point1 = Coordinate()
print(point1.x)
delattr(Coordinate, 'x')
print(point1.z)
# 触发作物
# print(point1.x)
print('===========================')
# help() 函数用于查看函数或模块用途的详细说明。
help(compile)
print('===========================')
# dict() 返回字典
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# **kwarg表示字段形式入参的不定长参数
print(dict(a=1, b=2, c=3, ))
print(dict(zip(['one', 'two', 'three'], [1, 2, 3]))) #对比下面使用list输出
dict([('one', 1), ('two', 2), ('three', 3)])
print('===========================')
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 我们可以使用 list() 转换来输出列表。
zip_value = zip(['one', 'two', 'three'], [1, 2, 3])
print(list(zip_value))
# 元素个数与最短的列表一致
zip_value = zip(['one', 'two', 'three'], [1, 2, 3, 4, 5])
print(list(zip_value))
#与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
a,b=zip(*zip(['one', 'two', 'three'], [1, 2, 3, 4, 5]))
print(list(a))
print(list(b))
print('===========================')
#返回模块的属性列表。
print(dir([]))
print('===========================')
#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
# 组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
seq=['one','two','three']
for i,value in enumerate(seq):
    print(i,value)
print('===========================')
#把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
print(type(divmod(7, 2)))
print('===========================')
file=open("D:\\[4]pyProject\\p1\\123.txt")
print(file.read())
print('===========================')
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
def is_odd(n):
    return n%2==0
newList=filter(is_odd,[1,2,3,4,5,6])
for value in newList:
    print(value)
print('===========================')
print(float('123.12'))
print("你好")