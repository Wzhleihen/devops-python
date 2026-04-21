# p-007-inheritance-mro-private-attrs.answer

## 参考实现
```python
class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def shout(self):
        print(f"{self.get_name()} is shouting")


class Dog(Animal):
    def shout(self):
        super().shout()
        print("wang")


class A:
    def __init__(self):
        self.__b = 100

    def get_b(self):
        return self.__b


class B(A):
    def broken_show(self):
        return self.__b  # 会触发 AttributeError: _B__b

    def fixed_show(self):
        return self.get_b()


print("MRO:", Dog.__mro__)

d = Dog("dog")
d.shout()

b = B()
try:
    print(b.broken_show())
except Exception as e:
    print("broken_show error:", e)

print("fixed_show:", b.fixed_show())
```

## 关键说明
- `__b` 在 `A` 内会改写为 `_A__b`，`B` 内写 `self.__b` 会变成 `_B__b`；
- 修复核心是通过父类公开接口访问私有数据；
- `super()` 会按照 `Dog.__mro__` 决定调用链。

## 预期输出（示例）
```text
MRO: (<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
dog is shouting
wang
broken_show error: 'B' object has no attribute '_B__b'
fixed_show: 100
```
