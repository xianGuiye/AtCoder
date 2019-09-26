N,M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
 
A.sort(reverse=True)
for i in range(M):
    A[0] = int(A[0]/2)
    for j in range(1,N-1):
        if A[j] >= A[0] and A[0] >= A[j+1]:
            A.insert(j+1,A[0])
            A.pop(0)
print(sum(A))
