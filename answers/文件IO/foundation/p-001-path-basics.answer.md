# 答案：p-001-path-basics

## 参考实现（示意）
```python
from pathlib import Path
import os

p = Path("G:/SRE/devops-python/code/文件IO/path-damo01.py")
print(p.name, p.stem, p.suffix, p.parent)

print(os.path.join(str(p.parent), "a", "b"))
print(p.parent / "a" / "b")
```

## 边界说明
- 建议统一使用 `Path` 以减少字符串拼接错误。
- Windows 下原始字符串可减少转义干扰。
