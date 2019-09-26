import sys
N = int(input())
p = [int(x) for x in input().split()]
count = 0

#順列が一度の入れ替えで昇順にできるときは「すでに昇順である」か「2箇所だけp[i]!=i+1」のどちらかである
for i in range(N-1):
    if p[i] == i + 1:
        continue
    else:
        count += 1
    
    #2箇所以上の相違があった場合は不可能として終了
    if count > 2:
        print("NO")
        sys.exit()
else:
    print("YES")

