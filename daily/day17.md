# Day 17 - 分组提取、命名捕获与文本分割（完整AI分析版）

📅 日期：2026-03-03  
⏱ 距离上次学习：1 天

---

## ✅ 今日目标
- [x] 掌握命名分组 `(?P<name>...)` 的提取方式。
- [x] 理解 `findall` 在有/无分组场景下返回结构变化。
- [x] 能完成 `split`/`sub` 类文本处理并验证输出正确性。

## 📚 章节内容
- 章节：正则表达式进阶（结构化提取）
- 小节：
  1) 位置分组与命名分组
  2) `group/groups/groupdict` 返回差异
  3) `re.split` 与清洗流程
- 学习位置：`正则表达式/`
- 对应练习：
  - `正则表达式/t2.py`
  - `正则表达式/t3.py`
  - `正则表达式/t4.py`
  - `practice/正则表达式/advanced/p-002-argparse-grep.md`
  - `practice/正则表达式/transfer/p-003-log-analyzer.md`
- 对应答案：
  - `answers/正则表达式/advanced/p-002-argparse-grep.answer.md`
  - `answers/正则表达式/transfer/p-003-log-analyzer.answer.md`
- 章节总结（3行内）：
  1. 当天从“匹配字符串”升级为“提取字段结构”。
  2. 通过命名分组与 `groupdict()`，实现可读性更高的数据抽取。
  3. 与当天提交语义一致：新增并扩展了正则用法示例文件。

## 🗂 证据归档（先归档，缺失补证）
- 归档检查：未发现 `归档/2026/2026-03-03`（归档证据缺失）。
- 补证来源（显式标注）：
  - 代码证据：`正则表达式/t2.py`、`正则表达式/t3.py`、`正则表达式/t4.py`
  - 时间线证据：`daily/_generated/timeline_by_date.json`
  - 映射证据：`daily/_generated/day_mapping_with_policy.json`
  - 提交证据：`37f300a12fadd4f97d3dc3e444d6791a083a3910`（2026-03-03，添加正则表达式用法）

## 📌 今日内容（代码在做什么）
1. `t2.py` 增加命名分组样例，演示 `groups()` 与 `groupdict()` 的并行使用。  
2. `t2.py` 补充 `sub/subn` 与分组注释，连接“匹配”与“替换”两类任务。  
3. `t3.py` 构造结构化文本（姓名、年龄、电话），用命名分组提取字典结果。  
4. `t4.py` 用 `re.split('[\\.()\\s,]+', s)` 拆分函数调用文本，并通过 `filter(None, ...)` 清空项。  

## 🧠 核心知识（底层原理）
- 命名分组让“第几个组”变成“字段名”，可读性与维护性更好。  
- `group(0)` 是整体命中，`group(1..n)` 是捕获组，`groupdict()` 是命名组映射。  
- `findall` 遇到分组后会返回组内容而非整段匹配，这是很多解析错误的根源。  
- `re.split` 常配合字符类做“多分隔符清洗”，再用 `filter(None, ...)` 去空值。

## 💻 关键代码（精简 + 行为解释）
```python
import re

s = """
zhangsan, 20, 123456789
lisi, 21, 123456789
"""
pattern = re.compile(r'(?P<name>\w+),\s*(?P<age>\d+),\s*(?P<phone>\d+)')
for m in pattern.finditer(s):
    print(m.groupdict())
```

### 行为解释
- 每条记录会被解析成 `{"name": ..., "age": ..., "phone": ...}`。
- 命名分组降低了后续字段映射错误概率。
- 该模式可直接迁移到日志/CSV 风格文本抽取。

## ⚠️ 问题 / 坑（至少一个真实错误案例）
### 案例：把 `findall` 分组结果当完整匹配字符串使用
- 错误现象：模式含分组时，`findall` 返回组内容；若仍按“整段字符串”处理，会出现索引或字段拼接错误。  
- 根因：忽略了 `findall` 的返回规则变化（无分组 vs 有分组）。
- 修正：
  - 需要完整对象时改用 `finditer`；或
  - 调整模式为非捕获分组 `(?:...)` 以保持返回结构稳定。
- 防再犯规则：设计模式时先写明“预期返回形态（str / tuple / Match）”。

## 🏋️ 强化训练（三层：练习 / 答案 / 要求）
- 训练目标：从“能写模式”进阶到“能稳定抽取结构化字段”。
- 第一层（基础）：
  - 题目：完成 `p-001-regex-basics`，补一个“有分组/无分组”对照小节。
  - 练习回链：`practice/正则表达式/foundation/p-001-regex-basics.md`
  - 答案回链：`answers/正则表达式/foundation/p-001-regex-basics.answer.md`
- 第二层（进阶）：
  - 题目：完成 `p-002-argparse-grep`，要求输出命名字段字典。
  - 练习回链：`practice/正则表达式/advanced/p-002-argparse-grep.md`
  - 答案回链：`answers/正则表达式/advanced/p-002-argparse-grep.answer.md`
- 第三层（迁移）：
  - 题目：完成 `p-003-log-analyzer`，加入 `split + groupdict` 双流程解析。
  - 练习回链：`practice/正则表达式/transfer/p-003-log-analyzer.md`
  - 答案回链：`answers/正则表达式/transfer/p-003-log-analyzer.answer.md`

### 可验证验收标准
- [ ] `t3` 类输入可稳定产出包含 `name/age/phone` 的字典列表。  
- [ ] 同一文本在“有分组/无分组”两种模式下输出差异可被准确解释。  
- [ ] `re.split` 结果无空字符串，且能还原出预期 token 序列。  
- [ ] 至少提交 1 个失败样例及对应修复方式。  

## 🧩 我的理解（第一人称）
- 我现在能清楚解释：为什么命名分组是从教学代码走向工程代码的关键一步。  
- 我还模糊的点：复杂日志里可选字段与贪婪/非贪婪量词的组合策略。  
- 我准备怎么补：增加失败样本集，用 `finditer + groupdict` 做逐条断言。

## 🚀 延伸（下一步学习）
- 下一步主题：正则与命令行工具结合（grep 风格过滤与日志分析）。
- 推荐练习：
  1. 写一个最小 `grep` 脚本，支持 `-i` 和行号输出；
  2. 对日志做命名分组抽取并导出为字典列表；
  3. 引入异常样本（缺字段、空行）并验证鲁棒性。

## 📎 回链索引
- 关键文件：
  - `正则表达式/t2.py`
  - `正则表达式/t3.py`
  - `正则表达式/t4.py`
  - `practice/正则表达式/advanced/p-002-argparse-grep.md`
  - `answers/正则表达式/advanced/p-002-argparse-grep.answer.md`
  - `practice/正则表达式/transfer/p-003-log-analyzer.md`
  - `answers/正则表达式/transfer/p-003-log-analyzer.answer.md`
- 关键证据：
  - `daily/_generated/timeline_by_date.json`
  - `daily/_generated/day_mapping_with_policy.json`
  - `37f300a12fadd4f97d3dc3e444d6791a083a3910`
- 说明：本日无归档目录，已按“先归档、缺失补证”规则明确补证来源。

## ✅ 完成度自检
- [x] 日期固定为 2026-03-03
- [x] 已显式执行“归档优先，缺失补证”
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含三层强化训练与可验证验收标准
- [x] 已包含 practice/answers 题号回链
