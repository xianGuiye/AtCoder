N,M = [int(x) for x in input().split()]
List = [list(map(int,input().split())) for i in range(M)]
left = List[0][0]
right = List[0][1]
for j in range(M-1):

    l = List[j+1][0]
    r = List[j+1][1]

    if l > left:
        left = l
    if r < right:
        right = r
    if right < left:
        print(0)
        break
else:
    print(right-left+1)
