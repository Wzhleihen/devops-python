print('-' * 30)
print('=' * 30)


class Produto():
    def __init__(self, x, y):
        self.x =  x
        self.y = y

    def __repr__(self):
        return f'Produto({self.x}, {self.y})'

_B = 1
_C = 2
__my = 3

if __name__ == '__main__':
    P = Produto(4,5)
    print(P)

print('~' * 30)