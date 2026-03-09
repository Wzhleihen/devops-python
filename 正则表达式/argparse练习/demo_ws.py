import argparse

parser = argparse.ArgumentParser('ws', add_help= True, description='统计文件字符数')

# 定义获取文件读取
parser.add_argument('file', nargs='?',help='iupte file name')

# 定义参数
parser.add_argument('-l', action="store_true", help='lines')
parser.add_argument('-w', action="store_true",  help='words')
parser.add_argument('-c', action="store_true",  help='characters')

args = parser.parse_args()
print(args)

with open(args.file, "r", encoding="utf-8") as f:
    text = f.read()

lines = len(text.splitlines())
words = len(text.split())
chars = len(text)

# if args.l:
#     print(f'lines:{lines}')
# elif args.w:
#     print(f'words: {words}')
# elif args.c:
#     print(f'chars: {chars}')
# else:
#     print(f'lines: {lines}\nwords: {words}\nchars: {chars}')

options = {
    'l': ('lines', lines),
    'w': ('words', words),
    'c': ('chars', chars)
}

if not (args.l or args.w or args.c):
    for name, value in options.values():
        print(f'{name}: {value}')
else:
    for key, (name, value) in options.items():
        if getattr(args, key):
            print(f'{name}: {value}')