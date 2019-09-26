def Size(k):
    return 6*pow(2,k-1) - 3

k,s,t = [int(x) for x in input().split()]
moji = ["A","B","C"]
l_layer = [k]
r_layer = [k+2]

for i in range(k-1):
    l_layer.append(l_layer[i] - 1)
    r_layer.append(l_layer[i+1] + Size(i+2) - 1)

left = k - 1
while l_layer[i] <= s and s <= r_layer[i]:
    left -= 1


