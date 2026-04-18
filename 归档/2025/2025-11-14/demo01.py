# # 有错吗？
# def foo():
#     global x
#     x += 1
#     print(x)


# foo()


# 有错吗？
def foo():
    global x
    x = 10
    x += 1
    print(x)


foo()
print(x)  # 可以吗
