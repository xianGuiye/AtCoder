import math
N,K = [int(x) for x in input().split()]
p = 0

#すべての初期値x(1~N)について確率を試算する
for x in range(1,N+1):

    #kは「何回表が出ればKに到達するか」を表す
    k = K/x
    if x < K:
        k_log = math.ceil(math.log2(k))

    #すでにKに到達しているため,現在の得点の時点でクリア→ 0回表が出ればよい
    else:
        k_log = 0
    
    p += 1/N/pow(2,k_log)

print(p)
