N,X = [int(i) for i in input().split()]
W = []
for j in input().split():
    W.append(j)

count = 1
Sum = 0
while Sum <= X and count < N + 2:
    if count < N + 1:
        Sum += int(W.pop(0))
    count += 1
print(count-1)
    
