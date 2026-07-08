# # 常见的hash函数用法

# print(hash('hello'))  # 字符串的hash值
# print(hash(123))  # 整数的hash值
# print(hash(1.23))  # 浮点数的hash值
# print(hash((1, 2, 3)))  # 元组的hash值


# # 在类中使用hash函数
# class Person:
#     pass


# t1 = Person()
# t2 = Person()

# print(hash(Person))  # 类的hash值
# print(hash(Person()))  # 实例的hash值
# print(hash(t1))  # 实例的hash值
# print(hash(t2))  # 实例的hash值

# class A:
#     def __init__(self, name):
#         self.name = name

#     def __hash__(self):
#         return 1
    
#     def __repr__(self):
#         return self.name
    
# a1 = A('tom')
# a2 = A('tom')


# print(a1, a2, hash(a1), hash(a2))  # 输出实例的hash值
# print([a1, a2])
# print((a1, a2))
# print({a1, a2})
# print({a1, a1}) # 集合中只会保留一个实例，因为它们的hash值相同


# # 元组
# t1 = ('tom',)
# t2 = ('tom',)
# print(t1 is t2)
# print(t1 == t2)
# print({t1, t2})

''' 
上例中， A的实例放在set中，它们hash值是相同的，为什么不能去重？
hash值相同就会去重吗？


哈希冲突怎么解决去重问题
'''


# class A:
#     def __init__(self, name):
#         self.name = name

#     def __hash__(self):
#         return self.name.__hash__()
    
#     def __repr__(self):
#         return self.name
    
#     # def __eq__(self, other):
#     #     return self.name == other.name
    
# a1 = A('tom')
# a2 = A('tom')
# print(a1, a2, hash(a1), hash(a2))  # 输出实例的hash值
# print(a1 == a2)  # 输出True，因为它们的name属性相同
# print(a1 is a2)  # 输出False，因为它们是不同的实例
# print({a1, a2}) # 去重了吗？
# print({A('jerry'), A('jerry')}) # 去重了吗？


''' 
## 思考 ：
1. List 类实例为什么不可 hash？
2. Functools. Lru_cache 使用到的 functools._HashedSeq 类继承自 list，为什么可 hash？
'''
# print(hash([1, 2, 3]))  # 报错，list不可hash


# import functools 



# 设计二维坐标类 Point，使其成为可 hash 类型，并比较 2 个坐标的实例是否相等？

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

t1 = Point(1, 2)
t2 = Point(1, 2)
print(t1 == t2)  # 输出 True
print(t1 is t2)  # 输出 False
print({t1, t2})  # 输出 {Point(1, 2)}