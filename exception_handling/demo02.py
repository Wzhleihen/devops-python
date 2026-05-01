import logging

FORMAT = '%(asctime)-15s %(message)s'

logging.basicConfig(format=FORMAT, level=logging.INFO)

def foo():
    try:
        print('+' *  30)
        # raise IndexError('我抛出的异常描述')
        # raise 100  #ininstance(100, BaseException)
        open('test1.txt')
    # except Exception as e:
    except FileNotFoundError as e:
        print('other~~', e, type(e), str(e), e.args)
        logging.error(str(e))
    print('=' * 30)

foo()
print('*' * 30)