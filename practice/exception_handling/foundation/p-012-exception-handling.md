# P-012 异常处理：try/except/raise 与自定义异常

> 对应 day25 — 异常处理（try/except/raise/自定义异常/logging 集成）

---

## 题目一（基础）：异常捕获与层级

编写函数 `safe_divide(a, b)`：

1. 正常情况返回 `a / b` 的结果。
2. 当 `b == 0` 时捕获 `ZeroDivisionError`，返回 `None`。
3. 当 `a` 或 `b` 不是数字时捕获 `TypeError`，返回 `None`。
4. except 顺序：先窄（具体异常）后宽。

### 验收标准
```python
assert safe_divide(10, 2) == 5.0
assert safe_divide(10, 0) is None
assert safe_divide('a', 2) is None
```

再编写函数 `safe_index(lst, idx)`：
1. 返回 `lst[idx]`。
2. 捕获 `IndexError`，返回默认值 `"N/A"`。
3. 捕获 `TypeError`（如 idx 不是整数），返回 `"N/A"`。

```python
assert safe_index([1, 2, 3], 1) == 2
assert safe_index([1, 2, 3], 10) == 'N/A'
assert safe_index([1, 2, 3], 'a') == 'N/A'
```

---

## 题目二（进阶）：自定义异常层级 + raise

设计一个校验体系：

1. 基类 `ValidationError(Exception)`，接收 `field` 和 `message` 参数。
2. 子类 `TypeValidationError`：字段类型不符。
3. 子类 `RangeValidationError`：字段值超出范围。

编写 `validate_age(value)` 函数：
- 若 `value` 不是 `int`，raise `TypeValidationError`。
- 若 `value < 0` 或 `value > 150`，raise `RangeValidationError`。
- 否则返回 `value`。

### 验收标准
```python
assert validate_age(25) == 25

try:
    validate_age('abc')
except TypeValidationError as e:
    assert e.field == 'age'

try:
    validate_age(-1)
except RangeValidationError as e:
    assert 'range' in str(e).lower() or 'age' in str(e).lower()

# 宽捕获：子类能被父类 except 匹配
try:
    validate_age('abc')
except ValidationError:
    pass  # TypeValidationError 是 ValidationError 子类，可被捕获
```

---

## 题目三（迁移）：异常 + logging 集成校验器

实现 `Validator` 类：

1. 构造时接收 `rules` 字典，格式：`{'field_name': (type, min, max)}`。
2. `validate(data: dict)` 方法遍历 rules 逐字段校验。
3. 校验失败时：
   - 用 `logging.error()` 记录错误详情。
   - 收集所有错误到列表，不在第一个错误处中断。
4. 校验完成后，若有错误则 raise `ValidationError`，携带所有错误信息。
5. logging 同时输出到控制台和文件 `validation.log`。

### 验收标准
```python
import logging

rules = {
    'age': (int, 0, 150),
    'score': (float, 0.0, 100.0),
}
v = Validator(rules)

# 正常数据
v.validate({'age': 25, 'score': 88.5})  # 不抛异常

# 异常数据：两个字段都有问题
try:
    v.validate({'age': 'young', 'score': 200.0})
except ValidationError as e:
    errors = e.errors
    assert len(errors) == 2  # 两个校验错误都被收集
```

---

## 提示
- `raise` 的对象必须是 `BaseException` 的子类实例。
- `sys.exit()` 抛出 `SystemExit`，继承自 `BaseException` 而非 `Exception`，`except Exception` 捕获不到。
- 异常捕获按继承层级匹配：先写子类 except，再写父类 except。
- 自定义异常可以添加任意属性（如 `field`、`errors`），增强错误信息的结构化。
