N,K = [int(x) for x in input().split()]
S = input()
list = []
count = 1
for x in range(N):
    if x >= N - 1:
        list.append(count)
        break
    if S[x] == S[x+1]:
        count += 1
    else:
        list.append(count)
        count = 1
l = len(list)
max = 0
if S[0] == "1":
    start = 0
else:
    start = 1
    max = list[0] + list[1]

for x in range(start,l,2):
    number = 0
    for y in range(2*K+1): 
        if x + y >= l:
            break
        else:
            number += list[x + y]
    if number > max:
        max = number
print(max)




