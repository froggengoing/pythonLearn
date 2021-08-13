list = [1, 2, 4, 6]

# iter创建迭代器对象
# next访问元素
# 访问超过元素数量后，抛StopIteration
it = iter(list)
n = 0
try:
    while n := next(it):
        print(n)
except StopIteration:
    pass
print('over!!')

# 迭代器更多使用for访问，自动处理StopIteration
for value in it:
    print(value)


# 自定义迭代器
# 需要实现__iter__() 和 __next__()
class MyNumbers:

    def __iter__(self):
        self.a = 10
        # 必须返回迭代器
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        # 触发 StopIteration 异常来结束迭代
        if x > 15:
            raise StopIteration
        return x


num = MyNumbers()
itNum = iter(num)
print(next(itNum))
print("---")
for value in iter(num):
    print(value)


# 神奇的yield
print("神奇的yield")
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        n, a, b = n + 1, b, a + b
f1=fab(5)
for value in f1:
    print(value)
