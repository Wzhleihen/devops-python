# P-011 魔术方法：实例化 / 字符串表示 / 布尔协议

> 对应 day25 — 魔术方法（`__new__/__str__/__repr__/__bytes__/__bool__/__len__`）

---

## 题目一（基础）：Color 类的字符串协议

实现 `Color` 类，满足以下要求：

1. `__init__(self, r, g, b)` 接收 RGB 三个整数。
2. `__str__` 返回 `rgb(r, g, b)` 格式（用户友好）。
3. `__repr__` 返回 `Color(r, g, b)` 格式（开发者精确表示）。
4. `__bytes__` 返回 `#RRGGBB` 的十六进制字符串编码后的字节。

### 验收标准
```python
c = Color(255, 128, 0)
assert str(c) == 'rgb(255, 128, 0)'
assert repr(c) == 'Color(255, 128, 0)'
assert f'{c}' == 'rgb(255, 128, 0)'            # f-string 走 __str__
assert [c].__repr__() == '[Color(255, 128, 0)]' # 容器内走 __repr__
assert bytes(c) == b'#ff8000'
```

---

## 题目二（进阶）：Singleton 单例 + Container 布尔语义

### Part A：Singleton
利用 `__new__` 实现单例模式：

1. 多次实例化 `Singleton()` 返回同一对象。
2. `__init__` 仅在首次创建时执行初始化。

```python
s1 = Singleton(10)
s2 = Singleton(20)
assert s1 is s2
assert s1.value == 10  # 不被第二次 __init__ 覆盖
```

### Part B：Container
实现 `Container` 类：

1. 内部用列表存储元素，支持 `add(item)` 和 `remove(item)`。
2. `__len__` 返回元素数量。
3. `__bool__` 基于 `__len__`，空容器为 `False`。
4. `__repr__` 返回 `Container([...])` 格式。

```python
c = Container()
assert not c                  # 空容器 False
c.add('a')
c.add('b')
assert c                      # 非空 True
assert len(c) == 2
assert repr(c) == "Container(['a', 'b'])"
```

---

## 题目三（迁移）：`__new__` 对象池

实现 `PooledObject` 类：

1. 池容量上限为 `max_pool`（类属性，默认 3）。
2. 当池未满时，`__new__` 创建新实例并加入池；池满时返回最早创建的实例（循环复用）。
3. 每个实例有 `id` 属性标识自己。

```python
PooledObject.max_pool = 3
a = PooledObject('A')
b = PooledObject('B')
c = PooledObject('C')
d = PooledObject('D')  # 池满，复用最早的实例
assert d is a
assert d.id == 'D'     # 但 id 被重新初始化
```

---

## 提示
- `__str__` 影响 `str()` / `print()` / f-string；`__repr__` 影响容器展示和交互式环境。
- `__new__` 返回非本类实例时 `__init__` 不会触发。
- 单例模式的关键是在类上缓存实例引用。
