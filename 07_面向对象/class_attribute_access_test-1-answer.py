# ===== 正确输出 =====


class Person:
    age = 3
    height = 175

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


tom = Person("Tom")
jerry = Person("Jerry", 20)


# 1
# Person.age = 30（修改类属性）
# tom.age = 18（实例属性，来自 __init__）
# jerry.age = 20（实例属性）
print(1, Person.age, tom.age, jerry.age)
# 1 30 18 20


# 2
# height 目前仍是类属性（没有实例覆盖）
print(2, Person.height, tom.height, jerry.height)
# 2 175 175 175


# 3
# jerry.height = 180 → 在 jerry.__dict__ 中创建实例属性
print(3, Person.height, tom.height, jerry.height)
# 3 175 175 180


# 4
# tom.height += 10 等价于：
# tom.height = tom.height + 10
# → 先从类取 175，再写入实例 → 185
print(4, Person.height, tom.height, jerry.height)
# 4 175 185 180


# 5
# Person.height += 15 → 类属性变为 190
# 注意：tom/jerry 已经有自己的 height，不受影响
print(5, Person.height, tom.height, jerry.height)
# 5 190 185 180


# 6
# 新增类属性 weight = 50
# 实例没有该属性 → 向上查类
print(6, Person.weight, tom.weight, jerry.weight)
# 6 50 50 50


# 7
# tom.__dict__ 中确实有 height（因为第4步创建了实例属性）
print(7, tom.__dict__["height"])
# 7 185


# 8（如果取消注释）
# tom.__dict__ 中没有 weight（因为没被实例覆盖）
# 会报 KeyError
# print(8, tom.__dict__['weight'])


# ===== 核心原理总结 =====

# 1. 属性查找顺序：
# obj.__dict__ → class.__dict__ → 父类（MRO）

# 2. 赋值规则：
# obj.x = value → 一定写入 obj.__dict__

# 3. += 的本质：
# obj.x += 10
# ≈ obj.x = obj.x + 10
# → 触发“先查再写”，从而可能创建实例属性

# 4. 类属性 vs 实例属性：
# - 类属性：所有实例共享（除非被实例覆盖）
# - 实例属性：只属于自己

# 5. __dict__ 只存“实例自己拥有的属性”
