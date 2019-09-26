import math
N,D = [int(x) for x in input().split()]
X = [list(map(int,input().split())) for i in range(N)]
count = 0


for j in range(N-1):
    for k in range(j+1,N):
        tmp = 0

        #j番目の点とk番目の点の距離を求める
        for l in range(D):
            tmp += pow(X[j][l] - X[k][l],2)
        
        #1で割り切れることができれば整数である
        if math.sqrt(tmp) % 1 == 0:
            count += 1

print(count)
