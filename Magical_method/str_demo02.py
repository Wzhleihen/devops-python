import json

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'(Poiint {self.x}, {self.y})'

    def __repr__(self): #用list，tulpe等
        return f'<P{self.x}, {self.y} >'

    def __bytes__(self):
        # return f'(P {self.x}, {self.y}  >>>)'.encode()
        # return str(self).encode()
        # return repr(self).encode()
        return json.dumps({
            "x": self.x,
            "y": self.y
        }).encode()

t = Point(4, 5)
print(type(t), t)
print(str(t))
print(f'{t}')
print([t, str(t)])  # __str__默认只能间接构建 ，解决这个问题要使用 __repr__

print(bytes(t))


# # 案例使用
from pathlib import Path
p1 = str(Path('/etc/sysconfig'))

print(p1)
print(str(p1))
print([p1])