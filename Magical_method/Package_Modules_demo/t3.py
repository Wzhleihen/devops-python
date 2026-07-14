# import t1
# from t1 import Produto, _B, _C, __my
from t1 import *   # 使用 * 默认情况下不会导入有下划线的关键字 ，如果有 __all__ 定义, 则导入 __all__ 定义的


print(*filter(lambda x:not x.startswith('_'), dir()))  # 当前全局变量有谁

print(*filter(None, dir()))  # 当前全局变量有谁

import  sys
# print(sorted(filter(lambda x:x.startswith('m'), sys.modules.keys())))  # 加载了什么模块
print(*sorted(filter(lambda x:not x.startswith('__'), reversed(sys.modules.keys()))))  

print('=' * 30)
# print(t1.__dict__)

import functools