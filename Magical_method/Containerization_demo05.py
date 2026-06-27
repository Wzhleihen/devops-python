# class Student:
#     def __len__(self):
#         return 100
#
#
# print(len(Student()))

# # 一般用在字典中
# class A(dict):
#     # 全部基础父类构造器
#     def __missing__(self, key):
#         print(key)
#
# t1 = A(a=1, b='abc')
# print(t1, type(t1),isinstance(t1, dict) )
#
# t1.update()


# 应用
class Cart:
    def __init__(self):
        self.__items = []

    def __len__(self):
        return len(self.__items)


    # 在电商项目里面，加东西进去，习惯使用 item
    def add_item(self, item):
        self.__items.append(item)
        return self  # 返回自身, 实现链式调用，
        # return  self + item

    # 定义查看实例的方法
    def __repr__(self):
        return str(self.__items)

    # 定义迭代器
    def __iter__(self):
        # return  iter(self.__items)
        yield  from self.__items  # 生成器函数

    # 那如果我把我的购物车理解成为一个线性数据结构，我刚说了购物车里面的数据，一般看到最上一个是最新加入的数据，那么我如何实现呢？
    def __getitem__(self, index):
        print(index, '+++')
        return self.__items[index]

    # 实现通过索引修改
    def __setitem__(self, index, value):
        self.__items[index] = value

    # 实现 cart + 100 + 200
    def __add__(self, other):
        # self.__items.append(other)
        # return self
        return self.add_item(other)


cart = Cart()
cart.add_item('item1')
cart.add_item('item2')
cart.add_item(3)

# 链式调用
cart.add_item(100).add_item(3000)
print(cart + 11 + 200)


# print(cart.__items)
print(len(cart))
print(cart)
print(cart[0])

print('-' * 30)

print(3 in cart)  # 默认使用 __contains__ ，未定义可以使用 __iter__
print(2 in cart)

print('=' * 30)
for item in cart:
    print(item)






