# 声明与构造方法
class annimal:

    def __init__(self, name):
        self.name = name

    def hello(self):
        print('hello', self.name)

    def run(self, speed=20):
        print('i can run fast', speed)


an = annimal('cat')
an.hello()


# 多继承
class action:
    def run(self, speed=10):
        print('i can run fast', speed)


class Cat(annimal, action):
    def __init__(self, name):
        super().__init__('iam' + name)

    def eat(self):
        print('i like eat fish')


c = Cat('cat')
c.hello()
c.eat()
c.run()
print('------')


# 重写
class SubCat(Cat):
    def eat(self):
        super(SubCat, self).eat()
        print('sub cat eat small finsh')


c2 = SubCat('sub_cat')
c2.hello()
c2.eat()

print('------')


# 私有变量与方法
class Dog(annimal, action):
    age = 0
    __count = 0

    def __private_method(self):
        print('cannot call outside')


do = Dog('dog')
print(do.age)


# 私有变量不可访问
# print(do.__count)
# 私有方法不可访问
# do.__private_method()

# 类变量
# 类变量定义在类中且在函数体之外。
# 类变量通常不作为实例变量使用。
# 类变量在整个实例化的对象中是公用的。
class Pig(annimal):
    age = 5
    __count = 5

    def add(self):
        Pig.__count += 1

    def getCount(self):
        return Pig.__count


p1 = Pig('pig')
print(p1.age)
# 运行时动态添加类属性
Pig.runtimeField = 'hello world'
print(p1.runtimeField)
# 类变量不属于对象，可以直接修改。
Pig.age = 20
print(p1.age)
print(p1.getCount())
#
p2 = Pig('pig2')
p2.add()
# 修改的类变量，对所有对象实例都影响
print(p1.getCount())


class Sheet(annimal):
    '''
    实例变量
    '''
    var3 = 'class_var3'

    def runtimeVar1(self):
        self.var1 = 'var1'

    def runtimeVar2(self):
        self.var2 = 'var2'
        self.var3 = 'var3'


s3 = Sheet('pig')
# 运行时动态添加对象变量
s3.runtimeVar = 'var'
print(s3.runtimeVar)
# 赋值对象变量
s3.runtimeVar2()
print(s3.var2)
# 同时存在对象属性和类属性，优先调用对象属性
print(s3.var3)
# 调用未赋值对象变量，报错
# print(s3.var1)
# 类专有方法或属性

print(s3.__class__)
print(type(s3.__class__))
print(type(s3))

print(s3)


# 类似java的toString
class Tiger(annimal):
    def __str__(self):
        return 'i ma ' + self.name

    def __repr__(self):
        return 'from repr : i am ' + self.name


t1 = Tiger('tiger')
print(t1)
# 与上面直接调用等同
print(str(t1))
print(repr(t1))
# 与repr写法相同
print('%r' % t1)


class CallTest:

    def __call__(self, *args, **kwargs):
        print('call object directly:' + args[0])


callOb = CallTest()
# 允许像方法一样直接调用对象
callOb('123')


# _eq_
class EqTest:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id


eq14 = EqTest(14)
eq14_2 = EqTest(14)
eq13 = EqTest(13)
print(eq14 == eq14_2)
print(eq13 == eq14)
