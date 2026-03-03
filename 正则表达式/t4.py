# 分割

import re
s = """
os.path.abspath(path)
normpath(join(os.getcwd(), path)).
"""

# split() 默认使用 \s+ 分割
# 把每行单词提取出来
print(s.split()) # 做不到['os.path.abspath(path)',
# 'normpath(join(os.getcwd(),', 'path)).']

# print(re.split('[\.()\s,]+', s))

print(*filter(None, re.split('[\.()\s,]+', s)))