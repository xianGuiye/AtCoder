N,M = [int(x) for x in input().split()]
List = [list(map(int,input().split())) for i in range(M)]
left = List[0][0]
right = List[0][1]


#すべてList[i]においてList[i][0]<=k,k<=List[i][1]となるようなkの個数を求める
for j in range(1,M-1):

    l = List[j][0]
    r = List[j][1]

    left = max(l,left)
    right = min(r,right)
    
    if right < left:
        print(0)
        break
else:
    print(right-left+1)
