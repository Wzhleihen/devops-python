import json

d = {'name': 'tom', 'age': 25, 'interest': ('movie', 'music'), 'class': ['python']}
# 元组会自动转为数组
x = json.dumps(d)

print(type(x), x)