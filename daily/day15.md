# Day 15 - JSON 与 MsgPack 对照序列化（完整AI分析版）

📅 日期：2025-12-19  
⏱ 距离上次学习：1 天

---

## ✅ 今日目标
- [x] 掌握 `json / pickle / msgpack` 在类型与体积上的差异。
- [x] 理解 `msgpack.loads(..., raw=False)` 对字符串类型还原的意义。
- [x] 能把“序列化选择”映射到实际任务（日志、配置、跨语言数据交换）。

## 📚 章节内容
- 章节：序列化与反序列化（格式对比阶段）
- 小节：
  1) 三种序列化协议的输出类型比较（`str` vs `bytes`）  
  2) MsgPack 反序列化参数与字符串解码  
  3) 结构化数据在文件IO与正则任务中的迁移使用
- 学习位置：`序列化与反序列化/t2.py`
- 对应练习：
  - `practice/正则表达式/foundation/p-001-regex-basics.md`
  - `practice/正则表达式/advanced/p-002-argparse-grep.md`
  - `practice/正则表达式/transfer/p-003-log-analyzer.md`
- 对应答案：
  - `answers/正则表达式/foundation/p-001-regex-basics.answer.md`
  - `answers/正则表达式/advanced/p-002-argparse-grep.answer.md`
  - `answers/正则表达式/transfer/p-003-log-analyzer.answer.md`
- 章节总结（3行内）：
  1. 当天提交语义集中在 `json` 与 `msgpack` 示例更新。  
  2. 重点从“会序列化”升级为“知道为什么选这种格式”。  
  3. 类型一致性（尤其字节/字符串）成为数据链路稳定性的关键。

## 🧾 证据来源（时间线先归档）
- 归档目录检查：未发现 `归档/2025/2025-12-19`。
- 归档缺失，补证来源。
- 补证证据（优先级顺序）：
  1) `daily/_generated/timeline_by_date.json`（2025-12-19：`update msgpack exmaple`、`update  json example`）
  2) `daily/_generated/day_mapping_with_policy.json`（day08 映射到 2025-12-19）
  3) `序列化与反序列化/t2.py`（json/pickle/msgpack 对照代码）
  4) 提交证据：`a4f2f7e`、`9f0a9ff`（2025-12-19）

## 📌 今日内容（代码在做什么）
1. 构造统一字典 `d`，分别用 `json/pickle/msgpack` 执行 `dumps`。  
2. 打印每种格式的输出类型与字节长度，用真实数据对比编码体积。  
3. 使用 `msgpack.loads(x, raw=False)` 还原对象，验证结构等价性。  
4. 通过 `d == y` 与 `d is y` 对照，说明“值相等不代表对象同一性”。

## 🧠 核心知识（底层原理）
- JSON 可读性高、跨语言友好，但通常体积更大。  
- Pickle/MsgPack 输出字节流，适合紧凑存储或高效传输；其中 Pickle 更偏 Python 内部生态。  
- `msgpack.loads(..., raw=False)` 会把原始字节键值解码为字符串，减少后续类型错配。  
- 反序列化会生成新对象：语义上“值复制”，不是“对象引用共享”。

## 💻 关键代码或关键行为
```python
methods = (json, pickle, msgpack)

for i, m in enumerate(methods):
    x = m.dumps(d)
    print(i + 1, m.__name__, type(x), len(x), x)

y = msgpack.loads(x, raw=False)
print(d == y)  # True
print(d is y)  # False
```

### 行为解释
- 同一数据结构在不同协议下会得到不同的编码类型和体积。  
- `msgpack.loads(..., raw=False)` 保证还原后的键值更接近日常 Python 字符串语义。  
- `==` 与 `is` 的并列输出用于验证“内容一致性”与“对象身份”是两套判断。

## ⚠️ 问题 / 坑（至少一个真实错误案例）
### 案例：路径拼接中把字符串当 `Path` 使用
- 错误现象：`TypeError: unsupported operand type(s) for /: 'str' and 'str'`（见 `文件IO/文件IO.ipynb`）。  
- 根因：`/` 运算符只对 `pathlib.Path` 做了重载，普通字符串不能直接参与该运算。  
- 修正：
  - 使用 `Path('base') / 'child'`；或
  - 使用 `os.path.join('base', 'child')`。  
- 防再犯规则：路径处理前先统一类型，进入函数时立即把输入转为 `Path`。

## 🏋️ 强化训练（练习 / 答案 / 要求）
- 训练目标：把序列化输出接入“日志提取与统计”完整链路。
- 训练任务：
  1. 基础：完成 `p-001-regex-basics`，提取结构化字段；  
  2. 进阶：完成 `p-002-argparse-grep`，把过滤条件参数化；  
  3. 迁移：完成 `p-003-log-analyzer`，将分析结果导出为 JSON 或 MsgPack。
- 验收标准：
  - 同一输入日志可输出两种格式（JSON/MsgPack）且字段一致；
  - 对异常日志行有容错策略，不因单行错误终止全流程；
  - 提交中包含性能与体积对比（至少 1 组数据）。

## 📎 practice / answers 回链
- `practice/正则表达式/foundation/p-001-regex-basics.md`
- `answers/正则表达式/foundation/p-001-regex-basics.answer.md`
- `practice/正则表达式/advanced/p-002-argparse-grep.md`
- `answers/正则表达式/advanced/p-002-argparse-grep.answer.md`
- `practice/正则表达式/transfer/p-003-log-analyzer.md`
- `answers/正则表达式/transfer/p-003-log-analyzer.answer.md`

## ✅ 完成度自检
- [x] 日期固定为 2025-12-19
- [x] 已执行“先归档证据”并明确标注“归档缺失，补证来源”
- [x] 已包含今日目标 / 章节内容 / 今日内容 / 核心知识 / 关键代码或关键行为
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含基础/进阶/迁移训练与验收标准
- [x] 已包含 practice/answers 回链路径
