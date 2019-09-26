N,X = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]
count = 1
Sum = 0

for i in range(N):
    Sum += L[i]

    #現在の座標がXを超えていれば終了する
    if Sum > X:
        break
    count += 1

print(count)
    
