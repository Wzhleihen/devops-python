# ls /etc/
# ls -a /etc/  ls -lah ls --all -h
# ls -ls -h  /etc/    ls /etc -la -h


import argparse
from pathlib import Path
from datetime import datetime


parser = argparse.ArgumentParser("ls", add_help=True, description="show file list")
parser.add_argument(
    "path", nargs="?", default=".", help="dir name"
)  # 位置参数，默认值为当前目录
parser.add_argument(
    "-a", "--all", action="store_true", help="show all files"
)  # 可选参数，默认值为False
parser.add_argument(
    "-l", "--long", action="store_true", dest="detail", help="show long listing"
)  # 可选参数，默认值为False

# 附加题：排序
parser.add_argument("-r", "--reverse", action="store_true", help="reverse sort order")

# 添加size显示功能
parser.add_argument(
    "-s", "--size", action="store_true", dest="human", help="show file size"
)

# print("=" * 30)
# args = parser.parse_args("-h")
# print(args)

# print("=" * 30)


parser.print_help()  # usage: ls [-h] [-a] [-l] [path]
print("=" * 30)

args = parser.parse_args(["-lars"])

print(args)
print(args.all, args.detail, args.path)
print("=" * 30)

# 在处理一些工作的活，需要一些shell脚本，但是shell脚本效率太低而且不便于到时错
# 在生产环境中，是看什么东西效率最高，而且保证我们尽量不出错，应该用对应语言（py，ts）等


# def listdir(path):
#     p = Path(path).absolute()
#     # for f in p.iterdir():
#     # print(f, str(f), f.name)  # str(f) 以防有地方字符不兼容
#     # print(f.name)  # 以防有地方字符不兼容
#     # if not all and f.name.startswith("."):  # 如果不是all，并且文件名以.开头，则跳过
#     #     continue
#     # yield f.name
#     # yield from (f.name for f in p.iterdir() if not (not all and f.name.startswith(".")))
#     # yield from (f.name for f in p.iterdir() if all or not f.name.startswith("."))
#     # 如果是all，或者文件名不以.开头，则返回文件名
#     # if all or not f.name.startswith(".") 逻辑思路：all 或者不是以.开头的文件才返回文件名
#     # not (not all and f.name.startswith(".")) 逻辑思路：不是（不是all并且文件名以.开头）才返回文件名， 等同于上面一句
#     yield from map(
#         lambda f: f.name,
#         filter(lambda f: all or not f.name.startswith("."), p.iterdir()),
#     )
#     # 对于大批量的文件，使用filter和map函数可以提高效率，因为它们是惰性求值的，不会一次性加载所有文件到内存中，而是逐个处理文件
#     """
#     解释：filter函数的第一个参数是一个函数，第二个参数是一个可迭代对象。f
#     ilter函数会对可迭代对象中的每个元素调用第一个参数函数，如果返回True，则保留该元素，否
#     则丢弃该元素。这里的lambda函数就是第一个参数函数，它接受一个文件对象f，如果all为True或者文件名不以.开头，
#     则返回True，否则返回False。这样就实现了根据all参数来过滤文件列表的功能。
#     map函数的第一个参数是一个函数，第二个参数是一个可迭代对象。map函数会对可迭代对象中的每个元素调用第一个参数函数，
#     """


# print(*listdir(args.path), sep="\n")


# def listdir(path, all=False, detail=False):
#     p = Path(path).absolute()
#     for f in p.iterdir():
#         if not all and f.name.startswith("."):
#             continue
#         if not detail:
#             yield f.name
#         else:

#             # drwxr-xr-x 1 hyms 197609    0 Apr 23 11:55 ls业务功能的实现/
#             st = f.stat()
#             # print(st)
#             mtime = datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
#             # yield (st.st_mode, st.st_nlink, st.st_uid, st.st_gid, st.st_size, mtime, f.name)
#             yield " ".join(
#                 map(
#                     str,
#                     (
#                         st.st_mode,
#                         st.st_nlink,
#                         st.st_uid,
#                         st.st_gid,
#                         st.st_size,
#                         mtime,
#                         f.name,
#                     ),
#                 )
#             )


# 添加size 计算
def _gethuman(size: int):
    units = " KMGTP"
    depth = 0
    while size >= 1024 and depth < len(units) - 1:
        size /= 1024
        depth += 1
    return f"{size:.1f}{units[depth] if depth else ''}"


# print(_gethuman(10240000))


def _liostdir(path, all, detail, human):
    p = Path(path).absolute()  # 获取绝对路径 absolute() 以防输入相对路径时出错
    for f in p.iterdir():  # 遍历目录下的文件和子目录
        if not all and f.name.startswith("."):
            continue
        if not detail:
            yield (f.name,)  # 如果不显示详细信息，则只返回文件名
        else:

            # drwxr-xr-x 1 hyms 197609    0 Apr 23 11:55 ls业务功能的实现/
            st = f.stat()
            # print(st)
            import stat

            mode = stat.filemode(st.st_mode)
            mtime = datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            size = _gethuman(st.st_size) if human else st.st_size
            # yield (st.st_mode, st.st_nlink, st.st_uid, st.st_gid, st.st_size, mtime, f.name)
            yield " ".join(
                map(
                    str,
                    (
                        mode,
                        st.st_nlink,
                        st.st_uid,
                        st.st_gid,
                        # st.st_size,
                        size,
                        mtime,
                        f.name,
                    ),
                )
            )


# 添加排序功能
def listdir(path, all=False, detail=False, reverse=False, human=False):

    yield from sorted(
        _liostdir(path, all, detail, human), key=lambda x: x[-1], reverse=reverse
    )


print(*(listdir(args.path, args.all, args.detail, args.reverse, args.human)), sep="\n")


# 33206 1 0 0 5.9K 2026-04-23 14:04:39 argparse-ls-instantiation_demo01.py
# 参考：改变33206 为drwxr-xr-x

""" 
import shutil
shutil.copy
shutil.copy2
"""
