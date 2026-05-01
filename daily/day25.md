# Day 25 - 魔术方法（实例化/字符串/布尔）与异常处理

📅 日期：2026-05-01  
⏱ 距离上次学习：3 天

---

## 📦 证据归档（先归档，后补证）
- 与语义直接对应的代码证据：
  - `Magical_method/instantiation_demo01.py` — `__new__` 与 `__init__` 实例化流程
  - `Magical_method/str_demo02.py` — `__str__` / `__repr__` / `__bytes__` 字符串协议
  - `Magical_method/bool_demo03.py` — `__bool__` / `__len__` 布尔协议
  - `exception_handling/demo01.py` — try/except/raise/自定义异常
  - `exception_handling/demo02.py` — 异常捕获 + logging 错误记录

## ✅ 今日目标
- [x] 理解 `__new__` 与 `__init__` 的分工：构造 vs 初始化
- [x] 掌握 `__str__` / `__repr__` / `__bytes__` 三者的触发场景与优先级
- [x] 掌握 `__bool__` / `__len__` 的回退链（bool → `__bool__` → `__len__` → 默认 True）
- [x] 理解 try/except/raise 异常处理流程与异常层级
- [x] 掌握自定义异常与 logging 集成异常记录

## 📚 章节内容与学习位置
- 章节：魔术方法（Magical Methods）/ 异常处理（Exception Handling）
- 小节：
  1) `__new__` 实例化机制与 MRO 关系
  2) `__str__` / `__repr__` / `__bytes__` 字符串表示协议
  3) `__bool__` / `__len__` 布尔判定协议
  4) try/except/raise 异常控制流
  5) 自定义异常 + logging 集成
- 学习位置：`Magical_method/`, `exception_handling/`
- 对应练习：
  - `practice/07_面向对象/advanced/p-011-magic-methods-str-bool.md`
  - `practice/exception_handling/foundation/p-012-exception-handling.md`
- 对应答案：
  - `answers/07_面向对象/advanced/p-011-magic-methods-str-bool.answer.md`
  - `answers/exception_handling/foundation/p-012-exception-handling.answer.md`

## 🧠 核心知识（机制层）

### 1. `__new__` 与 `__init__` 的分工
- `__new__(cls)` 是**构造方法**：从无到有创建实例对象，返回值决定最终实例类型。
- `__init__(self)` 是**初始化方法**：在 `__new__` 返回实例后填充属性。
- 调用链：`A(args)` → `A.__new__(A, args)` → 若返回 A 的实例 → `A.__init__(instance, args)`。
- `__new__` 返回非本类实例时，`__init__` **不会被调用**。
- `return super().__new__(cls)` 沿 MRO 向上查找 `object.__new__`，不能写 `return cls(...)` 否则无限递归。

### 2. 字符串表示三件套
- `__str__`：面向**用户**的可读字符串，`str(obj)` / `print(obj)` / f-string 触发。
- `__repr__`：面向**开发者**的精确表示，交互式解释器 / `[obj]` 等容器展示触发。
- `__bytes__`：`bytes(obj)` 触发，适合序列化场景（如 JSON encode）。
- 回退规则：未定义 `__str__` 时，`str()` 会回退到 `__repr__`；反之不成立。

### 3. 布尔判定协议
- `bool(obj)` 优先调用 `__bool__`，未定义则回退到 `__len__`（长度 0 为 False）。
- 两者都未定义时，任何实例默认为 `True`。
- 类本身（`bool(MyClass)`）永远为 `True`，因为类是 type 的实例。

### 4. 异常处理机制
- `try/except` 按异常类的继承层级匹配：先窄后宽。
- `raise` 主动抛出异常：`raise ExceptionType('msg')`。
- `raise` 的对象必须是 `BaseException` 的子类实例，`raise 100` → `TypeError`。
- `sys.exit(code)` 抛出 `SystemExit`（继承 `BaseException` 而非 `Exception`），`except Exception` 捕获不到。
- `raise NotImplementedError` 用于抽象方法占位，强制子类实现。

### 5. 自定义异常 + logging 集成
- 继承 `Exception` 即可创建自定义异常：`class MyException(Exception): pass`。
- except 块中用 `logging.error(str(e))` 记录异常，不影响程序继续执行。
- `e.args` 是异常携带的参数元组，`str(e)` 取第一个参数的字符串形式。

## 💻 关键代码（精简）

```python
# __new__ 与 __init__ 分工
class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # 沿 MRO 调用 object.__new__
    def __init__(self, x, y):
        self.x = x
        self.y = y

t = A(4, 5)  # __new__ 创建实例 → __init__ 填充属性
```

```python
# __str__ / __repr__ / __bytes__
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f'(Point {self.x}, {self.y})'
    def __repr__(self):
        return f'<P{self.x}, {self.y}>'
    def __bytes__(self):
        return json.dumps({"x": self.x, "y": self.y}).encode()

print([Point(4,5)])  # 容器内触发 __repr__：[<P4, 5>]
```

```python
# __bool__ / __len__ 回退链
class B:
    def __bool__(self):
        return bool(len(self))
    def __len__(self):
        return 1

print(bool(B()))  # __bool__ → __len__ → 1 → True
```

```python
# 异常处理 + logging
import logging
logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.INFO)

try:
    open('test1.txt')
except FileNotFoundError as e:
    logging.error(str(e))  # 记录异常但不中断程序
```

## ⚠️ 真实错误案例（现象/根因/修正/防再犯）

### 案例 1：`__new__` 中 `return cls(...)` 导致无限递归
- 错误现象：`A(4, 5)` 调用后 `RecursionError: maximum recursion depth exceeded`。
- 根因：`__new__` 中写 `return cls(*args, **kwargs)` 等价于再次调用 `cls()`，触发 `cls.__new__` → 无限递归。
- 修正：改为 `return super().__new__(cls)` 或 `return object.__new__(cls)`。
- 防再犯规则：`__new__` 中永远不要用 `cls()` 创建实例，必须走 `super().__new__(cls)` 或 `object.__new__(cls)`。

### 案例 2：`[obj]` 输出不符合预期 — 未定义 `__repr__`
- 错误现象：`print([Point(4,5)])` 输出 `[<__main__.Point object at 0x...>]` 而非自定义格式。
- 根因：列表/元组等容器内部对元素调用 `__repr__` 而非 `__str__`，未定义 `__repr__` 时走 `object.__repr__`。
- 修正：为 Point 添加 `__repr__` 方法。
- 防再犯规则：需要在容器中展示的对象，必须定义 `__repr__`；`__str__` 只影响直接 `print/str/f-string`。

## 🏋️ 强化训练（分层）
- 基础：实现一个 `Color` 类，定义 `__str__`（输出 `rgb(r,g,b)`）和 `__repr__`（输出 `Color(r,g,b)`），验证在容器和 f-string 中的不同表现。
- 进阶：实现 `Singleton` 类，利用 `__new__` 实现单例模式；实现 `Container` 类，通过 `__len__` 和 `__bool__` 实现"空容器为 False"语义。
- 迁移：实现带自定义异常层级的简易校验器 — `ValidationError` 基类 + `TypeValidationError` / `RangeValidationError` 子类，配合 logging 记录所有校验失败。
- 验收标准：
  - 魔术方法练习：至少覆盖 `__str__/__repr__/__bool__` 三个协议，能区分容器内与直接打印的输出差异；
  - 单例练习：连续创建两个实例，`is` 比较返回 `True`；
  - 异常练习：至少 2 层自定义异常继承，except 按先窄后宽捕获，日志输出到文件。
- practice 回链：
  - `practice/07_面向对象/advanced/p-011-magic-methods-str-bool.md`
  - `practice/exception_handling/foundation/p-012-exception-handling.md`
- answers 回链：
  - `answers/07_面向对象/advanced/p-011-magic-methods-str-bool.answer.md`
  - `answers/exception_handling/foundation/p-012-exception-handling.answer.md`

## 🧩 我的理解（第一人称）
- `__new__` 和 `__init__` 的关系就像"建房子"和"装修"：`__new__` 把毛坯房造出来，`__init__` 负责内部装修。如果 `__new__` 造的不是本类的房子，装修队（`__init__`）根本不会进场。
- `__str__` vs `__repr__` 的设计哲学很清晰：str 给用户看（友好），repr 给开发者看（精确可重建）。容器内用 repr 是因为容器本身在 repr 语境下需要精确展示每个元素。
- 异常层级和 logging 配合使用后，才真正理解"记录但不崩溃"的生产级错误处理思路。

## 🚀 延伸（下一步学习）
- 下一步主题：更多魔术方法（`__eq__/__hash__/__lt__` 比较协议、`__add__` 运算符重载）+ 异常处理进阶（finally/else/上下文管理器）。
- 推荐动作：
  1. 用 `__new__` 实现对象池（限制实例数量）；
  2. 实现 `__enter__/__exit__` 上下文管理器替代 try/finally；
  3. 用 `functools.total_ordering` 简化比较协议实现。

## ✅ 完成度自检
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含强化训练（基础/进阶/迁移 + 验收标准）
- [x] 已包含 practice/answers 回链
- [x] 已限定证据来源并显式标注
