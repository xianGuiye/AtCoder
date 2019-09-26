import sys
N = int(input())
a = [int(x) for x in input().split()]
b = []

#1~Nにおいてj(N/2<j)の倍数となるものは1つしか存在しないためボールの入れ方は一意に定まるため「いいボールの入れ方」はこの範囲にて存在することになるからj(j<=N/2)について調べれば良い
for i in reversed(range(int(N/2))):
    b = i
    stack = 0
    #Nまでの範囲にてi番目の箱(整数i+1が書かれた箱)に入るボールの総数%2を求める
    while b < N:
        stack += a[b]
        stack %= 2
        b += i+1
    a[i] = stack

c = sum(a)

#初期状態がすでに「いいボールの入れ方」であるとき
if c == 0:
    print(c)
    sys.exit()

print(c)
for j in range(N):
    if a[j] == 1:
        print(j+1, end=" ")
print()



