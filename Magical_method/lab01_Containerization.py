class Fib:
    pass


f = Fib(5)
print(f)  # 打印五个斐波那契数
print(f[10]) # 列出10个斐波那契数
for x in f:  # 迭代
    print(x)
# 长度
print(len(f))

print(f[11]) # 是否需要重头算