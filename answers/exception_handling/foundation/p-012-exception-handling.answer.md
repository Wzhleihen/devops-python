# P-012 参考答案：异常处理 — try/except/raise 与自定义异常

---

## 题目一：异常捕获与层级

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None


def safe_index(lst, idx):
    try:
        return lst[idx]
    except (IndexError, TypeError):
        return 'N/A'


# 验证
assert safe_divide(10, 2) == 5.0
assert safe_divide(10, 0) is None
assert safe_divide('a', 2) is None

assert safe_index([1, 2, 3], 1) == 2
assert safe_index([1, 2, 3], 10) == 'N/A'
assert safe_index([1, 2, 3], 'a') == 'N/A'
print('题目一 全部通过')
```

**要点**：
- except 可以用元组同时捕获多个同级异常：`except (IndexError, TypeError)`。
- 先窄后宽的原则：如果同时写了 `except Exception` 和 `except ZeroDivisionError`，必须把具体异常放前面，否则永远不会走到具体分支。

---

## 题目二：自定义异常层级 + raise

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f'{field}: {message}')


class TypeValidationError(ValidationError):
    def __init__(self, field, expected_type):
        super().__init__(field, f'expected type {expected_type.__name__}')
        self.expected_type = expected_type


class RangeValidationError(ValidationError):
    def __init__(self, field, value, min_val, max_val):
        super().__init__(field, f'{value} not in range [{min_val}, {max_val}]')
        self.value = value
        self.min_val = min_val
        self.max_val = max_val


def validate_age(value):
    if not isinstance(value, int):
        raise TypeValidationError('age', int)
    if value < 0 or value > 150:
        raise RangeValidationError('age', value, 0, 150)
    return value


# 验证
assert validate_age(25) == 25

try:
    validate_age('abc')
except TypeValidationError as e:
    assert e.field == 'age'
    print(f'捕获 TypeValidationError: {e}')

try:
    validate_age(-1)
except RangeValidationError as e:
    print(f'捕获 RangeValidationError: {e}')

try:
    validate_age('abc')
except ValidationError:
    print('父类 ValidationError 也能捕获子类异常')

print('题目二 全部通过')
```

**要点**：
- 自定义异常的 `__init__` 中调用 `super().__init__(msg)` 确保 `str(e)` 有意义。
- 异常可以携带结构化属性（`field`、`expected_type`、`value`），方便上层代码程序化处理。
- 子类异常能被父类 `except` 匹配 — 这就是异常层级设计的价值。

---

## 题目三：异常 + logging 集成校验器

```python
import logging


class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors
        msg = '; '.join(str(e) for e in errors)
        super().__init__(msg)


class FieldError:
    def __init__(self, field, message):
        self.field = field
        self.message = message

    def __str__(self):
        return f'{self.field}: {self.message}'


class Validator:
    def __init__(self, rules):
        self.rules = rules
        self.logger = logging.getLogger('validator')
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')

            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            self.logger.addHandler(sh)

            fh = logging.FileHandler('validation.log')
            fh.setFormatter(fmt)
            self.logger.addHandler(fh)

    def validate(self, data):
        errors = []
        for field, (expected_type, min_val, max_val) in self.rules.items():
            value = data.get(field)

            if not isinstance(value, expected_type):
                err = FieldError(field, f'expected {expected_type.__name__}, got {type(value).__name__}')
                errors.append(err)
                self.logger.error(str(err))
                continue

            if value < min_val or value > max_val:
                err = FieldError(field, f'{value} not in [{min_val}, {max_val}]')
                errors.append(err)
                self.logger.error(str(err))

        if errors:
            raise ValidationError(errors)

        self.logger.info(f'Validation passed for {list(data.keys())}')


# 验证
rules = {
    'age': (int, 0, 150),
    'score': (float, 0.0, 100.0),
}
v = Validator(rules)

v.validate({'age': 25, 'score': 88.5})
print('正常数据通过')

try:
    v.validate({'age': 'young', 'score': 200.0})
except ValidationError as e:
    assert len(e.errors) == 2
    print(f'捕获 {len(e.errors)} 个错误: {e}')

print('题目三 全部通过')
```

**要点**：
- 校验器不在第一个错误处中断，而是收集所有错误后一次性抛出 — 这是生产中常见的"批量校验"模式。
- logging 同时输出到控制台和文件：两个 Handler（StreamHandler + FileHandler）挂在同一个 Logger 上。
- 检查 `if not self.logger.handlers` 避免重复添加 Handler（day24 错误案例的教训）。
- `FieldError` 是普通类而非异常类 — 用于结构化存储错误信息；最终统一包装在 `ValidationError` 中抛出。
