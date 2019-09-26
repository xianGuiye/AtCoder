N,K = [int(x) for x in input().split()]
S = list(input())
point = N - 1 #初期の幸福な人数を最大の人数N-1に設定する
count = 0　

#初期状態の幸福な人数を計測する
for i in range(N-1):
    #隣が違う向きを向いている度に1点ずつ減点
    if S[i] != S[i+1]:
        point -= 1
        count += 1

#一回の反転で増やせる幸福な人数は高々2人だけであるから,N-1人を超えない範囲で反転可能回数Kと減点量を比較して条件分岐する
if K >= count/2:
    print(N-1)
elif K >= int(count/2):
    print(N-2)
else:
    print(point+2*K)


