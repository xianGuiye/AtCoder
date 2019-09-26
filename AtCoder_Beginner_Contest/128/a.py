A,P=[int(x) for x in input().split()]

#A個のリンゴはA*3個の欠片になるから初期値Pと足して2で割ればアップルパイの個数が求まる
print(int(((A*3)+P)/2))

