# P-010 OOP 综合迁移训练 — 参考答案

📎 回链：`daily/day24.md`  
📅 日期：2026-04-28

---

## 第一题：Temperature 增强

```python
class Temperature:
    def __init__(self, t, unit="c"):
        self._c = None
        self._f = None
        self._k = None
        if unit == "f":
            self._f = t
            self._c = self.f2c(t)
        elif unit == "k":
            self._k = t
            self._c = self.k2c(t)
        else:
            self._c = t

    @property
    def c(self):
        return self._c

    @property
    def f(self):
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f

    @property
    def k(self):
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k

    @classmethod
    def c2f(cls, c): return 9 * c / 5 + 32
    @classmethod
    def f2c(cls, f): return 5 * (f - 32) / 9
    @classmethod
    def c2k(cls, c): return c + 273.15
    @classmethod
    def k2c(cls, k): return k - 273.15

    def __repr__(self):
        return f"Temperature({self.c:.1f}°C / {self.f:.1f}°F / {self.k:.2f}K)"

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.c - other.c) < 1e-9

    def __add__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return Temperature(self.c + other.c)


# 测试
t1 = Temperature(100)
print(repr(t1))  # Temperature(100.0°C / 212.0°F / 373.15K)

print(Temperature(0) == Temperature(32, "f"))  # True

t2 = Temperature(20) + Temperature(30)
print(t2.c)  # 50
```

**要点**：
- `__eq__` 使用浮点容差比较，避免精度问题。
- `__add__` 返回新 Temperature 对象，不修改原对象。
- `NotImplemented`（不是 `NotImplementedError`）让 Python 尝试反向操作。

## 第二题：Shape + PerimeterMixin

```python
import math

class Shape:
    def __init__(self):
        self._area = None

    @property
    def area(self):
        raise NotImplementedError

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self._a, self._b, self._c = a, b, c

    @property
    def area(self):
        if self._area is None:
            p = (self._a + self._b + self._c) / 2
            self._area = math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return self._area

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius ** 2
        return self._area

class PerimeterMixin:
    _perimeter = None

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._calc_perimeter()
        return self._perimeter

    def _calc_perimeter(self):
        raise NotImplementedError

class FullTriangle(PerimeterMixin, Triangle):
    def _calc_perimeter(self):
        return self._a + self._b + self._c

class FullCircle(PerimeterMixin, Circle):
    def _calc_perimeter(self):
        return 2 * math.pi * self._radius


# 测试
ft = FullTriangle(3, 4, 5)
print(ft.area)       # 6.0
print(ft.perimeter)  # 12

fc = FullCircle(5)
print(fc.area)       # 78.539...
print(fc.perimeter)  # 31.415...

# MRO 解释
print(FullTriangle.mro())
# [FullTriangle, PerimeterMixin, Triangle, Shape, object]
# FullTriangle → PerimeterMixin(提供 perimeter) → Triangle(提供 area) → Shape(基类) → object
```

**要点**：
- Mixin 通过 `_calc_perimeter` 模板方法将计算委托给子类，自身只管缓存逻辑。
- MRO 中 PerimeterMixin 在 Triangle 之前，因为写在继承列表左侧。

## 第三题：简化 find

```python
import argparse
from pathlib import Path
from fnmatch import fnmatch

parser = argparse.ArgumentParser("find", description="简化版 find 命令")
parser.add_argument("path", nargs="?", default=".", help="搜索路径")
parser.add_argument("-name", dest="pattern", help="文件名模式")
parser.add_argument("-type", dest="ftype", choices=["f", "d"], help="文件类型")

args = parser.parse_args()

root = Path(args.path).resolve()
for p in root.rglob("*"):
    if args.ftype == "f" and not p.is_file():
        continue
    if args.ftype == "d" and not p.is_dir():
        continue
    if args.pattern and not fnmatch(p.name, args.pattern):
        continue
    print(p)
```

**要点**：
- `rglob("*")` 递归遍历所有路径。
- `fnmatch` 支持 `*` 和 `?` 通配符，与 shell glob 语义一致。
- 过滤逻辑用 `continue` 跳过不匹配项，代码清晰。
