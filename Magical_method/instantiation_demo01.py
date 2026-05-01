class A:
    # __new__ 1 实例化， 2 元类构造类的过程
    def __new__(cls, *args, **kwargs):   #构造实例，从无到有
        print(cls)
        print(args)
        print(kwargs)
        # return cls(*args, **kwargs)  #会出现递归
        #return  100 # 如果返回的不是A的实例，那么实例化得到的就不是A的实例   # <class 'int'> 100
        # return object.__new__(cls)  # 类似调用（静态方法） static method
        return super().__new__(cls) #沿 MRO（方法解析顺序）向上查找“下一个类”的 __new__

    def __init__(self, x,y):
        print('init ~~~')
        self.x = x
        self.y = y

t = A(4, 5)  # A.__new__(A) => object
print(type(t), t)




