from shutil import copyfile, copyfileobj, copy, copy2, copytree
import shutil
from pathlib import Path

# copyfileodj 核心代码，操作文件对象，复制内容
# copyfile 判断文件是否相同，核心调用copyfileodj
# copy copyfile 复制内容，copymode  rwx权限
# copy2 copyfile 复制内容，copymode，copystat 复制内容和所有元数据

# 在windows上，要加r前缀，防止转义
src = r"G:\SRE\devops-python\code\文件IO\a"
dst = r"G:\SRE\devops-python\code\文件IO\dst"

# 如果目标文件夹存在，先删除,否则copytree会报错, 加上True，删除非空文件夹
# shutil.rmtree(dst, True)
# copytree(src, dst)
# 递归复制文件夹及其内容
# dirs_exist_ok=True 目标文件夹存在时覆盖


# def fn(x, y):
#     #  ['b', 'b1', 'b2', 'b3']
#     print(x, type(x), y)
#     return x


# copytree(src, dst, ignore=fn)

shutil.rmtree(dst, True)
# copy文件同时，排除文件，不用全部复制
def fn(x, names):
    # s = set()
    # #  ['b', 'b1', 'b2', 'b3']
    # for name in names:
    #     if name.endswith(".py"):
    #         print(name)
    #         s.add(name)
    # return s
    # 优化成解析式
    # return {name for name in names if name.endswith(".py") }
    return set(filter(lambda name: name.endswith(".py"),names))
    # 使高阶函数把逻辑抽象出去，变成一个活的逻辑，根据用户的定义去写
    # copytree(src, dst, ignore=fn)中 ignore返回几个参数？最后应该返回什么类型？这些是要会的

copytree(src, dst, ignore=fn)
print(*Path(dst).rglob("*"),sep="\n")
