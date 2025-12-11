"""
      1
    2 1
  3 2 1
4 3 2 1
"""

# print(len(str(j)) * ' ' if j > i else j , end=' ')
# def multiplication_table(n):
for i in range(1, 10):
    for j in range(i, 0, -1):
        print(f"{j}*{i}={i*j}", end=" ")
    print()

print('-' * 50)
n = 9
width = len(f"{n}*{n}={n*n}")  # 最大表达式宽度

for i in range(1, n+1):
    line = ""
    for j in range(i, 0, -1):
        expr = f"{j}*{i}={i*j}"
        line += expr.rjust(width) + " "  # 固定宽度+空格
    print(line.center(n*(width+1)))      # 居中对齐整个行
