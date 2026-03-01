# 作业
# 复制目录
# 选择一个已存在的目录作为当前工作目录，
# 在其下创建a/b/c/d这样的子目录结构并在这些子目录的不同层级生成50个普通文件，
# 要求文件名由随机4个小写字母构成。
#
# 将a目录下所有内容复制到当前工作目录dst目录下去，要求复制的普通文件的文件名必须是x、y、z开头。举例。假设工作目录是/tmp，构建的目录结构是/tmp/a/b/c/d。
# 在a、b、C、d目录中放入随机生成的文件，这些文件的名称也是随机生成的。最终把a目录下所有的目录也就是b、C、d目录，和文件名开头是x、y、z开头的文件。

from pathlib import Path
import shutil
from string import ascii_lowercase
import random

#防止重复执行 删除临时目录
shutil.rmtree('tmp', ignore_errors=True)

base = Path('tmp')
src =  Path('a/b/c/d')

# 创建基础目录
(base / src).mkdir(parents=True, exist_ok=True)

# 创建 50 文件
sdir = [src] + list(src.parents)[:-1]
for name in range(50):
    file_name = ''.join(random.sample(ascii_lowercase, 4))
    (base / random.choice(sdir) / file_name).touch()

# print(list(base.glob('**/*')), sep='\n')

# 定义 一个函数，该函数接受一个目录路径和一个文件名列表作为参数，并返回一个文件名列表，该列表包含所有以x、y、z开头的文件名。
headers = set('xyz')
def ignore_files(src, names):
    # return {name for name in names
    #         if name[0] not in headers and Path(src , name).is_file()
    #         }
    return set(filter(lambda name: name[0] not in headers and Path(src , name).is_file(), names))

# 拷贝
shutil.copytree(str( base / 'a'), str( base / 'dst'), ignore=ignore_files)

# 遍历目标文件
print(*list((base / 'dst').rglob('*')), sep='\n')