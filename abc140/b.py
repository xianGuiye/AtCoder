N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
count = sum(B)

#すべての料理は必ず一度食べるから満足度sum(B)は必ず獲得する.追加点Cがあるかを検証する
for i in range(N-1):
    if A[i] == A[i+1] - 1:
        count += C[A[i]-1]

print(count)
