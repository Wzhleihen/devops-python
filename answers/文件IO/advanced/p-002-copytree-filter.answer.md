# 答案：p-002-copytree-filter

## 参考实现（示意）
```python
from shutil import copytree, rmtree
from pathlib import Path

src = Path("G:/SRE/devops-python/code/文件IO/a")
dst = Path("G:/SRE/devops-python/code/文件IO/dst")

rmtree(dst, True)

def ignore_fn(dirpath, names):
    return {n for n in names if n.endswith('.py') or n == '__pycache__'}

copytree(src, dst, ignore=ignore_fn)
print(*dst.rglob('*'), sep='\n')
```

## 边界说明
- 若保留目标目录，Python 3.8+ 可使用 `dirs_exist_ok=True`。
