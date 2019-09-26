from decimal import *
N = int(input())

#直感的に{1,2,...}の順列のそれぞれの要素について{2,3,...}を割ったときの余りの合計は{1%2,2%3,...N-1%N,N%1}となって{1,2,...,N-1,0}となるとき最大となるとわかる

print(int((Decimal(N-1)*Decimal(N))/Decimal(2)))
