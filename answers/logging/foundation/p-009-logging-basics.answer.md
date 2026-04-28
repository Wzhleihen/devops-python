# P-009 logging 三层体系基础训练 — 参考答案

📎 回链：`daily/day24.md`  
📅 日期：2026-04-28

---

## 第一题：Logger + Handler + Formatter

```python
import logging

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

# Handler 1: 控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))

# Handler 2: 文件
fh = logging.FileHandler("app.log", encoding="utf-8")
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s"))

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("这是 debug 消息")
logger.info("这是 info 消息")
logger.warning("这是 warning 消息")
logger.error("这是 error 消息")
```

**要点**：Logger 决定"是否记录"（level 门槛），Handler 决定"往哪输出"（各自也有 level 门槛），Formatter 决定"输出格式"。

## 第二题：EffectiveLevel 验证

```python
import logging

root = logging.getLogger()
root.setLevel(logging.WARNING)

myapp = logging.getLogger("myapp")
myapp_db = logging.getLogger("myapp.db")

print(f"root       level={root.level}, effective={root.getEffectiveLevel()}")
print(f"myapp      level={myapp.level}, effective={myapp.getEffectiveLevel()}")
print(f"myapp.db   level={myapp_db.level}, effective={myapp_db.getEffectiveLevel()}")
```

**输出**：
```
root       level=30, effective=30
myapp      level=0,  effective=30
myapp.db   level=0,  effective=30
```

**解释**：
- `myapp.db` 的 level 为 NOTSET(0)，沿 parent 找到 `myapp`，仍为 NOTSET(0)，继续找到 root，level=30(WARNING)。
- 查找路径：`myapp.db` → `myapp` → `root`（第一个非 NOTSET 的就是 EffectiveLevel）。

## 第三题：避免 Handler 重复

```python
import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(ch)
    return logger

log = setup_logger("test")
log = setup_logger("test")
log = setup_logger("test")
print(len(log.handlers))  # 1
log.info("只输出一次")
```

**要点**：`getLogger` 同名返回同一实例，但 `addHandler` 不会去重，所以需要手动检查。
