import time
N,K = [int(x) for x in input().split()]
a = []
a = list(map(int, input().split()))

start = time.time()
b = []
answer = 0
for i in range(N):
    b.append(a.pop(0))
    sum = 0
    c = len(b)
    for j in reversed(range(c)):
        sum += int(b[j])
        if sum >= K:
            answer += j + 1
            break

print(answer)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
