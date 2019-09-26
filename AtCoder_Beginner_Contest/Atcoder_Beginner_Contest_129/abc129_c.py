import math
N,M = [int(x) for x in input().split()]
a = [int(input()) for j in range(M)]

def combinations_count(n, r):
        return math.factorial(n)//(math.factorial(n - r) * math.factorial(r))

def keisan(n,r):
    count = 0
    while n >= r:

        count += combinations_count(n,r)
        n -= 1
        r += 1

    return count
result = 1

for i in range(M):
    if a[i] - a[i-1] == 1:
        result = 0
        break
    elif i == 0:
        result *= keisan(a[i]-1,0)
    else:
        result *= keisan(a[i]-a[i-1]-2,0)

else:
    result *= keisan(N - a[M-1]-1,0)

print(int(result)%1000000007)

