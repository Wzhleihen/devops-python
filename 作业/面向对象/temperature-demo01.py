"""
实现华氏温度和摄氏温度的转换。
℃ = 5 x (℉ - 32) / 9
℉ = 9 x ℃ / 5 + 32

完成以上转换后,增加与开氏温度的转换,K = ℃ + 273.15

"""

# staticmethod 与 classmethod 的区别
# staticmethod 是一个静态方法，它不接收隐式的第一个参数，可以像调用普通函数一样调用它。
# classmethod 是一个类方法，它接收隐式的第一个参数，即该类本身。可以通过类名直接调用它，也可以通过类的实例调用它。


class Temperature:  # 就是一个工具类，提供各种工具方法，来实现温度的转换
    def __init__(self, t, unit="c"):
        self._c = None
        self._f = None
        self._k = None
        if unit == "f":
            self._f = t
            self._c = self.f2c(t)
        elif unit == "k":
            self._k = t
            self._c = self.k2c(t)
        else:
            self._c = t

    @property
    def f(self):
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f

    @property
    def k(self):
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k

    @property
    def c(self):
        return self._c

    @classmethod
    def c2f(cls, c):
        return 9 * c / 5 + 32

    @classmethod
    def f2c(cls, f):
        return 5 * (f - 32) / 9

    @classmethod
    def c2k(cls, c):
        return c + 273.15

    @classmethod
    def k2c(cls, k):
        return k - 273.15

    @classmethod
    def f2k(cls, f):
        return cls.c2k(cls.f2c(f))

    @classmethod
    def k2f(cls, k):
        return cls.c2f(cls.k2c(k))


# 测试
print(Temperature.c2f(20))
c = Temperature(30)
print(c.f, c.k, c.c)
