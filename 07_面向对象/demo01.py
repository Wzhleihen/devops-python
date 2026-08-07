# 复习魔术方法
# 定义一个斐波那契数列的类，方便调用，计算第 n 项。

# 增加迭代数列的方法、返回数列长度、支持索引查找数列项的方法。


class Fib1:
    def __init__(self):
        self.items = [0, 1, 1] # 初始化数列 ，第一项为 0，第二项为 1，第三项为 1

    
    # def __repr__(self):
    #     return f"Fib(n={self.n})"
    
    def __call__(self, index):
        if index < 0:
            raise IndexError('Not negative index')
        if index < len(self.items):  # 用Fib()(3)思考边界
            return self.items[index]
        
        for i in range(len(self.items), index + 1):
            self.items.append(self.items[i - 1] + self.items[i - 2])
        return self.items[index]

# f = Fib1()
# print(f(3))
# print(f(10))
# -----------------------------------------

class Fib2:
    def __init__(self):
        self.items = [0, 1, 1]
    
    def __call__(self, index):
        return self[index]
    
        
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)

    
    def __str__(self):
        return str(self.items)
    
    __repr__ = __str__
    
    
    def __getitem__(self, index):
        if index < 0:
            raise IndexError('Not negative index')

        for i in range(len(self.items), index + 1):
            self.items.append(self.items[i - 1] + self.items[i - 2])
        return self.items[index]

f2 = Fib2()
print(f2(6), f2(10), f2(15))
print(f2[3], f2[4], f2[5])

for x in enumerate(f2):
    print(x)
    
    

# 实现一个 LRUCache 支持 cache[key]
