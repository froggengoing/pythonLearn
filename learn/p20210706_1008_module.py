# 导入自定义模块式，from 文件夹名 import 模块名
from learn import p20210706_1007_func
from learn.p20210706_1006_iter import fab
from learn  import  p20210706_1009_module
from . import p20210705_1004_string
from ..tushareLearn import company
import  sys
# 搜索模块文件的路径
print(sys.path)
p20210706_1007_func.printSingle(1,2,c=3)
fab(10)
print(dir())



