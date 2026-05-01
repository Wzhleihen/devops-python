# P-011 参考答案：魔术方法 — 实例化 / 字符串表示 / 布尔协议

---

## 题目一：Color 类

```python
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f'rgb({self.r}, {self.g}, {self.b})'

    def __repr__(self):
        return f'Color({self.r}, {self.g}, {self.b})'

    def __bytes__(self):
        return f'#{self.r:02x}{self.g:02x}{self.b:02x}'.encode()


# 验证
c = Color(255, 128, 0)
assert str(c) == 'rgb(255, 128, 0)'
assert repr(c) == 'Color(255, 128, 0)'
assert f'{c}' == 'rgb(255, 128, 0)'
assert bytes(c) == b'#ff8000'

print(c)        # rgb(255, 128, 0)   — __str__
print([c])      # [Color(255, 128, 0)] — 容器内 __repr__
print(bytes(c)) # b'#ff8000'          — __bytes__
```

**要点**：
- f-string 和 `print()` 都走 `__str__`。
- 列表的 `__repr__` 对每个元素调用 `__repr__`，所以容器内看到的是 `Color(...)` 而非 `rgb(...)`。
- `__bytes__` 使用 `{:02x}` 格式化为两位十六进制。

---

## 题目二 Part A：Singleton

```python
class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not Singleton._initialized:
            self.value = value
            Singleton._initialized = True


# 验证
s1 = Singleton(10)
s2 = Singleton(20)
assert s1 is s2
assert s1.value == 10
print(f's1.value={s1.value}, s2.value={s2.value}, same={s1 is s2}')
```

**要点**：
- `__new__` 每次都会被调用，通过类属性 `_instance` 缓存唯一实例。
- `__init__` 每次实例化都会被调用（因为 `__new__` 返回的是本类实例），所以需要 `_initialized` 标志位防止重复初始化。
- 这是最基础的单例实现；生产中还需考虑线程安全。

---

## 题目二 Part B：Container

```python
class Container:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return len(self) > 0

    def __repr__(self):
        return f'Container({self._items!r})'


# 验证
c = Container()
assert not c
assert len(c) == 0

c.add('a')
c.add('b')
assert c
assert len(c) == 2
assert repr(c) == "Container(['a', 'b'])"

c.remove('a')
assert len(c) == 1
print(f'bool={bool(c)}, len={len(c)}, repr={repr(c)}')
```

**要点**：
- `__bool__` 显式定义后优先于 `__len__`；这里两者保持一致语义。
- `{!r}` 在 f-string 中调用 `__repr__`，用于展示列表内容。
- 即使不定义 `__bool__`，Python 也会回退到 `__len__`：长度 0 为 False，非 0 为 True。

---

## 题目三：PooledObject 对象池

```python
class PooledObject:
    max_pool = 3
    _pool = []
    _index = 0

    def __new__(cls, *args, **kwargs):
        if len(cls._pool) < cls.max_pool:
            instance = super().__new__(cls)
            cls._pool.append(instance)
            return instance
        else:
            instance = cls._pool[cls._index % cls.max_pool]
            cls._index = (cls._index + 1) % cls.max_pool
            return instance

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f'PooledObject(id={self.id!r})'


# 验证
PooledObject.max_pool = 3
PooledObject._pool = []
PooledObject._index = 0

a = PooledObject('A')
b = PooledObject('B')
c = PooledObject('C')
print(a, b, c)  # 三个不同实例

d = PooledObject('D')  # 池满，复用 a
assert d is a
assert d.id == 'D'

e = PooledObject('E')  # 复用 b
assert e is b
assert e.id == 'E'

print(a, b, c)  # a.id='D', b.id='E', c.id='C'
```

**要点**：
- 对象池是 `__new__` 的经典应用：控制实例创建而非属性初始化。
- 池满后循环复用：用 `_index` 维护下一个被复用的位置。
- `__init__` 仍然会被调用（因为 `__new__` 返回的是本类实例），所以复用的实例会被重新初始化 — 这是有意为之的设计。
- 注意类属性 `_pool` 和 `_index` 是所有实例共享的。
