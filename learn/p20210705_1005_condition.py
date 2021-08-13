a = 200
if a < 100:
    print(True)
elif 100 < a < 200:
    print('大于100小于200')
else:
    print('大于等于200')

a = 200
b = 200.0
if (a == b):
    print("相等")

# while循环
w1 = 10
w0 = 0
sum = 0
while (w0 := w0 + 1) < w1:
    sum += w0
else:
    print(sum)
# # 无限循环
# while True:
#     var = int(input("请输入整数"))
#     print('你输入的是：', var)
# for in
for value in ['a', 'b', 'c']:
    print('list:', value)
for value in ('x', "y", "z"):
    print('tuple:', value)
for k,value in dict({('a',1),('b',2)}).items():
    print('dict：',k,'=',value)
for value in range(2,5):
    print(value)
# pass
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")