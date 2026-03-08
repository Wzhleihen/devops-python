#ls -a /etc
#ls -ar-h /etc
# ls -la -h /etc
# ls -lahls --all -h -1
# 1s /etc -la -h


# 引出问题 ： 人为使用py脚本，解决这些参数非常困难，使用 argparse 模块，可以轻松解决

# argparse模块  简介： 专门用于解析命令行参数的模块

import argparse


parser = argparse.ArgumentParser('ls', add_help= True, description='show file list')

# parser.add_argument('path1', nargs='?',help='path to list')
parser.add_argument('path1', nargs='+',help='path to list')
''' 
nargs 表示参数可有可无 , 默认显示为 []
        ? 表示参数可有可无
        + 表示至少有一个参数
        * 表示参数可以有多个
        
'''


parser.print_help()  # usage 出现参数 列表

print('-'*30)
args = parser.parse_args([])
print(args)
# x = parser.parse_args(['-h'])  # 传入参数，解析参数，当没有参数时，会输出 usage
# 当 parse_args() 传入参数时，会返回一个 Namespace 对象，当没有参数时，会输出 usage
# 程序执行流程
'''
parser.print_help()
↓
parser.parse_args(['-h'])
↓
触发 -h
↓
打印 help
↓
sys.exit(0)
↓
程序结束
'''

# print(type(x), x)

''' 
usage: ls [-h]
ls: error: unrecognized arguments: /etc
说明出现异常，只能接受 -h参数
'''