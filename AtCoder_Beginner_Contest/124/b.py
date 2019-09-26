N = int(input())
H = (int(x) for x in input().split())
count = 0

#i番目の旅館が海を眺められるのはH[j]<=H[i](j<i)のとき
for i in range(N):
  for j in range(i):
    if H[i] < H[j]:
      break
#すべてのループが回れば眺められる旅館ということ
else:
    count+=1

print(count)
