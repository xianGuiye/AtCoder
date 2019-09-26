N = int(input())
V = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
count = 0

#宝石の価値 > 支払うコストのときだけ宝石を手に入れればよい
for x in range(N):
    if V[x] >= C[x]:
        count += V[x] - C[x]

print(count)
