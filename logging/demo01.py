import  logging  # 模块加载，并且执行模块，模块的顶层代码会执行
import sys



# 用于测试环境调式用
# logging.warning('test info ~~~')  # message

#常见用于log记录器logger

# 三种方式都能创建 根日志记录器
# root = logging.root
# root = logging.Logger.root
# root = logging.getLogger()  # 常用， root不用去创建，从全局去获取，只用去创建自定义的根，根只有一个


# log1 = logging.Logger('m1')
# print(log1, type(log1))
#
# log2 = logging.Logger('m1')
# print(log2, type(log2))
#
# # 对log1和log2进行实例化，生成对象不一样
# print(log1 == log2)
# print(log1 is log2)

# 常用getLoger来获取一个log对象，保证拿到同样名字实例
# log3 = logging.getLogger('m1')  # 通过 字典m1 ==> logger，  在内部实现必须使用字典来实现
# print(log3, type(log3))
# print(log3.parent, log3.parent is root)

# 一般情况下，我们都会使用getLogger，通过一个名字获取对应的log，没就创建，有就直接返回
# log4 = logging.getLogger('m1')
# print(log4, type(log4))
#
# # log3和log4 获取同一个生成对象，地址一样
# print(log3 == log4)
# print(log3 is log4)

# log = logging.getLogger('m1')
# print(log.level)
# # log.setLevel(40)
# print(log.level, log.getEffectiveLevel())
# # 当小于有效级别log是不输出的
# log.warning('log test info ~~~') # msg >= log Effective Level(有效level)

# Effective Level怎么得到？ 找最近的父类定义 getEffectiveLevel

# log1 = logging.getLogger('m1.m2')
# print(log1.level, log1.getEffectiveLevel())

FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"
# pattern = "[(?<date>.*)]\t(P<message>)\w+>)"
logging.basicConfig(level=logging.INFO,  format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S",
                    stream=sys.stdout
                    )



# 一般情况下，建议大家设计为 WARNING,一般调式采用info级别

root = logging.getLogger()

h1 = logging.StreamHandler()
root.addHandler(h1)  # 默认情况只会输出message

f1 = logging.Formatter('** %(message)s **')
h1.setFormatter(f1)  # 引用 Formatter

print('='  * 30)
print(root.handlers)
logging.info('test')  # msg level >= root EL; ==> all Handler

# 输出靠 Handler
#  格式靠 Formatter
# [<StreamHandler <stderr> (NOTSET)>] 默认在控制，输出标准错误