'''
内建反射函数：
getattr 获取
setattr 修改
hasattr 判断
'''



class Point:
    # z = 200
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def showme(self):
        return f'< {self.x} : {self.y}>'

t = Point(1,2)
# print(t.x , t.y)
# print(t.showme)
# print(t.showme())

# getattr 用于获取对象属性
print(getattr(t, 'x'))
print(getattr(t, 'y'))
print(getattr(t, 'z', 3000))  # 等价于 t.z
# AttributeError: 'Point' object has no attribute 'z'
setattr(t, 'x', 40)
print(t.x)

# 在类外面添加一个属性
# setattr(Point, 'showme',  # 字符串
#         lambda self: f'< {self.x} : {self.y}> ____'
# )
# 等价于下面  这个showme是标识符
Point.showme = lambda self: f'< {self.x} : {self.y}> ____'
print(t.showme())
print(getattr(t, 'showme')())
# hasattr 判断对象属性是否存在， 返回布尔值
print(hasattr(Point, 'z'))
print(hasattr(t, 'z'))
