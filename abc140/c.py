N = int(input())
B = [int(x) for x in input().split()]
count = 0

#A[i] = min(B[i],B[i+1])をとるときB[i]の各要素は最大となる
for i in range(N-2):
    count += min(B[i],B[i+1])
print(count+B[0]+B[N-2])
