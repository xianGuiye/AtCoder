from operator import mul
from functools import reduce

#組み合わせ総数nCrを求める
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1),True)
    under = reduce(mul, range(1,r + 1),True)
    return over // under

N,K = [int(x) for x in input().split()]

#(k-1)Ci * (N-K+1)C(i+1) → 　i個の青いボールとN-i個の赤いボールがあるときの操作の回数
for i in range(K):
    if N-K-i >= 0:
        print((cmb(K-1,i)*cmb(N-K+1,i+1))%(10**9+7))
    else:
        print(0)
