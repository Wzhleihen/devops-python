# 答案：p-001-regex-basics

## 参考实现（示意）
```python
import re

text = """2026-04-18 host=10.0.0.1\n2026-04-19 host=192.168.1.2"""
ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
print(ips, dates)
```

## 边界说明
- 分组会改变 `findall` 返回结构（字符串列表 vs 元组列表）。
