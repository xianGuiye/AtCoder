def cmb(n,r):
    r = min(n-r,r)
    if r == 0: 
        return 1
    over = reduce(mul, range(n, n - r, -1),True)
    under = reduce(mul, range(1,r + 1),True)
    return over // under


