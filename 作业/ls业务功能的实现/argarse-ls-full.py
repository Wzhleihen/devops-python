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


# 参数调用
parser.print_help()  # usage: ls [-h] [-a] [-l] [path]
print("=" * 30)

args = parser.parse_args(["-lars"])

print("=" * 30)

# 功能实现


# 添加size 计算
def _gethuman(size: int):
    units = " KMGTP"
    depth = 0
    while size >= 1024 and depth < len(units) - 1:
        size /= 1024
        depth += 1
    return f"{size:.1f}{units[depth] if depth else ''}"


# print(_gethuman(10240000))


def _listdir(path, all, detail, human):
    p = Path(path).absolute()
    for f in p.iterdir():
        if not all and f.name.startswith("."):
            continue
        if not detail:
            yield (f.name,)
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
                        size,
                        mtime,
                        f.name,
                    ),
                )
            )


# 添加排序功能
def listdir(path, all=False, detail=False, reverse=False, human=False):

    yield from sorted(
        _listdir(path, all, detail, human), key=lambda x: x[-1], reverse=reverse
    )
