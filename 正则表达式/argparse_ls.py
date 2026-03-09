'''
要求
实现 ls 命令功能：
- `-a` 和 `--all`：显示包含 `.` 开头的文件
- `-l`：详细列表显示
- `-h` 和 `-l` 配合，人性化显示文件大小，例如 1K、1G、1T 等，可以认为 1G=1000M

'''
import argparse
import os
import stat
import time

parser = argparse.ArgumentParser('ls',add_help=False, description='show file list')

parser.add_argument('path', nargs='?', default='.', help='path to list')
parser.add_argument('-a', '--all', action='store_true', help='show all files')
parser.add_argument('-l', action='store_true', help='show detail list')
parser.add_argument('-h', action='store_true', help='human readable')

args = parser.parse_args()

path = args.path


def human_size(size):
    units = ['B', 'K', 'M', 'G', 'T']
    for u in units:
        if size < 1000:
            return f"{size}{u}"
        size /= 1000
    return f"{size:.1f}P"


files = os.listdir(path)

# 处理 -a
if not args.all:
    files = [f for f in files if not f.startswith('.')]

for f in files:
    fullpath = os.path.join(path, f)

    if args.l:

        st = os.stat(fullpath)

        mode = stat.filemode(st.st_mode)
        size = st.st_size

        if args.h:
            size = human_size(size)

        mtime = time.strftime(
            "%Y-%m-%d %H:%M",
            time.localtime(st.st_mtime)
        )

        print(mode, size, mtime, f)

    else:
        print(f)