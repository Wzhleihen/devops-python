# Day 14 - Pickle 序列化与二进制对象读写（完整AI分析版）

📅 日期：2025-12-18  
⏱ 距离上次学习：2 天

---

## ✅ 今日目标
- [x] 理解 `pickle.dump/load` 的对象持久化流程。
- [x] 区分文本序列化（如 JSON）与二进制序列化（如 Pickle/MsgPack）的输出形态。
- [x] 能定位并修复序列化脚本中的路径与文件读取错误。

## 📚 章节内容
- 章节：序列化与反序列化（与文件IO衔接）
- 小节：
  1) Pickle 写入与读取顺序  
  2) 二进制文件句柄与 `rb/wb` 模式  
  3) 相对路径与执行目录的耦合问题
- 学习位置：`序列化与反序列化/t1.py`
- 对应练习：
  - `practice/文件IO/foundation/p-001-path-basics.md`
  - `practice/文件IO/advanced/p-002-copytree-filter.md`
- 对应答案：
  - `answers/文件IO/foundation/p-001-path-basics.answer.md`
  - `answers/文件IO/advanced/p-002-copytree-filter.answer.md`
- 章节总结（3行内）：
  1. 当天提交语义是“pickle 示例更新”，核心在对象写入与按序读取。  
  2. Pickle 面向 Python 对象，强调“读取顺序必须与写入顺序一致”。  
  3. 首个工程化坑是运行目录变化导致相对路径失效。

## 🧾 证据来源（时间线先归档）
- 归档目录检查：未发现 `归档/2025/2025-12-18`。
- 归档缺失，补证来源。
- 补证证据（优先级顺序）：
  1) `daily/_generated/timeline_by_date.json`（2025-12-18：`update  pickle example`）
  2) `daily/_generated/day_mapping_with_policy.json`（day07 映射到 2025-12-18）
  3) `序列化与反序列化/t1.py`（pickle 读写示例）
  4) 提交证据：`945e51c`（2025-12-18）

## 📌 今日内容（代码在做什么）
1. 以 `a/b/c/d` 四类 Python 对象为样本，演示可序列化对象集合。  
2. 通过 `pickle.load()` 连续读取 4 次，验证“同一二进制流中的顺序反序列化”。  
3. 通过示例说明：Pickle 输出是二进制字节流，不是可直接阅读的文本。  
4. 把文件IO阶段的 `with open(..., 'rb')` 复用到反序列化读取流程中。

## 🧠 核心知识（底层原理）
- Pickle 是 Python 专用对象协议，强调“对象结构保真”，不强调跨语言可读性。  
- `dump` 与 `load` 必须在二进制模式下工作：`wb/rb`。  
- 多对象写入一个文件时，读取顺序不可打乱，否则语义会错位。  
- 相对路径默认基于“当前工作目录”，而不是脚本所在目录。

## 💻 关键代码或关键行为
```python
import pickle

filename = 'src.bin'

with open(filename, 'rb') as f:
    for i in range(4):
        x = pickle.load(f)
        print(i, type(x), x)
```

### 行为解释
- 使用 `pickle.load()` 按写入顺序逐个还原对象。  
- 每次 `load` 都从文件指针当前位置继续读取，直到对象边界结束。  
- 若执行目录不对，`filename='src.bin'` 会直接触发文件不存在错误。

## ⚠️ 问题 / 坑（至少一个真实错误案例）
### 案例：运行 `t1.py` 时出现 `FileNotFoundError`
- 错误现象：`FileNotFoundError: [Errno 2] No such file or directory: 'src.bin'`。  
- 根因：脚本使用相对路径，执行时当前工作目录不在 `序列化与反序列化/` 下。  
- 修正：
  - 方案A：在目标目录执行脚本；
  - 方案B：使用 `Path(__file__).with_name('src.bin')` 构造脚本同级绝对路径。  
- 防再犯规则：凡文件脚本进入提交前，统一做一次“跨目录执行”自检。

## 🏋️ 强化训练（练习 / 答案 / 要求）
- 训练目标：把“能跑通 demo”升级为“路径稳健 + 输出可验证”。
- 训练任务：
  1. 基础：完成 `p-001-path-basics`，确保路径拼接与存在性检查稳定；  
  2. 进阶：完成 `p-002-copytree-filter`，加入异常处理与日志输出；  
  3. 迁移：将 Pickle 的输入输出流程封装为 CLI 子命令（参考后续正则/argparse训练）。
- 验收标准：
  - 能在不同工作目录下稳定读到同一 `src.bin`；
  - 提交中至少包含 1 条失败复现记录与修复说明；
  - 关键函数提供输入/输出示例与边界条件说明。

## 📎 practice / answers 回链
- `practice/文件IO/foundation/p-001-path-basics.md`
- `answers/文件IO/foundation/p-001-path-basics.answer.md`
- `practice/文件IO/advanced/p-002-copytree-filter.md`
- `answers/文件IO/advanced/p-002-copytree-filter.answer.md`

## ✅ 完成度自检
- [x] 日期固定为 2025-12-18
- [x] 已执行“先归档证据”并明确标注“归档缺失，补证来源”
- [x] 已包含今日目标 / 章节内容 / 今日内容 / 核心知识 / 关键代码或关键行为
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含基础/进阶/迁移训练与验收标准
- [x] 已包含 practice/answers 回链路径
