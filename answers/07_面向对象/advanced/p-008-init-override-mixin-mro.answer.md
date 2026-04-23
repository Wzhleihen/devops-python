# p-008-init-override-mixin-mro.answer

## 参考实现
```python
class A:
    def __init__(self):
        self.a1 = 100


class BrokenB(A):
    def __init__(self):
        self.b1 = 200


class FixedB(A):
    def __init__(self):
        super().__init__()
        self.b1 = 200


class Animal:
    def __init__(self, name):
        self.name = name

    def shout(self):
        print(f"{self.name} is shouting")


class Dog(Animal):
    def shout(self):
        super().shout()
        print("wangwang")


class Document:
    def __init__(self, content):
        self.content = content


class PrintableMixin:
    def print(self):
        print(f"*** {self.content} ***")


class PrintableWord(PrintableMixin, Document):
    pass


print("--- init 错误复现 ---")
b1 = BrokenB()
try:
    print(b1.a1)
except Exception as e:
    print("broken init error:", e)

print("--- init 修复后 ---")
b2 = FixedB()
print(b2.__dict__)

print("--- override + super ---")
d = Dog("ahuang")
d.shout()

print("--- mixin mro ---")
print(PrintableWord.__mro__)
pw = PrintableWord("hello")
pw.print()
```

## 关键说明
- 子类自定义 `__init__` 时必须显式接入父类初始化链；
- 重写方法中使用 `super()` 可以复用父类逻辑并保证顺序可控；
- Mixin 的方法命中依赖 MRO，`PrintableWord(PrintableMixin, Document)` 会优先找 `PrintableMixin.print`。

## 预期输出（示例）
```text
--- init 错误复现 ---
broken init error: 'BrokenB' object has no attribute 'a1'
--- init 修复后 ---
{'a1': 100, 'b1': 200}
--- override + super ---
ahuang is shouting
wangwang
--- mixin mro ---
(<class '__main__.PrintableWord'>, <class '__main__.PrintableMixin'>, <class '__main__.Document'>, <class 'object'>)
*** hello ***
```
