N,L = [int(x) for x in input().split()]
A = list(range(L,L+N))
Min = 100 #味の最小値はとりあえず最大値100で初期化しておく

#絶対値が最小のものをすべてのりんごについて探す
for i in A:
    if Min >= abs(i):
        youso = i 
        Min = abs(i)

A.remove(youso)
print(sum(A))
        
