class A: pass

print(bool(A))
t1 = A()
print(bool(t1))
print('='* 30)


class B:
    def __bool__(self):
        # return True
        print('__bool__ ---')
        return bool(len(self))   # len(self) => self.__len__()
    def __len__(self):  #容器使用
        print('__len__ +++')
        return 1

# print(bool(B))
# # print(bool(B()))
t = B()
print(bool(t))
print(len(t))

# class C:
#     def __len__(self):
#         return 0

# print(bool(C))