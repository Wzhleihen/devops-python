# 分组例子

import re


s =  """ 
name, age, phone
zhangsan, 20, 123456789
lisi, 21, 123456789
wangwu, 22, 123456789
"""

pattern = re.compile(r'(?P<name>\w+),\s*(?P<age>\d+),\s*(?P<phone>\d+)')

for m in pattern.finditer(s):
    print(m.groupdict())