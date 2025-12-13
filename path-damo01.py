# 常见的路径操作

# 获取文件名称
print(__name__)
print(__file__)

import os

# 获取当前文件的绝对路径
parent = os.path.dirname(__file__)  # 获取当前文件的父目录
# 用于创建绝对路径拼接
print(os.path.join(os.path.dirname(__file__), "code"))
print("=" * 30)


# 遍历目录
parent = os.path.dirname(__file__)
print(parent)
while parent != os.path.dirname(parent):
    parent = os.path.dirname(parent)
    print(parent)


# Python 3.8+ 的解决方案（了解即可） 后面使用 pathlib 模块
while parent != (new_parent := os.path.dirname(parent)):
    parent = new_parent
    print(parent)
""" 
:=：赋值表达式（海象运算符）
一次计算，多处使用
更高效、更清晰
⚠️ 但：
Python 3.8 之前不能用
教学阶段 不建议广泛使用
"""
