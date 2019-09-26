import time
start = time.time()
N = int(input())
A = [int(input()) for x in range(N)]
count = 0
i = 0
while A != []:
    count += 1
    base = A[0]
    A.pop(0)
    i = 0
    while i < len(A):
        if A[i] > base:
            base = A[i]
            A.pop(i)
        else:
            i += 1
el_time = time().time() - start
print(el_time)

