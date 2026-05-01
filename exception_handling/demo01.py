import sys

class MyException(Exception):
    pass

def foo():
    try:
        # i/o
        # 0a =  100
        print('test')
        print('~' * 30)
        print('~' * 30)
        # sys.exit(0)   # 定义退出码，，让程序立刻中断
        # raise NotImplementedError  #主动中断程序执行，并明确告诉调用方：这个功能“定义了但尚未实现”，必须由子类或后续代码补充实现。
        # raise MyException('异常原因')
        # raise IndexError('test error')  # 常用于抛出异常
        print('~' * 30)
        print('~' * 30)
    except ArithmeticError:
        print('Arith')
    except Exception as e:
        print(type(e), e)
    print('=' * 30)

foo()
print('*' * 30)