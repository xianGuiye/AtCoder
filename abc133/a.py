N,A,B = [int(x) for x in input().split()]

#電車代A*N円とタクシー代B円のうち最小のものを出力する
print(min(A*N,B))
