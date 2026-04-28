import logging

FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"
# pattern = "[(?<date>.*)]\t(P<message>)\w+>)"
logging.basicConfig(level=logging.INFO,  format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

logging.info('test')

# 一般情况下，建议大家设计为 WARNING,一般调式采用info级别

root = logging.getLogger()
print('='  * 30)
print(root.handlers)