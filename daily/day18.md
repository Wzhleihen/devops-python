# Day 18 - argparse 参数建模与 `ls` 命令骨架（完整AI分析版）

📅 日期：2026-03-08  
⏱ 距离上次学习：5 天（相对上一个已建档日 2026-03-03）

---

## 📦 证据归档（先归档，后补证）
- 归档目录检查：未发现 `归档/2026/2026-03-08`（归档缺失，已补证）。
- 当天提交语义（优先）：
  1. `6396bab47c668422a2ec93fe895ed6eff0ca3d14`：`添加正则表达式用法`
  2. `5d0a618f430725d0450417f04a6c2926e56488cc`：`添加练习`
  3. `e25598d19ef45b39255749e355716776d6378197`：合并提交（辅助证据）
- 与语义直接对应的代码证据：
  - `正则表达式/argparse-demo01.py`（argparse 参数行为演示）
  - `正则表达式/argparse_ls.py`（`ls` 参数与输出骨架）
  - `正则表达式/argparse练习/题目.md`（练习 1~10，包含 `wc/mkdir/grep/ls`）
- 补证说明（显式）：当天提交包含大量练习目录/临时文件（`作业/tmp/...`），其教学语义主要由 `argparse` 相关脚本与题目文档承载，因此以 CLI 训练链路作为主证据。

## ✅ 今日目标
- [x] 理解 `argparse` 的位置参数、短长选项与 `action` 行为。
- [x] 能实现简化 `ls` 的 `-a/-l/-h` 组合逻辑。
- [x] 建立“题目要求 → 参数设计 → 输出实现”的 CLI 建模流程。

## 📚 章节内容
- 章节：正则表达式与命令行工具（argparse 实战段）
- 小节：
  1) 参数可选性（`nargs`）与布尔开关（`store_true/store_false`）
  2) `ls` 详细输出（权限/大小/时间）
  3) 练习驱动：从 `echo/wc/mkdir` 过渡到完整 `ls`
- 学习位置：`正则表达式/`
- 对应练习：`正则表达式/argparse练习/题目.md`
- 对应答案：当前源码内联实现 + 回链到已有样例答案。
- 章节总结（3行内）：
  1. 这一天核心是“CLI 参数语义建模”。
  2. 通过 `argparse_ls.py` 把参数解析连接到真实文件系统输出。
  3. 重点难点从“会写脚本”升级到“能设计参数接口”。

## 📌 今日内容（代码在做什么）
1. `argparse-demo01.py`：演示 `nargs`、`store_true/store_const/store_false` 的解析行为。  
2. `argparse_ls.py`：实现简化 `ls`，支持路径参数、隐藏文件过滤、详细列表和人类可读大小。  
3. `argparse练习/题目.md`：定义分层训练题，明确 `wc/mkdir/cp/grep/du/ls` 目标。

## 🧠 核心知识（底层原理）
- CLI 程序的第一步不是写业务，而是先稳定“参数契约”。
- `action='store_true'` 表示“选项存在即 True”；这比手写字符串判断更稳。
- `nargs='?'` 让位置参数变为可选，但后续代码必须处理 `None` 分支。
- `-h` 在 `argparse` 中默认占用 help 语义；业务层“human readable”通常需谨慎命名与测试。

## 💻 关键代码（精简 + 行为解释）
```python
parser.add_argument('path', nargs='?', default='.', help='path to list')
parser.add_argument('-a', '--all', action='store_true', help='show all files')
parser.add_argument('-l', action='store_true', help='show detail list')
parser.add_argument('-h', action='store_true', help='human readable')
```

### 行为解释
- 缺省路径落到当前目录 `.`。  
- `-a/-l/-h` 为布尔开关，组合后驱动显示策略。  
- 这组参数定义直接映射题目中的 `ls` 使用矩阵（`ls` / `ls -a` / `ls -l` / `ls -lh` / `ls path`）。

## ⚠️ 问题 / 坑（至少一个真实错误案例）
### 案例：参数未注册导致解析失败
- 错误现象：在 `argparse-demo01.py` 的实验注释中，出现  
  `usage: ls [-h]` 与 `ls: error: unrecognized arguments: /etc`。  
- 根因：当解析器只识别 `-h`（或位置参数定义不匹配）时，传入路径会被判定为未知参数。  
- 修正：
  - 明确注册位置参数（如 `path`）；
  - 用 `parse_args([...])` 为关键命令形态补最小测试。  
- 防再犯规则：每新增一个 CLI 选项，至少验证“默认 + 单选 + 组合”三类调用。

## 🏋️ 强化训练（练习 / 答案 / 要求）
- 训练目标：把 argparse 基础转成稳定 CLI 交互设计能力。
- 训练任务：
  1. 基础：完成 `wc` 参数分支（`-l/-w/-c`）与默认全量输出；
  2. 进阶：完成 `grep` 的 `-i/-n` 组合；
  3. 迁移：实现最小 `ls`，输出权限/大小/时间/文件名。
- 难度分层：基础 / 进阶 / 迁移
- 验收标准：
  - 能通过 5 类命令形态：无参、路径参数、单选项、组合选项、错误参数；
  - 对错误输入给出可读报错（非静默失败）；
  - 输出字段顺序与题目约束一致。
- practice 回链（已存在样例题号）：
  - `practice/正则表达式/foundation/p-001-regex-basics.md`
  - `practice/正则表达式/advanced/p-002-argparse-grep.md`
  - `practice/正则表达式/transfer/p-003-log-analyzer.md`
- answers 回链（已存在样例题号）：
  - `answers/正则表达式/foundation/p-001-regex-basics.answer.md`
  - `answers/正则表达式/advanced/p-002-argparse-grep.answer.md`
  - `answers/正则表达式/transfer/p-003-log-analyzer.answer.md`

## 🧩 我的理解（第一人称）
- 我现在能清楚解释：为什么命令行工具先要设计参数模型，再写文件处理逻辑。  
- 我还模糊的点：复杂 CLI（多子命令）下参数复用和冲突规避策略。  
- 我准备怎么补：把当前单命令脚本升级到 `subparsers` 版本做一次重构。

## 🚀 延伸（下一步学习）
- 下一步主题：多命令 CLI（`subparsers`）与测试自动化。  
- 推荐练习：
  1. 将 `wc/mkdir/grep` 合并为一个多子命令工具；
  2. 为参数矩阵编写 `pytest` 用例；
  3. 增加“错误参数提示 + 示例命令”输出。

## 📎 回链索引
- 证据文件：
  - `正则表达式/argparse-demo01.py`
  - `正则表达式/argparse_ls.py`
  - `正则表达式/argparse练习/题目.md`
- 关键提交：
  - `6396bab47c668422a2ec93fe895ed6eff0ca3d14`
  - `5d0a618f430725d0450417f04a6c2926e56488cc`
  - `e25598d19ef45b39255749e355716776d6378197`（合并提交）

## ✅ 完成度自检
- [x] 已按“先归档证据，缺失则补证”执行并显式标注
- [x] 已优先使用 2026-03-08 当天提交语义组织内容
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含强化训练（基础/进阶/迁移）与验收标准
- [x] 已包含 practice/answers 样例题号回链
