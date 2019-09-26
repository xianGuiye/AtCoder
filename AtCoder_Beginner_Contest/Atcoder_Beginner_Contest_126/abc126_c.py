import math
N,K = [int(x) for x in input().split()]
p = 0
for x in range(N):
    k = K/(x+1)
    if x < K:
        k_log = math.ceil(math.log2(k))
    else:
        k_log = 0
    p += 1/N/pow(2,k_log)

print(p)
