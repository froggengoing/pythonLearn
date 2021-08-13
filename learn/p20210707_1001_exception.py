# 自定义异常
class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value * 2


# 异常
try:
    try:
        value = int(input('请输入数字'))
    # 多个异常使用逗号分隔 并放在括号里
    except (IOError, Exception) as e:
        print('输入错误：', e)
    # 没有异常的时候会执行
    else:
        if value > 5:
            print(value)
            raise MyException('不能大于5,')
        print(value)
    # 不管有没有异常都会执行
    # 如果有异常会在finally后执行
    finally:
        print('finished')
except Exception as e:
    print(e)