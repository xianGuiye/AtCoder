N,M = [int(x) for x in input().split()]
Card = list(map(int, input().split())) 
List = [list(map(int,input().split())) for i in range(M)]
NumberList = []

for i in range(M):
    loop = List[i][0]
    number = List[i][1]
    for j in range(loop):
        NumberList.append(number)

for i in range(N):
    NumberList.append(Card.pop(0))

NumberList.sort(reverse=True)
print(NumberList)
sum = 0
for k in range(N):
    sum += NumberList.pop(0)
print(sum)
