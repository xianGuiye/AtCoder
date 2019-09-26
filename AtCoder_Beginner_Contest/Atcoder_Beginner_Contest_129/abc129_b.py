N = int(input())
W = []
W = list(map(int,input().split()))
S = sum(W)
temp = sum(W)/2
count = 0
for i in range(N):
    count += W[i]
    diff = S/2 - count
    if temp >= abs(diff):
        temp = abs(diff)
print(int(temp*2))
