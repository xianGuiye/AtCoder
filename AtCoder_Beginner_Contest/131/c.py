import math

#引数xとyの最大公約数を求める関数
def Euclidean(x,y):
    if y == 0:
        return x
    else:
        return Euclidean(y,x%y)

A,B,C,D = [int(x) for x in input().split()]
count = B - A + 1
E = Euclidean(C,D) #EはCとDの最大公約数
F = int(C*D/E) #FはCとDの最小公倍数

C_ = B//C - (A-1)//C #AからBの間でCで割り切れるものの個数
D_ = B//D - (A-1)//D #AからBの間でDで割り切れるものの個数
C_and_D = B//F - (A-1)//F #AからBの間でFで割り切れる(CでもDでも割り切れる)ものの個数

#CでもDでも割り切れない個数 = 総数 - (Cで割り切れる個数 + Dで割り切れる個数 - CでもDでも割り切れる個数)
print(count - (C_ + D_ - C_and_D)) 

