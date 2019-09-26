N = int(input())
A = [int(x) for x in input().split()]
seki = 1
Max = max(A)


for x in range(2,int(Max**0.5)+1):
    count = 0

    for y in range(N):
        if A[y] % x != 0:
            count += 1
        if count >= 2:
            break
    else:
        seki = x

for i in range(N):
    count = 0
    if A[i] < 1000000000**0.5+1:
        break
    for j in range(N):
        if A[i] % A[j] != 0:
            count += 1
        if count >= 2:
            break
    else:
        seki = A[i]

print(seki)
