N = int(input())
A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]
A_sum = sum(A)

#最初の勇者から順に(i番目の勇者に関して)i番目の街を優先して狩るように仮定する
for i in range(N):
    while (B[i] != 0 and A[i+1] != 0):
        #A[i] == 0 ならA[i+1]の敵を狩ることができる
        if A[i] == 0:
            if B[i] <= A[i+1]:
                A[i+1] -= B[i]
                B[i] = 0
            else:
                B[i] -= A[i+1]
                A[i+1] = 0
        else:
            if B[i] <= A[i]:
                A[i] -= B[i]
                B[i] = 0
            else:
                B[i] -= A[i]
                A[i] = 0

A_after_sum = sum(A)

#敵の数Aが減った分が勇者が狩った敵の数となる
print(A_sum- A_after_sum)
