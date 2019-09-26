N,M = [int(x) for x in input().split()]
Card = list(map(int, input().split())) 
List = [list(map(int,input().split())) for i in range(M)]
Card.sort()

for i in range(M):
    loop = List[i][0]
    for j in range(loop):
        if Card[0] > List[i][1]:
            break
        Card.pop(0)
        Card.append(List[i][1])
    Card.sort()

sum = 0
for k in range(N):
    sum += Card.pop(0)
print(sum)
