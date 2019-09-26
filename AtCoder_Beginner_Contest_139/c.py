N = int(input())
H = [int(i) for i in input().split()]
count = 0
max_c = 0
tmp = H[0]

for i in range(1,N):
    
    #H[i-1]<H[i]ならカウントをリセット
    if tmp < H[i]:
        if max_c < count:
            max_c = count
        count = 0

    #それ以外はカウントを増やしていく
    else:
        count += 1
    
    tmp = H[i]

#最終的に現在のカウントと過去の最大値max_cを比較して大きい方を出力する
print(max(max_c,count))
