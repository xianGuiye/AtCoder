r,D,x = [int(x) for x in input().split()]
tmp = x

#i年後の重さは(i-1年の重さ)*r-Dで与えられる
#以下は10年分出力する

for i in range(10):
    tmp = tmp * r - D
    print(tmp)


