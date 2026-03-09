import argparse
import os

parser = argparse.ArgumentParser('ws', add_help= True, description='统计文件字符数')

# 定义获取文件读取
parser.add_argument('path1', nargs='?',help='iupte file name')

# 定义参数
parser.add_argument('-l',  help='lines')
parser.add_argument('-w',  help='words')
parser.add_argument('-c',  help='characters')


args = parser.parse_args()
print(args)

if args.path1:
    with open(args.path1, 'r') as f:
        if args.l:
            print(len(f.readlines()))
        if args.w:
            print(len(f.read().split()))
        if args.c:
            print(len(f.read()))
else:
    print('file not found')
