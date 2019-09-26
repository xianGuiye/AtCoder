N,K = [int(x) for x in input().split()]
S = str(input())
replace = list(S)

for i in range(N):
    if i == K - 1:
       replace[i] = replace[i].lower()

answer = ''.join(replace)

print(answer)

