N = int(input())
A = [int(x) for x in input().split()]
count = 0
ab_sum = 0
min = 1000000000

for i in range(N):
    ab = 0

    if A[i] >= 0:
        ab_sum += A[i]
        ab = A[i]
    else:
        count += 1
        ab_sum -= A[i]
        ab = -A[i]
    if ab < min:
        min = ab

if(count % 2 == 0):
    print(ab_sum)
else:
    print(ab_sum-2*min)
    
