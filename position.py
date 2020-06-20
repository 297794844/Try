def fun(a, *b):
    print(a)
    print(*b)
    print(b)
    for i in range(len(b)):
        for j in b[i]:
            print(j)
def havefun(j, **k):
    print(j)
    print(k)
    for o, p in k.items():
        print(o, p)
if __name__ == "__main__":
    a = 1
    d = 2, 3, 4
    c = {'a':1, 'b':2}
    #fun(a, d)
    havefun(a, **c)
