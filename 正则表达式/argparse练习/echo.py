import argparse

parser = argparse.ArgumentParser(prog='echo', description='echo')

# 获取内容
parser.add_argument(
    'content',
    nargs='*',
    help='content to be echoed'
)

# 不换行参数
parser.add_argument(
    '-n',
    '--no-newline',
    action='store_true',
    help='do not output the trailing newline'
)

args = parser.parse_args()

print(args)
print(*args.content, end='' if args.no_newline else '\n')
# if args.no_newline:
#     print(*args.content, end='')
# else:
#     print(*args.content)
