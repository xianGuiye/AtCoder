import sys
N = int(input())
A = [list(map(int,input().split())) for x in range(N)]
A_ = sorted(A,key=lambda x: x[1]) #〆切が近いもの順にソートする
Sum = 0

#〆切が近いものから処理していく
for x in A_:
    Sum += x[0]
    #現在時刻が次のタスクの〆切を超過したときは不可能として終了
    if Sum > x[1]:
        print("No")
        sys.exit()

#すべてのタスクが〆切内に終えた場合は可能として出力
else:
    print("Yes")
