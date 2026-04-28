"""
md
 图形
- 1、有Shape基类,要求所有子类都必须提供面积的计算,子类有三角形、矩形、圆。
- 2、上题圆类的数据可序列化

三角形面积——海伦公式:

$$p = (a+b+c)/2$$

$$S = \sqrt{p(p-a)(p-b)(p-c)}$$

"""

# 1、有Shape基类,要求所有子类都必须提供面积的计算,子类有三角形、矩形、圆。
# 数据尽量少量计算，使用到就计算，计算结果缓存起来，避免重复计算

import math


class shape:
    def __init__(self):
        self._area = None

    @property
    def area(self):
        raise NotImplementedError("基类不可实例化")


class Triangle(shape):
    def __init__(self, a, b, c):
        super().__init__()
        self._a = a
        self._b = b
        self._c = c

    @property
    def area(self):
        if self._area is None:
            p = (self._a + self._b + self._c) / 2
            self._area = math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return self._area


class Rectangle(shape):
    def __init__(self, width, height):
        super().__init__()
        self._width = width
        self._height = height

    @property
    def area(self):
        if self._area is None:
            self._area = self._width * self._height
        return self._area


class Circle(shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius**2
        return self._area


import json
import msgpack


class SerializableMixin:
    def dumps(self, t="json"):
        if t == "json":
            print(self.__dict__)
            return json.dumps(self.__dict__)
        elif t == "msgpack":
            return msgpack.dumps(self.__dict__)
        else:
            raise ValueError("不支持的序列化类型")


class SerializableCircle(SerializableMixin, Circle):
    pass


# c = Circle(3)
# print(c.area)

# shapes = (Triangle(3, 4, 5), Rectangle(3, 4), Circle(3))
# for s in shapes:
#     print(s.__class__.__name__, s.area)

c = SerializableCircle(4)
print(c.area)
print(c.dumps("json"))
print(c.dumps("msgpack"))
