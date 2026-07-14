# import m  # 目录也是模块，__init__.py文件是目录的初始化文件，目录也是模块
#
# print(m.X)
# print(m)
# print(dir(m)) # 查看模块中所有属性和方法
# # ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']

# print(m.__dict__) # 查看模块中所有属性和方法，以字典形式展示
# print(type(m)) 

# import t1 
# print(t1.__file__)
# print(dir(t1)) # 查看模块中所有属性和方法
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# 根据包加载原理，包名.模块名，加载子模块，会加载父模块，父模块的__init__.py文件会被执行一次
import m.m1.m12

print(__name__)

import  sys
print(*filter(lambda x:x.startswith('m'), dir()))  # 当前全局变量有谁

print('=' * 30)
# print(sorted(filter(lambda x:x.startswith('m'), sys.modules.keys())))  # 加载了什么模块
print(*sorted(filter(lambda x:x.startswith('_'), reversed(sys.modules.keys()))))  

print(m.m1.m12.X)  # 112


# 模块使用必须加载，加载模块，模块中的代码才会执行，模块中的代码只执行一次，应该在 sys.modules 中查找模块是否已经加载过，加载过就不再加载，直接使用


''' 
问题1：
import os

os.path.exists #能不能访问这个方法? 
 能访问，在os模块中， os.path是一个模块，在全局情况下，os.py已经做了预加载，这种方式不严谨，不推荐依赖隐式导入
 建议做法： import os.path 或者 from os import path
'''