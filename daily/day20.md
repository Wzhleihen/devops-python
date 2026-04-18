# Day 20 - 类属性/实例属性查找与覆盖机制（完整AI分析版）

📅 日期：2026-04-18  
⏱ 距离上次学习：40 天

---

## 📦 证据归档（先归档，后补证）
- 归档目录检查：未发现 `归档/2026/2026-04-18`（归档缺失，已补证）。
- 当天提交语义（优先）：
  1. `9fe6225`：重构学习仓库结构并落地 day/强化训练体系（包含 `07_面向对象/` 学习文件纳入规范结构）。
- 与语义直接对应的代码证据（仅限本章节）：
  - `07_面向对象/class_attribute_access_test-1.py`
  - `07_面向对象/class_attribute_access_test-1-answer.py`
  - `07_面向对象/demo01.ipynb`
- 补证说明（显式）：本日分析严格限定在 `07_面向对象/`，不引用其他章节文件。

## ✅ 今日目标
- [x] 理清“实例属性优先于类属性”的查找顺序。
- [x] 理解 `+=` 在实例访问中的“先查后写”副作用。
- [x] 能通过 `__dict__` 判断属性是否已被实例覆盖。

## 📚 章节内容
- 章节：面向对象（属性模型）
- 小节：类属性、实例属性、覆盖与查找链
- 学习位置：`07_面向对象/`
- 对应练习：
  - `07_面向对象/class_attribute_access_test-1.py`
  - `practice/07_面向对象/foundation/p-001-class-vs-instance-attr.md`
  - `practice/07_面向对象/advanced/p-002-attribute-shadowing-trace.md`
  - `practice/07_面向对象/transfer/p-003-config-model-with-class-defaults.md`
- 对应答案：
  - `07_面向对象/class_attribute_access_test-1-answer.py`
  - `answers/07_面向对象/foundation/p-001-class-vs-instance-attr.answer.md`
  - `answers/07_面向对象/advanced/p-002-attribute-shadowing-trace.answer.md`
  - `answers/07_面向对象/transfer/p-003-config-model-with-class-defaults.answer.md`
- 章节总结（3行内）：
  1. 通过同一段脚本连续观察类属性与实例属性在不同时刻的值变化。
  2. 重点掌握“读取走查找链，赋值写入实例”的差异行为。
  3. 借助 `__dict__` 验证覆盖是否发生，避免靠猜测理解属性机制。

## 📌 今日内容（代码在做什么）
1. 定义 `Person.age`、`Person.height` 为类属性，并在构造函数中写入实例属性 `self.age`。  
2. 通过 `jerry.height = 180` 与 `tom.height += 10` 对比“显式赋值”和“复合赋值”产生的实例覆盖。  
3. 通过 `Person.height += 15` 观察“类属性变化不会影响已覆盖该属性的实例”。

## 🧠 核心知识（底层原理）
- 属性查找顺序：`obj.__dict__ -> class.__dict__ -> MRO`。
- 实例赋值规则：`obj.x = v` 会把 `x` 写入实例字典（即使类中同名属性存在）。
- `obj.x += 10` 本质是“先读 `obj.x`，再写回 `obj.x`”，因此可能触发实例属性新建。
- `__dict__` 可作为“是否已实例覆盖”的直接证据，不应只凭输出猜测。

## 💻 关键代码（精简 + 行为解释）
```python
class Person:
    height = 175

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


tom = Person("Tom")
jerry = Person("Jerry", 20)

jerry.height = 180

tom.height += 10

Person.height += 15

print(Person.height, tom.height, jerry.height)
print(tom.__dict__["height"])
```

### 行为解释
- 运行后可得到：`Person.height=190, tom.height=185, jerry.height=180`。  
- `tom/jerry` 已各自持有 `height` 实例属性，不再跟随类属性后续变化。  
- `tom.__dict__["height"]` 存在且为 `185`，证明覆盖发生在实例层。

## ⚠️ 问题 / 坑（至少一个真实错误案例）
### 案例：误以为修改类属性会同步更新所有实例同名值
- 错误现象：执行 `Person.height += 15` 后，误判 `tom.height` 也应变成 190。  
- 根因：忽略了 `tom.height += 10` 已在实例层创建 `height`，查找优先命中实例属性。  
- 修正：先检查 `obj.__dict__`，确认同名属性是否已被实例覆盖，再判断类属性改动影响范围。  
- 防再犯规则：涉及同名属性时，先写“谁在读、谁在写、写到哪一层”三行推导。

## 🏋️ 强化训练（练习 / 答案 / 要求）
- 训练目标：把“属性查找与覆盖”从现象记忆提升为可推导、可验证能力。
- 训练任务：
  1. 基础：完成 `p-001-class-vs-instance-attr`，给出 5 条访问表达式的值推导。  
  2. 进阶：完成 `p-002-attribute-shadowing-trace`，逐步记录每次赋值后的 `__dict__` 变化。  
  3. 迁移：完成 `p-003-config-model-with-class-defaults`，实现“类默认配置 + 实例覆盖配置”模型。
- 难度分层：基础 / 进阶 / 迁移
- 验收标准：
  - 至少 3 处使用 `__dict__` 证明属性归属；
  - 至少 1 处解释 `+=` 导致实例覆盖的过程；
  - 至少 1 个迁移题给出“类改动影响实例”的边界说明。
- practice 回链：
  - `practice/07_面向对象/foundation/p-001-class-vs-instance-attr.md`
  - `practice/07_面向对象/advanced/p-002-attribute-shadowing-trace.md`
  - `practice/07_面向对象/transfer/p-003-config-model-with-class-defaults.md`
- answers 回链：
  - `answers/07_面向对象/foundation/p-001-class-vs-instance-attr.answer.md`
  - `answers/07_面向对象/advanced/p-002-attribute-shadowing-trace.answer.md`
  - `answers/07_面向对象/transfer/p-003-config-model-with-class-defaults.answer.md`

## 🧩 我的理解（第一人称）
- 我现在能清楚解释：为什么“看起来改的是同一个属性名”，结果却可能三处值都不同。  
- 我还模糊的点：描述符（`property`）介入后，查找与赋值链路如何变化。  
- 我准备怎么补：下一步用 `property` 和普通属性做对照实验，输出调用轨迹。

## 🚀 延伸（下一步学习）
- 下一步主题：描述符与 `property` 对属性访问链路的影响。  
- 推荐练习：
  1. 用 `property` 改写 `height`，观察读写拦截；
  2. 对比普通属性与 `property` 的 `__dict__` 变化；
  3. 补一组“类变量做默认配置、实例做局部覆盖”的小型场景题。

## 📎 回链索引
- 章节目录：`07_面向对象/`
- 关键文件：
  - `07_面向对象/class_attribute_access_test-1.py`
  - `07_面向对象/class_attribute_access_test-1-answer.py`
  - `07_面向对象/demo01.ipynb`
- 关键提交：
  - `9fe6225`

## ✅ 完成度自检
- [x] 已限定只使用 `07_面向对象/` 作为证据来源
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含强化训练（基础/进阶/迁移）与验收标准
- [x] 已包含 practice/answers 规范回链路径
- [x] 已提供关键代码与可验证输出
