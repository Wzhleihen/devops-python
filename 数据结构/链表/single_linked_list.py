''' 
用面向对象实现LinkedList链表
单向链表实现append、iternodes方法

解决思路：
1. 定义一个Node类，包含value和next属性 ，用于存储链表的节点
2. 定义一个SingleLinkedList类，包含head属性，用于存储链表的头节点
3. 实现append方法，向链表尾部添加节点
4. 实现iternodes方法，遍历链表，返回每个节点的值
'''

# 定义一个Node类，包含value和next属性
class Node:
    def __init__(self, value, next: 'Node' = None):
        self.value = value  # 存储节点的值
        self.next = next   # 索引下一个节点
    
    def __repr__(self):  # 定义__repr__方法，返回节点的值，方便调试，在py3.10+ 自动调用，可以不加
        return str(self.value) 

# 定义一个SingleLinkedList类，包含head属性，用于存储链表的头节点
class SingleLinkedList:
    def __init__(self):  # 初始化头部和尾部为None
        self.head = None
        self.tail = None  # 需要吗？
    
    def append(self, item):
        node = Node(item)  # 创建一个节点
        if self.head is None:  # 如果链表为空，头部和尾部都指向新节点
            self.head = node
        else:
            self.tail.next = node
            
        self.tail = node
        
        return self  # 返回self，可以链式调用
    
    # 实现iternodes方法，遍历链表，返回每个节点的值
    def iternodes(self):
        current = self.head  # 获取当前节点
        while current:
            yield current  # 偏函数 yield ，返回当前节点，暂停函数执行，等待下一次调用
            current = current.next  # 移动到下一个节点


ll = SingleLinkedList()
ll.append(1).append(4).append(3).append(2)

for node in ll.iternodes():
    print(node.value)