""" 
我是一个模块
"""

# import os  # 在顶层加载os模块，os为标识符


# print(type(os), os)  # 输出os模块的类型

# # 即使是 frozen 状态，__file__ 依然能定位到对应的源码路径
# # 在 3.11+ 之后，地址都被加载到frozen中，提高了加载速度，减少了内存占用，当前运行版本为3.14
# print(os.stat)  # 输出os模块的属性
# print(os.path, os.path.__file__)  # path是os模块的一个子模块，
# print(os.__file__)  # 输出os模块的文件路径
# print(__name__)  # 输出当前文件的文件名


# import os  # 加载之后，会被dir()方法列出当前模块的所有属性和方法，os模块的属性和方法也会被列出

# print(__name__)
# print(__doc__)  # 输出当前文件的文档字符串
# print(__file__)  # 输出当前文件的路径
# print(dir())  # 输出当前文件的所有属性和方法
# print(sorted(globals().keys()))  # 排序，输出当前文件的全局变量和方法
# print(*globals().items(), sep= '\n')  # 输出当前文件的全局变量和方法的键值对

# print(locals())  # 输出当前文件的局部变量和方法, 这里和 globals() 一样，因为当前文件没有函数和类，局部变量和全局变量一样


'''
基本每个模块都有这些属性
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
__builtins__ : 内置模块，用于提供内置函数和异常
__cached__ : 模块缓存路径
__doc__ : 模块文档字符串
__file__ : 模块文件路径
__loader__ : 模块加载器
__name__ : 模块名称
__package__ : 模块包名
__spec__ : 模块规范
'''



# import os  # 在顶层加载os模块，os为标识符

# def a(x=5):
#     import random  # 在函数内部加载random模块，random为标识符
#     print(dir())  # 取当前环境的所有变量，全局
#     print(sorted(globals().keys()))  
#     print(sorted(locals().keys()))  

# a()

# import os.path  # 通过os.path访问path模块，os为标识符，path为属性，os会出现在全局

# print(dir())  # 输出当前文件的所有属性和方法


# 导入模块几种方式
# import os  # 导入模块，os为标识符, 必须是模块类型，.py或者目录
# from os import path  # 导入模块的属性，path为标识符
# from os.path import *  # 导入模块的所有属性，*为标识符
# import os.path as op  # 导入模块的属性，并给属性起别名，op为标识符
# from pathlib import Path  # 只导入 pathlib的模块

# from 用法
# from 模块 import 函数、类、变量、模块、属性，*  # 导入模块的函数、类、变量、模块、属性，*为批量导入
# from functools import update_wrapper as uw  # 导入模块的属性，update_wrapper为标识符
# print(op.exists(__file__))  # 输出当前文件的路径是否存在

# print(dir())  # 输出当前文件的所有属性和方法

# 例子
# import os  # 导入模块，os为标识符

# # 模块也有自己的全局变量，从os.__dict__中可以查看
# print(os.path.exists)  
# print(*os.path.__dict__.keys(), sep=', ')  
# print(dir(os.path))  # 输出和上面一样
# print(os.path.__dict__['exists']) # 模块的全局变量都放在，该模块的__dict__中，__dict__是一个字典，存放模块的全局变量和方法
# print(getattr(os.path, 'exists'))  # 输出模块的内存地址
# # <built-in function _path_exists>
# # <built-in function _path_exists>







