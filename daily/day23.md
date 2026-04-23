# Day 23 - 继承初始化、重写协作与 Mixin 复用（完整AI分析版）

📅 日期：2026-04-23  
⏱ 距离上次学习：2 天

---

## 📦 证据归档（先归档，后补证）
- 归档目录检查：未发现 `归档/2026/2026-04-23`（归档缺失，已补证）。
- 当天提交语义（优先）：当前以工作区学习证据补证。
- 与语义直接对应的代码证据：
  - `07_面向对象/extend-init.ipynb`
- 补证说明（显式）：本日结论来自 notebook 中“子类 `__init__` 与 `super()`、重写调用链、Mixin 组合”演示单元。

## ✅ 今日目标
- [x] 解释“子类自定义 `__init__` 时父类初始化不会自动执行”的机制。
- [x] 熟练使用 `super()` 在重写中复用父类行为。
- [x] 通过 `mro()` 理解 Mixin 多继承下的方法分派顺序。

## 📚 章节内容与学习位置
- 章节：面向对象（继承进阶）
- 小节：
  1) 继承与初始化协作
  2) 方法重写与父类逻辑复用
  3) Mixin 组合与 MRO
- 学习位置：`07_面向对象/extend-init.ipynb`
- 对应练习：
  - `practice/07_面向对象/advanced/p-008-init-override-mixin-mro.md`
- 对应答案：
  - `answers/07_面向对象/advanced/p-008-init-override-mixin-mro.answer.md`

## 🧠 核心知识（机制层）
- 当子类定义了自己的 `__init__`，父类 `__init__` 不会被隐式调用；需要显式 `super().__init__(...)`。
- `super()` 的查找遵循当前类的 MRO，不是“写死父类名”的静态绑定。
- Mixin 的本质是“按职责切片组合能力”，方法最终由 MRO 决定落点。
- `isinstance(obj, Parent)` 基于继承链判断，可用于验证对象的类型关系。

## 💻 关键代码（精简）
```python
class A:
    def __init__(self):
        self.a1 = 100

class B(A):
    def __init__(self):
        super().__init__()
        self.b1 = 200

c = B()
print(c.__dict__)  # {'a1': 100, 'b1': 200}
```

```python
class PrintableMixin:
    def print(self):
        print(f"*** {self.content} ***")

class Document:
    def __init__(self, content):
        self.content = content

class Word(Document):
    pass

class PrintableWord(PrintableMixin, Word):
    pass

print(PrintableWord.mro())
```

## ⚠️ 真实错误案例（现象/根因/修正/防再犯）
### 案例：子类重写 `__init__` 后遗漏父类初始化
- 错误现象：子类实例访问父类应有属性时报 `AttributeError`（父类属性未创建）。
- 根因：在子类 `__init__` 中未调用 `super().__init__()`，导致父类初始化逻辑被跳过。
- 修正：将 `super().__init__(...)` 放在子类 `__init__` 首段，再初始化子类扩展字段。
- 防再犯规则：只要子类重写 `__init__` 且依赖父类状态，默认先写 `super().__init__(...)`。

## 🏋️ 强化训练（分层）
- 基础：写 `A/B` 两层继承，分别演示“遗漏 super 报错”和“补上 super 正常”。
- 进阶：实现 `Animal -> Dog` 重写 `shout`，要求父类逻辑 + 子类扩展顺序正确。
- 迁移：设计 `LoggableMixin` + `Document` 组合类，打印 `mro()` 并解释为何方法会命中某层。
- 验收标准：
  - 至少 1 处展示“错误前后对照”输出；
  - 至少 1 处展示并解释 `__mro__` 或 `mro()`；
  - 至少 2 处 `super()`（初始化 + 普通方法各一次）。
- practice 回链：
  - `practice/07_面向对象/advanced/p-008-init-override-mixin-mro.md`
- answers 回链：
  - `answers/07_面向对象/advanced/p-008-init-override-mixin-mro.answer.md`

## 🧩 我的理解（第一人称）
- 我现在能稳定判断：子类一旦自定义 `__init__`，就要主动接上父类初始化链。
- 我最大的收获是：Mixin 不是“乱继承”，而是按能力拆分后通过 MRO 组合。
- 下一步我会补一个“多 Mixin + 同名方法”的最小例子，进一步巩固查找顺序。

## 🚀 延伸（下一步学习）
- 下一步主题：多继承冲突与协作式 `super()` 链。
- 推荐动作：
  1. 构建同名方法冲突案例并观察 MRO；
  2. 练习“每层都调用 `super()`”的协作式写法；
  3. 对比“显式父类名调用”与 `super()` 在可维护性上的差异。

## ✅ 完成度自检
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含强化训练（基础/进阶/迁移 + 验收标准）
- [x] 已包含 practice/answers 回链
- [x] 已限定证据来源并显式补证
