print(sorted(["a", "Ab", "2", "Abc"]))  # 怎么按照小写排序？


def fn(x: str):
    return str.lower(x)


# "abc".lower()  str.lower("abc")  # 这两种调用方式都可以
# fn("abc") === str.lower("abc")
# 高阶函数：函数的参数是函数，或者函数的返回值是函数

print(sorted(["a", "Ab", "2", "Abc"], key=lambda x: x.lower()))


print(sorted(["a", "Ab", "2", "Abc"], key=str.lower))


def fn(x):
    # return int(str(x), base=16)
    if isinstance(x, str):
        return int(x, base=16)
    else:
        return x


# print(sorted(["1", 100, "a", "20", 7], key=fn))
# print(sorted(["1", 100, "a", "20", 7], key=lambda x: int(str(x), base=16)))

print(
    sorted(
        ["1", 100, "a", "20", 7],
        key=lambda x: int(x, base=16) if isinstance(x, str) else int(x),
    )
)
