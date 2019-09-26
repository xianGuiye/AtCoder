import math,sys
N,M = [int(x) for x in input().split()]
a = [int(input()) for j in range(M)]

#コンビネーションnCrを求める
def combination(n, r):
        return math.factorial(n)//(math.factorial(n - r) * math.factorial(r))

#1段ずつ登る方法と１段飛ばしで登る方法を混ぜた登り方の総数を計算する
def keisan(a,b):
    count = 0
    n = b - a - 2
    r = 0

    while n >= r:

        count += combination(n,r)
        n -= 1
        r += 1

    return count

result = 1

#壊れている段がないとき
if M == 0:
    result *= keisan(-1,N+1)
    print(int(result)%1000000007)
    sys.exit()

for i in range(M):    

    if i == 0:
        result *= keisan(-1,a[0])
        continue

    #階段の段が連続して壊れている場合は登れない
    if a[i] - a[i-1] == 1:
        result = 0
        break
    else:
        result *= keisan(a[i-1],a[i])
    

else:
    result *= keisan(a[M-1],N+1)

print(int(result)%1000000007)

