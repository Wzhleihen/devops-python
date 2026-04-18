# 测试代码


class Person:
    age = 3
    height = 175

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


tom = Person("Tom")
jerry = Person("Jerry", 20)

Person.age = 30
print(1, Person.age, tom.age, jerry.age)  # 输出什么结果

print(2, Person.height, tom.height, jerry.height)  # 输出什么结果？
jerry.height = 180
print(3, Person.height, tom.height, jerry.height)  # 输出什么结果？

tom.height += 10
print(4, Person.height, tom.height, jerry.height)  # 输出什么结果？

Person.height += 15
print(5, Person.height, tom.height, jerry.height)  # 输出什么结果？


Person.weight = 50
print(6, Person.weight, tom.weight, jerry.weight)  # 输出什么结果？

print(7, tom.__dict__["height"])  # 可以查看吗？
# print(8, tom.__dict__['weight'])  # 可以查看吗？
