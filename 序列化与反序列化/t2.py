import json
import pickle
import msgpack

# d = {'name': 'tom', 'age': 25, 'interest': ('movie', 'music'), 'class': ['python']}
d = {"name": "tom", "age": 25, "interest": ["movie", "music"], "class": ["python"]}
# 元组会自动转为数组，其实可以禁止元组转为数组
# x = json.dumps(d)

# print(type(x), x)
# with open("json.txt", "w") as f:
#     json.dump(x, f)

# d1 = json.loads(x)
# print(type(d1), d1)
# print(d == d1)  # d.interest是元组，d1.interest是列表，所以不相等
# print(d is d1)  # 每次反序列化都会生成一个新的对象，所以不相等

methods = (json, pickle, msgpack)

for i, m in enumerate(methods):
    x = m.dumps(d)
    print(i + 1, m.__name__, type(x), len(x), x)

# enumerate 是 Python 内置函数，用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

""" 
1 json <class 'str'> 79 {"name": "tom", "age": 25, "interest": ["movie", "music"], "class": ["python"]}
2 pickle <class 'bytes'> 88 b'\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03tom\x94\x8c\x03age\x94K\x19\x8c\x08interest\x94]\x94(\x8c\x05movie\x94\x8c\x05music\x94e\x8c\x05class\x94]\x94\x8c\x06python\x94au.'
3 msgpack <class 'bytes'> 51 b'\x84\xa4name\xa3tom\xa3age\x19\xa8interest\x92\xa5movie\xa5music\xa5class\x91\xa6python'
"""

# 反序列化
print(x)

y = msgpack.loads(x)
y = msgpack.loads(x, raw=False) # 新版，raw=True数据使用bytes类型，raw=False数据使用str类型
print(type(y), y)
print(d == y)  # True
print(d is y)  # False  # 每次反序列化都会生成一个新的对象，所以不相等
