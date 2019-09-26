r,D,x = [int(x) for x in input().split()]
y = []
y.append(x)
tmp = 0
tmp2 = 0
for i in range(10):
    tmp = y.pop(0)
    tmp2 = tmp*r-D
    print(tmp2)
    y.append(tmp2)


