N,K = [int(x) for x in input().split()]
S = list(input())

#K番目の文字を小文字に変える
S[K-1] = S[K-1].lower()

#リストを文字列に変換する
answer = ''.join(S)

print(answer)

