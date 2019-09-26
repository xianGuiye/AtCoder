N = int(input())
A = [int(x) for x in input().split()]
Base1 = 0
Base2 = 0
a = []


for x in range(N):
    if x % 2 == 0:
        Base1 += A[x]
        Base2 -= A[x]
    else:
        Base1 -= A[x]
        Base2 += A[x]

for i in range(N):
    if i % 2 == 0:
        tmp1 = Base1
        if i >= 2:
            a.append(a[i-2]-A[i-2]*2+A[i-1]*2)
            print(a[i])
        else:
            a.append(Base1)
            print(a[i])
    if i % 2 == 1:
        tmp2 = Base2
        if i >= 2:
            a.append(a[i-2]-A[i-2]*2+A[i-1]*2)
            print(a[i])
        else:
            a.append(Base2+A[i-1]*2)
            print(a[i])
        
