# Day 16 - 正则单次匹配与全文扫描（完整AI分析版）

📅 日期：2026-03-02  
⏱ 距离上次学习：76 天

---

## ✅ 今日目标
- [x] 理解 `match` / `search` / `fullmatch` 的语义边界。
- [x] 掌握 `findall` / `finditer` 在“取值 vs 取位置信息”上的差异。
- [x] 能定位“匹配失败后误用返回值”导致的真实报错链路。

## 📚 章节内容
- 章节：正则表达式入门（匹配模型）
- 小节：
  1) 单次匹配：`match/search/fullmatch`
  2) 全文匹配：`findall/finditer`
  3) 迭代器结果与 `start/end/span` 位置索引
- 学习位置：`正则表达式/`
- 对应练习：
  - `正则表达式/t1.py`
  - `正则表达式/t2.py`
  - `practice/正则表达式/foundation/p-001-regex-basics.md`
- 对应答案：
  - `answers/正则表达式/foundation/p-001-regex-basics.answer.md`
- 章节总结（3行内）：
  1. 当天重点是把“能匹配”拆解为“从哪开始匹配、匹配多少、返回什么对象”。
  2. 通过 `finditer` 的位置信息，建立了可调试的正则观察方式。
  3. 内容与当天提交语义一致：围绕正则基础用法展开并扩充示例。

## 🗂 证据归档（先归档，缺失补证）
- 归档检查：未发现 `归档/2026/2026-03-02`（归档证据缺失）。
- 补证来源（显式标注）：
  - 代码证据：`正则表达式/t1.py`、`正则表达式/t2.py`
  - 时间线证据：`daily/_generated/timeline_by_date.json`
  - 映射证据：`daily/_generated/day_mapping_with_policy.json`
  - 提交证据：
    - `acfed4dfd12e7546af7c2b3688e7cea06ec00455`（2026-03-02，涉及 `t1.py`、`t2.py`）
    - `96c56b4ee7a203e587c274fc2640441e0b88ac5c`（2026-03-02，扩充 `t2.py`）

## 📌 今日内容（代码在做什么）
1. `t1.py` 用 `re.findall('(?:t|f)oo?', text)` 演示非捕获分组与可选量词的组合匹配。  
2. `t2.py` 先打印字符串字符索引，建立“模式命中位置”的观察基线。  
3. 在 `t2.py` 中对照 `match/search/fullmatch` 注释样例，明确三者起点与覆盖范围。  
4. 用 `finditer('b\w+', s)` 遍历匹配对象，并结合 `start/end` 回切原串，验证命中片段。  

## 🧠 核心知识（底层原理）
- `match` 默认从起始位置匹配；`search` 在范围内扫描第一个命中；`fullmatch` 要求整段完全命中。  
- `findall` 返回“值”，`finditer` 返回“对象迭代器（含位置信息）”。  
- 分组会改变 `findall` 的返回形态：无分组为字符串列表，有分组会返回分组内容（单组字符串/多组元组）。  
- 当匹配失败时返回 `None`，后续若直接 `.group()` 会触发异常，必须先判空。  

## 💻 关键代码（精简 + 行为解释）
```python
import re

s = """bottle\nbag\nbig\napple\nable"""
matches = re.finditer(r"b\w+", s)
for m in matches:
    print(m[0], m.start(), m.end())
```

### 行为解释
- `b\w+` 会命中以 `b` 开头的单词（如 `bottle`、`bag`、`big`）。
- `finditer` 返回可迭代的 `Match` 对象，可直接读取命中值和区间。
- 这类写法比只拿字符串结果更适合排查边界问题。

## ⚠️ 问题 / 坑（至少一个真实错误案例）
### 案例：匹配失败后直接取分组
- 错误现象：`m = re.match('^a', s)` 返回 `None` 后若执行 `m.group(0)`，会报：  
  `AttributeError: 'NoneType' object has no attribute 'group'`。
- 根因：`match` 只从起点匹配，多行文本起点是 `bottle`，不是 `a`。
- 修正：
  - 改为 `re.search('^a', s, re.M)` 进行多行锚点搜索；或
  - 先判空：`if m is not None:` 再调用 `group()`。
- 防再犯规则：所有 `Match` 对象访问前默认执行“判空一步”。

## 🏋️ 强化训练（三层：练习 / 答案 / 要求）
- 训练目标：建立“可解释、可调试”的正则匹配基本功。
- 第一层（基础）：
  - 题目：完成 `p-001-regex-basics` 的 IP 与日期提取。
  - 练习回链：`practice/正则表达式/foundation/p-001-regex-basics.md`
  - 答案回链：`answers/正则表达式/foundation/p-001-regex-basics.answer.md`
- 第二层（进阶）：
  - 在 `t2.py` 增加 3 组 `match/search/fullmatch` 对照输入，记录返回差异。
- 第三层（迁移）：
  - 将 `findall` 结果改造成“值 + 位置”报告（需使用 `finditer`）。

### 可验证验收标准
- [ ] 能给出 3 组输入下 `match/search/fullmatch` 的**不同返回结果**并解释原因。  
- [ ] 对同一模式同时输出 `findall` 与 `finditer` 结果，且 `finditer` 含 `start/end`。  
- [ ] 至少复现 1 次“`NoneType` 无 `group`”错误并提交修复前后对照。  

## 🧩 我的理解（第一人称）
- 我现在能清楚解释：同一个正则，在不同 API 下为什么返回完全不同。  
- 我还模糊的点：复杂多行文本中锚点与标志位（`re.M`/`re.S`）组合的最佳策略。  
- 我准备怎么补：每次写模式先做“最小文本 + 三 API 对照”验证。

## 🚀 延伸（下一步学习）
- 下一步主题：命名分组、替换与文本切分（向结构化提取过渡）。
- 推荐练习：
  1. 用命名分组提取 `name/age/phone`；
  2. 用 `re.split` 拆解函数调用串；
  3. 用 `sub/subn` 做批量替换并统计次数。

## 📎 回链索引
- 关键文件：
  - `正则表达式/t1.py`
  - `正则表达式/t2.py`
  - `practice/正则表达式/foundation/p-001-regex-basics.md`
  - `answers/正则表达式/foundation/p-001-regex-basics.answer.md`
- 关键证据：
  - `daily/_generated/timeline_by_date.json`
  - `daily/_generated/day_mapping_with_policy.json`
  - `acfed4dfd12e7546af7c2b3688e7cea06ec00455`
  - `96c56b4ee7a203e587c274fc2640441e0b88ac5c`
- 说明：本日无归档目录，已按“先归档、缺失补证”规则明确补证来源。

## ✅ 完成度自检
- [x] 日期固定为 2026-03-02
- [x] 已显式执行“归档优先，缺失补证”
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含三层强化训练与可验证验收标准
- [x] 已包含 practice/answers 题号回链
