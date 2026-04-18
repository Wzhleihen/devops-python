# Day 19 - `wc`/`mkdir` 命令闭环与幂等目录创建（完整AI分析版）

📅 日期：2026-03-09  
⏱ 距离上次学习：1 天

---

## 📦 证据归档（先归档，后补证）
- 归档目录检查：未发现 `归档/2026/2026-03-09`（归档缺失，已补证）。
- 当天提交语义（优先）：
  1. `ad5904061c2dfdb6558f0ada46cc92a87d81cc21`：`添加mkdir 练习命令，实现创建目录功能。`
  2. `071ed1b10bca2cc5c8d6514f8ee9b0306940e381`：`更新ws`
  3. `fcc8e72261c610cde01bd7d636768a1a89b811c6`：合并提交（辅助证据）
- 与语义直接对应的代码证据：
  - `正则表达式/argparse练习/demo_mkdir.py`（mkdir 命令实现）
  - `正则表达式/argparse练习/demo_ws.py`（wc 统计脚本）
  - `正则表达式/argparse练习/题目.md`（练习 2：wc，练习 3：mkdir）
- 补证说明（显式）：工作区当前缺少 `demo_mkdir.py` 文件快照，已通过提交对象 `ad590406...` 回溯到该文件内容作为补证；`demo_ws.py` 以现存文件与提交语义双重验证。

## ✅ 今日目标
- [x] 完成 `mkdir` 命令的参数化实现（含 `-p/--parents`）。
- [x] 完成 `wc` 命令的多统计分支（`-l/-w/-c` 与默认全量）。
- [x] 理解“幂等目录创建 + 输入校验”在 CLI 工具中的必要性。

## 📚 章节内容
- 章节：正则表达式与命令行工具（argparse 练习深化）
- 小节：
  1) `mkdir` 参数设计与 `Path.mkdir` 行为
  2) `wc` 统计逻辑与输出分发
  3) 命令错误输入的防御性处理
- 学习位置：`正则表达式/argparse练习/`
- 对应练习：`正则表达式/argparse练习/题目.md`（练习 2/3）
- 对应答案：当前以脚本实现为主，配合已有样例答案回链。
- 章节总结（3行内）：
  1. 这一天从“参数解析”进入“可执行命令闭环”。
  2. `demo_mkdir.py` 聚焦目录创建幂等，`demo_ws.py` 聚焦文本统计分支。
  3. 真实挑战是输入合法性与错误路径处理，而不只是功能跑通。

## 📌 今日内容（代码在做什么）
1. `demo_mkdir.py`：解析目录名与 `-p`，并调用 `Path(...).mkdir()` 完成创建。  
2. `demo_ws.py`：读取文件文本，计算行/词/字符数，按选项决定输出范围。  
3. 题目文档约束了两个命令的行为边界（默认行为、单选行为、参数形式）。

## 🧠 核心知识（底层原理）
- `Path.mkdir(parents=True, exist_ok=True)` 体现“可重复执行”的幂等设计。
- `nargs='?'` 让参数可缺省，但业务必须显式处理缺省值（避免运行时异常）。
- CLI 输出分发可用“选项字典 + 动态读取属性”减少重复 `if/elif`。
- 提交语义中的“更新ws/添加mkdir”本质是同一训练链：参数解析 → 系统调用。

## 💻 关键代码（精简 + 行为解释）
```python
if args.parents:
    Path(args.dir_name).mkdir(parents=True, exist_ok=True)
else:
    Path(args.dir_name).mkdir(exist_ok=True)
```

### 行为解释
- `-p` 时允许自动创建父目录；
- 非 `-p` 时只创建目标目录；
- 两种分支都启用 `exist_ok=True`，避免重复执行时报错中断。

## ⚠️ 问题 / 坑（至少一个真实错误案例）
### 案例：`demo_ws.py` 文件参数缺失导致运行时错误
- 触发方式：`python demo_ws.py -l`（未提供文件路径）。  
- 错误现象：`open(args.file, ...)` 中 `args.file` 为 `None`，会触发类型错误（路径应为字符串/PathLike）。  
- 根因：参数定义为 `nargs='?'`，允许缺省，但代码未对 `None` 做前置校验。  
- 修正：
  - 方案 A：把参数改为必填（去掉 `nargs='?'`）；
  - 方案 B：保留可选并在读取前判断 `if not args.file: parser.error(...)`。  
- 防再犯规则：凡是“可选位置参数 + 文件 IO”组合，必须先做空值与存在性检查。

## 🏋️ 强化训练（练习 / 答案 / 要求）
- 训练目标：形成可复用的 CLI 输入校验与文件系统操作规范。
- 训练任务：
  1. 基础：重构 `wc`，补齐“缺参/文件不存在/编码异常”处理；
  2. 进阶：扩展 `mkdir`，支持一次创建多个目录并输出执行结果；
  3. 迁移：把 `wc + mkdir + ls` 合并为统一入口 CLI。
- 难度分层：基础 / 进阶 / 迁移
- 验收标准：
  - 每个命令至少覆盖 1 条失败用例与 1 条成功用例；
  - 失败用例输出可读错误信息（含原因）；
  - 目录创建逻辑具备幂等性（重复执行结果一致）。
- practice 回链（已存在样例题号）：
  - `practice/正则表达式/foundation/p-001-regex-basics.md`
  - `practice/正则表达式/advanced/p-002-argparse-grep.md`
  - `practice/正则表达式/transfer/p-003-log-analyzer.md`
- answers 回链（已存在样例题号）：
  - `answers/正则表达式/foundation/p-001-regex-basics.answer.md`
  - `answers/正则表达式/advanced/p-002-argparse-grep.answer.md`
  - `answers/正则表达式/transfer/p-003-log-analyzer.answer.md`

## 🧩 我的理解（第一人称）
- 我现在能清楚解释：同样是 argparse，真正决定质量的是“异常分支是否被设计”。  
- 我还模糊的点：当 CLI 命令数量增长时，如何统一错误码与日志格式。  
- 我准备怎么补：下一步按子命令架构重组，并补一套最小回归测试。

## 🚀 延伸（下一步学习）
- 下一步主题：`subparsers` 架构与 CLI 工具测试化。  
- 推荐练习：
  1. 为 `demo_ws.py` 增加 `--encoding` 参数；
  2. 为 `demo_mkdir.py` 增加 dry-run 模式；
  3. 编写 `pytest` 参数化测试覆盖常用调用路径。

## 📎 回链索引
- 证据文件：
  - `正则表达式/argparse练习/demo_mkdir.py`（通过提交快照补证）
  - `正则表达式/argparse练习/demo_ws.py`
  - `正则表达式/argparse练习/题目.md`
- 关键提交：
  - `ad5904061c2dfdb6558f0ada46cc92a87d81cc21`
  - `071ed1b10bca2cc5c8d6514f8ee9b0306940e381`
  - `fcc8e72261c610cde01bd7d636768a1a89b811c6`（合并提交）

## ✅ 完成度自检
- [x] 已按“先归档证据，缺失则补证”执行并显式标注
- [x] 已优先使用 2026-03-09 当天提交语义组织内容
- [x] 已包含真实错误案例（可复现实例）
- [x] 已包含强化训练（基础/进阶/迁移）与验收标准
- [x] 已包含 practice/answers 样例题号回链
