# Day 21 - property 封装与 datetime 时间处理（完整AI分析版）

📅 日期：2026-04-19  
⏱ 距离上次学习：1 天

---

## 📦 证据归档（先归档，后补证）
- 归档目录检查：未发现 `归档/2026/2026-04-19`（归档缺失，已补证）。
- 当天提交语义（优先）：当前未发现独立提交记录，按工作区学习证据补证。
- 与语义直接对应的代码证据：
  - `07_面向对象/property.ipynb`
  - `07_面向对象/time.ipynb`
- 补证说明（显式）：本日内容基于 notebook 运行结果与代码单元输出整理。

## ✅ 今日目标
- [x] 理解 getter/setter 与 `@property` 的接口差异。
- [x] 掌握只读属性的实现与典型报错场景。
- [x] 完成 `datetime` 的构造、时间戳互转、字符串解析与格式化。

## 📚 章节内容
- 章节：面向对象（封装）+ Python 时间处理
- 小节：
  1) 私有属性与方法访问
  2) `@property` / `@name.setter`
  3) `datetime`、`timestamp`、`strptime`、`strftime`、时区对象
- 学习位置：`07_面向对象/`
- 对应练习：
  - `practice/07_面向对象/foundation/p-004-property-basic-encapsulation.md`
  - `practice/07_面向对象/advanced/p-005-readonly-property-validation.md`
  - `practice/07_面向对象/transfer/p-006-user-profile-timezone-model.md`
- 对应答案：
  - `answers/07_面向对象/foundation/p-004-property-basic-encapsulation.answer.md`
  - `answers/07_面向对象/advanced/p-005-readonly-property-validation.answer.md`
  - `answers/07_面向对象/transfer/p-006-user-profile-timezone-model.answer.md`
- 章节总结（3行内）：
  1. 从传统 `get_name/set_name` 过渡到 `@property`，接口更简洁但封装能力不变。
  2. 通过去掉 setter 验证“只读属性”的行为边界。
  3. 用 `datetime` 打通“对象、时间戳、字符串、时区”四种时间表达方式。

## 📌 今日内容（代码在做什么）
1. 在 `property.ipynb` 中先实现 `get_name/set_name`，再改写为 `@property` + setter 形式。  
2. 演示删除 setter 后写入属性会失败，用于理解只读设计。  
3. 在 `time.ipynb` 中完成：`now()`、`timestamp()`、`fromtimestamp()`、`strptime()`、`strftime()`、`timezone(timedelta(hours=8))`。

## 🧠 核心知识（底层原理）
- `@property` 把“方法调用语法”转换为“属性访问语法”，对外接口更稳定。
- setter 是写入入口，缺失 setter 的 property 默认只读。
- naive datetime 不含时区，aware datetime 带 `tzinfo`，两者在跨时区场景语义不同。
- 时间戳是统一交换格式，字符串/对象互转依赖明确格式模板。

## 💻 关键代码（精简 + 行为解释）
```python
import datetime

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


tom = Person("Tom")
tom.name = "Jerry"

now_dt = datetime.datetime.now()
ts = now_dt.timestamp()
restored = datetime.datetime.fromtimestamp(ts)
```

### 行为解释
- `tom.name` 的读写看起来像字段访问，实际走 getter/setter 逻辑。  
- `timestamp` 与 `fromtimestamp` 互转后能恢复同一时刻语义（精度允许范围内）。  
- 时间对象可进一步格式化输出，便于日志、报表和接口传输。

## ⚠️ 问题 / 坑（至少一个真实错误案例）
### 案例：删除 setter 后仍尝试赋值导致报错
- 错误现象：保留 `@property` 但去掉 `@name.setter` 后执行 `tom.name = 'jerry'` 抛出 `AttributeError`。  
- 根因：property 仅定义读取逻辑，未定义写入接口。  
- 修正：
  - 需要可写时补回 setter；或
  - 若业务要求只读，则保留当前实现并调整调用方行为。  
- 防再犯规则：定义 property 时先明确读写策略（只读/可写/受控写）。

## 🏋️ 强化训练（练习 / 答案 / 要求）
- 训练目标：把封装控制与时间处理能力迁移到可复用的数据模型中。
- 训练任务：
  1. 基础：完成 `p-004-property-basic-encapsulation`，将 getter/setter 改造为 property；  
  2. 进阶：完成 `p-005-readonly-property-validation`，实现只读属性并补齐异常用例；  
  3. 迁移：完成 `p-006-user-profile-timezone-model`，封装用户资料对象并处理时区时间展示。
- 难度分层：基础 / 进阶 / 迁移
- 验收标准：
  - 至少 1 个类同时包含可写属性与只读属性；
  - 至少 1 个失败用例验证“无 setter 不可写”；
  - 至少 1 个时间字段完成“字符串 ↔ datetime ↔ timestamp”闭环转换。
- practice 回链：
  - `practice/07_面向对象/foundation/p-004-property-basic-encapsulation.md`
  - `practice/07_面向对象/advanced/p-005-readonly-property-validation.md`
  - `practice/07_面向对象/transfer/p-006-user-profile-timezone-model.md`
- answers 回链：
  - `answers/07_面向对象/foundation/p-004-property-basic-encapsulation.answer.md`
  - `answers/07_面向对象/advanced/p-005-readonly-property-validation.answer.md`
  - `answers/07_面向对象/transfer/p-006-user-profile-timezone-model.answer.md`

## 🧩 我的理解（第一人称）
- 我现在能清楚解释：为什么 property 能在不改变调用方式的前提下增强封装。  
- 我还模糊的点：描述符协议（`__get__`/`__set__`）和 property 的关系细节。  
- 我准备怎么补：下一步补一个自定义描述符，与 property 并排对照。

## 🚀 延伸（下一步学习）
- 下一步主题：描述符协议与属性访问底层机制。  
- 推荐练习：
  1. 写一个只读描述符并挂到类属性；
  2. 对比描述符与 property 的使用边界；
  3. 将时间字段验证逻辑放进 setter/描述符里统一控制。

## 📎 回链索引
- 章节目录：`07_面向对象/`
- 关键文件：
  - `07_面向对象/property.ipynb`
  - `07_面向对象/time.ipynb`

## ✅ 完成度自检
- [x] 已包含至少 1 个真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含强化训练（目标/任务/验收/答案回链）
- [x] 已限定证据来源并显式标注补证方式
- [x] 已给出下一步可执行学习计划
