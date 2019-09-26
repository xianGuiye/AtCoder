from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1),True)
    under = reduce(mul, range(1,r + 1),True)
    return over // under

N,K = [int(x) for x in input().split()]


for i in range(int(N**(1/K))):
    count += N
    count += cmb(N,2)*K
    count += cmb(N,3)*K
