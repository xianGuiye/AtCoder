N = int(input())
A = [int(input()) for x in range(N)]
M = sorted(A,reverse=True)
M1 = M[0] #リストの中で最も大きい要素
M2 = M[1] #リストの中で2番目に大きい要素


for i in range(N):
    #2番目に大きい要素以下の要素が選択されているときは最大のM1を出力する
    if A[i] <= M2:
        print(M1)
    #最も大きい要素が選択されているときは2番目に大きいM2を出力する
    else:
        print(M2)

