

# 2 > 1 bool gt(int x, int y)
# 'a' > 'b' class str; bool gt(string x,string y)
#
# class A:
#     def __init__(self, name):
#         self.name = name
#     # >
#     def __gt__(self, other):
#         print(self, other)
#         return  True
#
#     def __str__(self):
#         print('-' * 30)
#         return f"<A {self.name}>"
#
#
# t1 =  A('t1')
# t2 = A('t2')
#
#
# print(t1 > t2)



class Student:
    def __init__(self, name, age = 20):
        self.name = name
        self.age = age

    # 刚好是一对啊一对这一对里面实现任意一个方法都可以解决大于和小于的问题
    def __gt__(self, other):  # < >  __le__
        print(self, other)
        return  self.age > other.age

    def __ge__(self, other):  # __le__ >= <=
        return self.age >= other.age

    def __eq__(self, other):   #  __ne__ == 或者  !=
        return self.name == other.name and self.age == other.age

    def __str__(self):
        print('-' * 30)
        return f"<Student {self.name}>"


t1 =  Student('tom',30)
t2 = Student('jerry')

print(t1 > t2)
print(t1 < t2)

print('=' * 30)
print(t2 >= t1)  # t2.__ge__(t1)

print('*' * 30)
t3 = Student('tom', 30)
print(t1 == t3)

print(t1 is t3) # 判断类型


