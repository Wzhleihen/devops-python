import re

# # 建议模式先编译，然后使用
# regex = re.compile('\d') # py使用re模块，模式一般都有进行先编译，要不然每次使用都会重新编译，效率较低

s = """bottle\nbag\nbig\napple\nable"""
for i, c in enumerate(s, 1):
    print((i-1, c), end='\n' if i % 7 ==0 else '\t')
print()

# enumerate()函数，用于遍历序列，返回索引和值，
# end参数用于指定输出的结束符，
# \t和\n是转义字符，分别表示制表符和换行符
#  方便查看对应位置的字符

# 单次匹配
# match() 函数， 默认必须从0处开始匹配上，或指定位置开始匹配
# search()函数，在字符串中搜索匹配的模式，返回第一个匹配的对象 ，从0或者指定位置开始匹配
# fullmatch()函数，要求全长匹配，一个不落(如果指定字符串范围，字符串也要匹配)

# # search
# # m = re.match('^a', s)
# # m = re.search('^a', s, re.M)  # re.M表示多行匹配
# m = re.search('^b', s)  # search()函数为全局匹配，从头开始匹配
# print(type(m), m)

# regex = re.compile('^b', re.M)
# m = regex.search(s, 1)  # 从第1个位置开始匹配,即返回第二个b
# print(m)


# # fullmatch
# m = re.fullmatch('b.*', s, re.M | re.S)
# print(m)

# regex = re.compile('^bag', re.M)
# m = regex.fullmatch(s, 7, 10)  # # 要完全匹配，多了少了都不行, [7, 10)
# print(m)


# 全文匹配
# findall()函数，在文本中，全文搜索多次，返回数据类型为list，元素为匹配的子串
# 如果有分组，1组返回的是分组的子串，多组返回字符串元组，元组中元素一定是组匹配的内容
# finditer()函数，返回所有匹配的子串的迭代器，元素为匹配的对象

# # findall
# m = re.findall('b\w+', s)
# print(type(m), m)

# for x in m:
#     print(type(x), x)
# print('=' *  30)

# regex = re.compile('b\w+', re.M)
# for x in regex.finditer(s):
#     print(type(x), x)


# # 分组findall
# x = re.findall(r'b(\w+)', s)
# for i in x:
#     print(type(i), i)

# # finditer
# m = re.finditer('b\w+', s)
# print(type(m), m)

# for x in m:
#     # print(type(x), x, x[0]) # py 3.6+ 支持
#     print(type(x), x, x[0], s[x.start():x.end()])

# x.start() 返回匹配的起始位置
# x.end() 返回匹配的结束位置
# x.span() 返回匹配的起始和结束位置

# 分组finditer
# x = re.finditer('(b\w+)\s(b\w+)\s(b\w+)', s)
# for i in x:
#     print(type(i), i, i.groups())

x = re.match('(b\w+)\s(?P<name2>\w+)\s(?P<name3>\w+)', s)
print(x.groups())
print(x.groupdict())
print(x[1],x.group(2))

# 正则匹配语法： \w 匹配字母、数字、下划线 ，\s 匹配空白字符
# 返回的是对象，不是字符串


'''
<class 'callable_iterator'> <callable_iterator object at 0x000001BB12DD4730>
<class 're.Match'> <re.Match object; span=(0, 6), match='bottle'> bottle bottle
<class 're.Match'> <re.Match object; span=(7, 10), match='bag'> bag bag
<class 're.Match'> <re.Match object; span=(11, 14), match='big'> big big
'''

## 匹配替换
# sub()函数，在文本中，全文搜索多次，返回替换后的对象是字符串
# subn()函数，在文本中，全文搜索多次，返回替换后的字符串和替换的次数， 用得比较少


# m = re.sub('b\w+', 'WWW', s, 10)
# print(type(m), m)

# x = re.subn('b\w', 'MMM', s,10)
# print(type(x), x)


# # 分组
# # () 表示分组

# m = re.search(r'(b)(\w+)', s)
# print(m, m[0],  m.group(0))
# print(m.group(1), m.groups())

'''
(\w) 被重复了 5 次
最后一次是 e
所以 group(1) = 'e'
'''

