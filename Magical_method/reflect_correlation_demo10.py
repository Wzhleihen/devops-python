'''
 __getattr__ 当属性找不到时调用，返回值为该属性的值
 __setattr__ 当使用 self.x = x 或者setattr(self, 'x', x)调用，解决方法，1调用object同名，2，使用自己的实例字典
 __delattr__  del 实例.xxx 都会触发该魔术方法
 __getarrtibute__ 属性访问第一站, 一般建议不要定义它，如果定义了，为了正确访问属性，建议调用object的同名方法
'''

# __getattr__
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __getattr__(self, item):
#         print('getattr ~~~~~~~', item, type(item))
#         print(item)
#         return item
#
# t = Point(4,5)
# print(t.x)
# print(t.y)
# print(t.z)  # 这个z是怎么找到的？


# __setattr__
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __setattr__(self, key, value):
#         print('setattr ~~~~~~~', key, value)
#         # super().__setattr__(key, value)  # 父类也是帮我们加入字典中
#         # setattr(self, key, value)
#         # self.x = 4
#         # 为什么会造成递归？
#         """
#         因为每次 setattr 都会调用 __setattr__，
#         而 __setattr__ 中又调用了 setattr
#         """
#         self.__dict__[key] = value
#
#     def __getattr__(self, item):
#         print('getattr ~~~~~~~', item, type(item))
#         print(item)
#         return item
#
# t = Point(4,5)
# print(t.x)


# __delattr__
#
# class Point:
#     z = 200
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __delattr__(self, item):
#         print(f'delattr {item}~~~~~~~', item, type(item))
#         # print(item)
#         # 使用delattr删除，一样会触发递归
#         # delattr(self, item)
#         # del self.__dict__[item]
#         # super().__delattr__(item)
#     # 只用通过实例删除属性，都归 delattr 管
#     # 当要删除属性时，会调用 __delattr__ ，在这里面可以做限制禁止删除非必要属性
#
# t = Point(4,5)
# print(t.x, t.y, t.z)
# print(Point.__dict__.keys())
# # del t.x
# del Point.z
# print(Point.__dict__.keys())


# __getattribute__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        # pass
        # print('getattribute ~~~~~~~', item, type(item))
        print(item)
        # return super().__getattribute__(item)
        return object.__getattribute__(self, item)
        # return item

t = Point(4,5)
print(t.x)
print(t.__dict__)


