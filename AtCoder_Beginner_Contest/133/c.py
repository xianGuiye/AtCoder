L,R = [int(x) for x in input().split()]
tmp1 = int(L/2019)
tmp2 = int(R/2019)
diff = tmp2 - tmp1 

#diff >= 1 であることはLとRが2019以上の差があるということ
if diff >= 1:
    print(0)
else:
    tmp3 = 0
    Min = 2018
    
    #(i*j)mod2019をすべて探索して最小のものを求める
    for i in range(L%2019,R%2019-1):
        for j in range(i,R%2019):
            tmp3 = (i*(j+1))%2019
            if Min > tmp3:
                Min = tmp3
    print(Min)
            


