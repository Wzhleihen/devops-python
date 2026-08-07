'''
双向链表实现append、pop、insert、remove、iternodes方法
'''

# 定义一个Node类，包含value和next属性
class Node:
    def __init__(self, value, next: 'Node' = None, prev: 'Node' = None):
        self.item = value  # 存储节点的值
        self.next = next   # 索引下一个节点
        self.prev = prev   # 索引上一个节点

    def __repr__(self):  
        return f"{self.prev.item if self.prev else None} < == {self.item} ==> {self.next.item if self.next else None}"

    # 当需要打印节点时，返回节点的值，强制转换成字符串
    def __str__(self):
        return str(self.item)
    
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None  # 初始化头节点为None
        self.tail = None  # 初始化尾节点为None
        self._size = 0     # 初始化链表长度为0, 容器化
        
        self.size = property(lambda self: self._size)

    # 实现容器化
    def __len__(self):
        return self._size
    
    def append(self, item: Node):
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail  # 指向原来的尾巴
        self.tail = node  # 更新尾巴
        
        self._size += 1
        
        return self

    def pop(self):
        """ 尾部弹出 """
        if not self.tail:
            raise Exception('List is empty')
        
        node = self.tail  # 获取当前尾部节点
        self.tail = node.prev  # 更新尾部节点
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return node

    def insert(self, index, item):
        """ 在指定位置插入节点 """
        # 完善正负索引
        if index <= 0:
            self.append(item)
            return 
        if index > -len(self):
            index = 0
        current = self[index]  # 获取指定索引的节点
        
        node = Node(item)
        prev = current.prev
        
        if index == 0:  # 插入到头部
            self.head = node
        else:  # 中间插入
            prev.next = node  # 原来的前一个节点指向新节点
            node.prev = prev  # 新节点指向前一个节点
        node.next = current  # 新节点指向当前节点
        current.prev = node  # 当前节点指向前一个节点
        
        self._size += 1
        return self
   

    def remove(self, index):
        """ 删除指定位置的节点 

        Args:
            index (_type_): _description_
        """
        if self.head is None:
            raise Exception('List is empty')

        current = self[index]  # 获取指定索引的节点
        prev = current.prev
        next = current.next
        
        if self.head == self.tail:  # 唯一节点
            self.head = None
            self.tail = None
        elif prev is None:  # 删除头节点， 其他写法 current is self.head
            self.head = next
            next.prev = None
        elif next is None: # 删除尾节点，其他写法 current is self.tail
            self.tail = prev
            prev.next = None
        else:  # 删除中间节点
            prev.next = next
            next.prev = prev
        
        del current  # 删除节点
        self._size -= 1
        

    def iternodes(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev
    
    # 实现迭代器协议
    def __iter__(self):
        yield from self.iternodes()
        # return self.iternodes()
    
    __iter__ = iternodes  # 等价于 self.__iter__() 
    
    
    # 实现反向
    def __reversed__(self):
        return self.iternodes(reverse=True)
    
    # 支持正副索引
    def __getitem__(self, index):
        if index >= len(self)  or index < -len(self): # 正负向超界
            raise IndexError(f'Index out of range{index}')

        reverse = False if index >= 0 else True
        start = 0 if index >= 0 else 1
        for i, node in enumerate(self.iternodes(reverse), start):
            if abs(index) == i:
                return node
                
    # 支持索引修改
    def __setitem__(self, index, value):
        self[index].item = value

if __name__ == '__main__':
    # 原始实例数据
    dll = DoubleLinkedList()
    dll.append(1).append(2).append(3).append(4)
    for i in dll.iternodes():
        print(i)
        
    # # 测试尾部弹出
    # print('-' * 30)
    # dll.pop()
    # dll.pop()
    # for i in dll.iternodes():
    #     print(i)
    
    # # 指定插入
    # print('-' * 30)
    # dll.insert(0, 'start')
    # dll.insert(1, 3)
    # dll.insert(3, 'end')
    # for i in dll.iternodes():
    #     print(i)
        
    # # 删除指定位置的节点
    # print('= ' * 30)
    # dll.remove(1)
    # for i in dll.iternodes():
    #     print(i)
        
    # # 实现翻转
    # print('实现翻转', '-' * 30)
    # for i in reversed(dll):
    #     print(i)
    
    # 支持索引
    print('支持索引', '-' * 30)
    for i in range(4):
        print(dll[i])
    print('支持负索引', '-' * 30)
    for i in range(1, 5):
        print(dll[-i])
    
    # 支持索引修改
    print('支持索引修改', '-' * 30)
    dll[0] = 'start'
    for i in dll.iternodes():
        print(i)