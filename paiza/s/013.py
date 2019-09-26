N = int(input())
c_f,c_b = [int(x) for x in input().split()]
a = list(input())

order = [N]

if c_f >= c_b:
    tmp = 1
    for i in reversed(range(N-1)):
        if a[i] == "d":
            order.append(i+1)
        else:
            order.insert(tmp,i+1)
            tmp = N - i
else:
    order.append(1)
    tmp = 2
    for i in range(1,N-1):
        if a[i] == "s":
            order.append(i+1)
        else:
            order.insert(tmp,i+1)
            tmp = i + 2

if N % 2 == 0:
    order.append(1)
order.append(N)

print(order)
