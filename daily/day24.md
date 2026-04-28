# Day 24 - logging 模块体系 + OOP 综合作业实战 + argparse 与高阶函数

📅 日期：2026-04-28  
⏱ 距离上次学习：5 天

---

## 📦 证据归档（先归档，后补证）
- 与语义直接对应的代码证据：
  - `logging/demo01.py` — Logger/Handler/Formatter 三层体系演示
  - `logging/demo02.py` — basicConfig 快速配置
  - `作业/面向对象/temperature-demo01.py` — Temperature 工具类（property + classmethod 综合）
  - `作业/面向对象/share-demo01.py` — Shape 继承体系 + SerializableMixin 序列化
  - `作业/ls业务功能的实现/argparse-ls-demo01.py` — argparse 参数解析 + ls 功能实现
  - `作业/ls业务功能的实现/argarse-ls-full.py` — ls 精简重构版
  - `作业/高阶函数本质/t1.py` — sorted + key 高阶函数应用

## ✅ 今日目标
- [x] 理解 logging 模块 Logger → Handler → Formatter 三层架构
- [x] 掌握 getLogger 的单例语义与 EffectiveLevel 向上查找机制
- [x] 综合运用 property/classmethod/Mixin 完成 Temperature 和 Shape 作业
- [x] 使用 argparse 实现带 `-a/-l/-h/-r` 参数的 ls 命令
- [x] 理解 sorted 的 key 参数作为高阶函数的本质

## 📚 章节内容与学习位置
- 章节：logging 模块 / 面向对象综合 / 标准库应用
- 小节：
  1) Logger/Handler/Formatter 三层体系
  2) Temperature 温度转换工具类
  3) Shape 继承 + SerializableMixin 序列化
  4) argparse 实现 ls 命令
  5) 高阶函数 sorted + key
- 学习位置：`logging/`, `作业/面向对象/`, `作业/ls业务功能的实现/`, `作业/高阶函数本质/`
- 对应练习：
  - `practice/logging/foundation/p-009-logging-basics.md`
  - `practice/07_面向对象/transfer/p-010-oop-comprehensive.md`
- 对应答案：
  - `answers/logging/foundation/p-009-logging-basics.answer.md`
  - `answers/07_面向对象/transfer/p-010-oop-comprehensive.answer.md`

## 🧠 核心知识（机制层）

### 1. logging 三层体系
- **Logger**：日志记录器，通过 `getLogger(name)` 获取；同名返回同一实例（内部用字典缓存）。
- **Handler**：决定日志输出到哪里（StreamHandler → 控制台，FileHandler → 文件）。一个 Logger 可挂多个 Handler。
- **Formatter**：决定日志输出格式，挂在 Handler 上。
- `logging.basicConfig()` 是对 root logger 的快捷配置（level/format/stream 三件套）。
- **EffectiveLevel**：当前 logger 未设置 level 时，沿 parent 链向上查找第一个非 NOTSET 的 level。

### 2. OOP 综合应用模式
- **Temperature**：以 `_c` 为内部标准单位，通过 `@property` 惰性计算 `f/k`，`@classmethod` 提供无状态转换方法 → "工具类"模式。
- **Shape 体系**：基类用 `raise NotImplementedError` 强制子类实现 `area`；子类用 `_area` 缓存避免重复计算。
- **SerializableMixin**：按职责切片，通过多继承给 Circle 追加序列化能力，不侵入 Shape 体系。

### 3. argparse + 高阶函数
- `argparse.ArgumentParser` 声明参数 → `parse_args()` 解析 → 命名空间对象访问。
- `sorted(iterable, key=func)` 中 key 是典型的高阶函数用法：传入函数对象，由 sorted 内部回调。

## 💻 关键代码（精简）

```python
# logging 三层体系
import logging, sys
FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT, stream=sys.stdout)

root = logging.getLogger()
h1 = logging.StreamHandler()
h1.setFormatter(logging.Formatter('** %(message)s **'))
root.addHandler(h1)
logging.info('test')  # 两个 handler 分别输出不同格式
```

```python
# Temperature 工具类核心
class Temperature:
    def __init__(self, t, unit="c"):
        self._c = t if unit == "c" else self.f2c(t) if unit == "f" else self.k2c(t)
    @property
    def f(self): return self.c2f(self._c)
    @classmethod
    def c2f(cls, c): return 9 * c / 5 + 32
```

```python
# Shape + Mixin
class SerializableMixin:
    def dumps(self, t="json"):
        return json.dumps(self.__dict__)

class SerializableCircle(SerializableMixin, Circle): pass
```

## ⚠️ 真实错误案例（现象/根因/修正/防再犯）

### 案例 1：logging 输出重复
- 错误现象：一条 `logging.info('test')` 在控制台出现两次，格式不同。
- 根因：`basicConfig` 给 root logger 已添加一个 StreamHandler，手动又 `addHandler(h1)` 追加了第二个 → 每条消息遍历所有 handler 各输出一次。
- 修正：理解"一条消息会遍历 logger 挂载的所有 handler"，按需控制 handler 数量。
- 防再犯规则：添加 handler 前先检查 `logger.handlers`，避免重复挂载。

### 案例 2：Mixin 中 f-string 未生效
- 错误现象：`PrintableMixin.print()` 输出 `*** {self.content} ***` 而非变量值。
- 根因：字符串用了普通引号而非 f-string（`'*** {self.content} ***'` 缺少 `f` 前缀）。
- 修正：改为 `f'*** {self.content} ***'`。
- 防再犯规则：包含 `{}` 插值的字符串必须检查是否有 `f` 前缀。

## 🏋️ 强化训练（分层）
- 基础：配置 logging 输出到文件和控制台，验证 EffectiveLevel 向上查找。
- 进阶：实现 Temperature 增加 `__repr__` 和链式调用；给 Triangle 追加 `PerimeterMixin`。
- 迁移：用 argparse + pathlib 实现 `find` 命令的简化版（支持 `-name` 和 `-type`）。
- 验收标准：
  - logging 练习：至少创建 2 个 handler、1 个自定义 formatter，日志同时输出到文件和控制台；
  - OOP 练习：至少 1 处 Mixin 组合 + 1 处 property 惰性计算；
  - argparse 练习：至少支持 2 个可选参数，输出格式化文件列表。
- practice 回链：
  - `practice/logging/foundation/p-009-logging-basics.md`
  - `practice/07_面向对象/transfer/p-010-oop-comprehensive.md`
- answers 回链：
  - `answers/logging/foundation/p-009-logging-basics.answer.md`
  - `answers/07_面向对象/transfer/p-010-oop-comprehensive.answer.md`

## 🧩 我的理解（第一人称）
- logging 的三层分离思想和 web 框架的中间件很像：Logger 管"谁记"，Handler 管"往哪输"，Formatter 管"长什么样"。
- Temperature 作业让我真正体会到 `@classmethod` 做"无状态工具方法" + `@property` 做"惰性缓存"的配合。
- Shape + SerializableMixin 是 day23 Mixin 知识的直接落地验证。
- argparse 实现 ls 让我把 pathlib/stat/datetime/高阶函数串联起来了。

## 🚀 延伸（下一步学习）
- 下一步主题：logging 进阶（FileHandler/RotatingFileHandler/日志分级输出）+ 装饰器进阶。
- 推荐动作：
  1. 用 RotatingFileHandler 实现日志轮转；
  2. 用装饰器替代 Mixin 实现 Serializable 能力注入并对比；
  3. 扩展 ls 命令支持递归 `-R` 参数。

## ✅ 完成度自检
- [x] 已包含真实错误案例（现象/根因/修正/防再犯）
- [x] 已包含强化训练（基础/进阶/迁移 + 验收标准）
- [x] 已包含 practice/answers 回链
- [x] 已限定证据来源并显式标注
