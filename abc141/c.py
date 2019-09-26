N,K,Q = [int(x) for x in input().split()]
A = [int(input()) for x in range(Q)]
p = [K - Q for x in range(N)]

for item in A:
    p[item-1] += 1

for item in p:
    if 0 < item:
        print("Yes")
    else:
        print("No")

