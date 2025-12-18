import pickle

filename = 'src.bin'

# 序列化后，看到什么
a = 99
b = 'c'
c = list('abc')
d = dict(a=1,b='1',c=list('abc'))


# with open(filename, 'wb') as f:
#     pickle.dump(a, f)
#     pickle.dump(b, f)
#     pickle.dump(c, f)
#     pickle.dump(d, f)

with open(filename, 'rb') as f:
    for i in range(4):
        x = pickle.load(f)
        print(i,type(x), x)