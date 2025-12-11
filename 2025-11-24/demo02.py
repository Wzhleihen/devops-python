def nxn(n):
    if n == 1:
        return 1
    else:
        return n + nxn(n - 1)


print(nxn(5))
# 输出结果为 15
