H,W = [int(x) for x in input().split()]
S = [input() for x in range(H)]
a = []
b = []

for i in range(H):
    a.append(S[i].count("."))
for j in range(W):
    b.append(0)
    for i in range(H):
        if S[i][j] == ".":
            b[j] += 1
            
print(max(a))
print(max(b))
print(max(a)+max(b)-1)




