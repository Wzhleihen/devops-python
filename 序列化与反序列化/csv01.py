import csv

rows = [
    ('id', 'name', 'age', 'desc'),
    [1, 2, 3, 4],
    ('2', 'tom', 20, 'tom\' name'),
    ['3', 'jerry', 22, """tom ",brother"""],
    'abcdefg',
    ((1,),2, 'abc')
]

# 使用csv 写入文件，在还原过程中，无法知道原来是什么数据类型，使用情况取决于使用者

# 解决写入csv文件时，出现换行问题，系统自动添加换行符，当前使用newline=''参数解决,
# newline=''参数的作用是控制写入文件时换行符的处理方式，避免在某些平台上出现多余的换行符。
# with open('.\csv01.csv', 'w',newline='') as f:
#     for line in rows:
#         # f.write(",".join(map(str, line)) + '\r\n')
#         print(",".join(map(str, line)), file=f, end='\r\n')

# 使用csv 模块读取csv文件，序列化
# with open('csv01.csv', 'r', newline='') as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(type(line), line)


# 使用csv 模块写入csv文件，反序列化
with open('csv02.csv', 'w', newline='') as f:
    writer = csv.writer(f,)
    writer.writerow(rows[0])  # 单行写入
    writer.writerows(rows[1:])  # 多行写入