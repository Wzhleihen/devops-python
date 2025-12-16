from pathlib import Path
import os

os.chdir(r"C:\Users\19058\Desktop\SRE\devops-python\code\文件IO")

p3 = Path("a")
print(p3.cwd())
# 查看文件夹是否存在
print(p3.exists())  # 返回 True

# 当文件夹不存在时创建文件夹，避免报错
if not p3.exists():
    p3.mkdir(parents=True)
