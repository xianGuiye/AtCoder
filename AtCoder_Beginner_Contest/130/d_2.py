import time
N,K = [int(x) for x in input().split()]
a = []
a = list(map(int, input().split()))

start = time.time()
b = []
answer = 0
for i in range(N):
    b.append(a.pop(0))
    c = len(b)
    while sum >= K:
        b.pop(0)
        
print(answer)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
