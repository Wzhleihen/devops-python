import  argparse
from pathlib import Path

parser = argparse.ArgumentParser('mkdir', description='创建目录')

parser.add_argument('dir_name', help='要创建的目录名称')
parser.add_argument('-p', '--parents', action='store_true', help='创建多级目录')

args = parser.parse_args()

print(args)

if args.parents:
    Path(args.dir_name).mkdir(parents=True, exist_ok=True)
else:
    Path(args.dir_name).mkdir(exist_ok=True)
