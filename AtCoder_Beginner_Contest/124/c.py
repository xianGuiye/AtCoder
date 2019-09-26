str = input()
S = list(str)
N = len(S)
count = 0

#10101...か01010...の2パターンあるが,ここでは01010...とするように考える
for x in range(N):
    if x % 2 == 0 and S[x] == "0":
        count += 1
    elif x % 2 == 1 and S[x] == "1":
        count += 1
#上記の2パターンは全てのタイルを入れ替えることで片方のパターンに塗り替えることができる
if count > N / 2:
    print(N - count)
else:
    print(count)


