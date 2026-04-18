# Day 10 - `os.path` 路径定位与父目录遍历（归档优先时间线版）

日期：2025-12-13  
距离上次学习：1 天

---

## 今日目标
- [x] 理解 `__file__`、`os.path.dirname()`、`os.path.join()` 的组合用法。
- [x] 能写出“从当前目录逐级向上到根目录”的循环逻辑。
- [x] 识别路径脚本中的真实语法错误，并能快速修正。

## 章节内容
- 章节：文件IO（路径操作）
- 小节：
  1) 当前脚本路径与父目录定位  
  2) `join` 拼接与跨平台路径表示  
  3) 父目录遍历停止条件与海象运算符
- 学习位置：`文件IO/path-damo01.py`、`文件IO/文件IO.ipynb`
- 对应练习：`文件IO/path-damo01.py`
- 章节总结（3行内）：
  1. 重点是从“写死路径”转向“脚本自定位 + 动态拼接”。
  2. 通过循环对照，掌握目录回溯终止条件。
  3. 为后续 `pathlib` 面向对象路径操作打基础。

## 证据来源（归档优先）
- 归档检查：未发现 `归档/2025/2025-12-13`（归档缺失）。
- 补证来源：
  - `文件IO/path-damo01.py`
  - `文件IO/文件IO.ipynb`
  - `作业/文件创建作业.ipynb`（同主题错误样例补证）
  - 提交证据：`986911d6e18078d74d3df84c5ae81dd3bf03841d`（2025-12-13，python os.path 学习）

## 今日内容（代码在做什么）
1. 输出 `__name__`、`__file__`，确认脚本身份与文件位置。  
2. 用 `os.path.dirname(__file__)` 获取父目录，再用 `os.path.join()` 进行路径拼接。  
3. 通过 `while parent != os.path.dirname(parent):` 实现逐级回溯到根目录。  
4. 使用 `new_parent := os.path.dirname(parent)` 改写循环，减少重复调用。

## 核心知识（底层原理）
- `dirname()` 是路径“向上一层”的稳定原语，循环调用可得到祖先目录链。
- `join()` 比手工拼接分隔符更稳健，适合跨平台场景。
- 根目录检测常见写法是“当前目录 == 上一级目录”时停止。
- 海象运算符适用于循环中“先计算后复用”的表达式场景。

## 关键代码（精简）
```python
import os

parent = os.path.dirname(__file__)
while parent != os.path.dirname(parent):
    parent = os.path.dirname(parent)
    print(parent)
```

## 问题 / 坑（真实错误案例）
### 案例：函数定义残缺导致 `SyntaxError`
- 错误现象：`作业/文件创建作业.ipynb` 出现 `SyntaxError: invalid syntax`，定位到单独一行 `def`。  
- 根因：函数定义未写完整（缺函数名/参数/冒号/函数体）。  
- 修正方式：先写最小函数骨架再填逻辑，例如：
  ```python
  def create_tree(base):
      pass
  ```
- 防再犯规则：先保证“可运行骨架”，再增加实现细节。

## 强化训练（练习 / 答案 / 要求）
- 训练目标：把路径脚本从“能跑”提升到“可复用”。
- 训练任务：
  1. 基础：实现 `get_ancestors(path)`，返回当前路径到根目录的链路。  
  2. 进阶：实现 `safe_join(base, *parts)`，并校验结果不越出 `base`。  
  3. 迁移：把 `os.path` 版本改写为 `pathlib` 版本并对齐输出。
- 验收要求：
  - 至少覆盖相对路径、绝对路径、空路径三类输入；
  - 每题记录“输入 / 输出 / 边界条件”；
  - 每题补一条“最易错点 + 如何避免复发”。
- 参考路径：`文件IO/path-damo01.py`、`文件IO/文件IO.ipynb`
- 训练回链：`practice/文件IO/foundation/p-001-path-basics.md`
- 答案回链：`answers/文件IO/foundation/p-001-path-basics.answer.md`

## 我的理解（第一人称）
- 我现在能清楚解释：为什么目录回溯要以“当前目录等于父目录”作为停止条件。  
- 我还模糊的点：路径规范化与权限校验在工程里如何组合最稳妥。  
- 我准备怎么补：下一次把 `safe_join` 和异常路径测试补齐。

## 回链索引
- 关键文件：
  - `文件IO/path-damo01.py`
  - `文件IO/文件IO.ipynb`
  - `作业/文件创建作业.ipynb`
- 关键提交：`986911d6e18078d74d3df84c5ae81dd3bf03841d`
- 证据说明：本日无对应归档目录，已按规则使用补证来源。
