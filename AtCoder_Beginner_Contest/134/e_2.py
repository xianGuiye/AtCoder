N = int(input())
A = [int(input()) for x in range(N)]
count = 0
tmp = A[0]
for i in range(N-1):
    if A[i] >= A[i+1]:
        count += 1
print(count)

