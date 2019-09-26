N,K = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
count = 0
tmp = a[0]
index = 0

#配列の先頭の要素を含む最小の連番でKを超えるか走査する
for i in range(N):
    for j in range(index+1,len(a)):
        if tmp >= K:
            count += len(a) - j + 1
            index = j - 1
            break
        tmp += a[j]
    
    index -= 1 
    tmp -= a[0]
    a.pop(0)

print(count)
