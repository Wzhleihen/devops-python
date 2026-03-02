import re

# # 建议模式先编译，然后使用
# regex = re.compile('\d') # py使用re模块，模式一般都有进行先编译，要不然每次使用都会重新编译，效率较低


s = """bottle\nbag\nbig\napple"""
for i, c in enumerate(s, 1):
    print((i-1, c), end='\n' if i % 7 ==0 else '\t')
print()

# enumerate()函数，用于遍历序列，返回索引和值，
# end参数用于指定输出的结束符，
# \t和\n是转义字符，分别表示制表符和换行符
#  方便查看对应位置的字符

m = re.match('^a', s)
print(type(m), m)

regex = re.compile('^a', re.M)
m = regex.match(s)
print(type(m), m)