T,B,U,D,L,R = [int(x) for x in input().split()]
N = int(input())
p = [int(input()) for x in range(N)]
now = p[0]
count = 0

for i in range(N-1):
    if (now == T and p[i+1] == B) or (now == B and p[i+1] == T):
        count += 2
    elif (now == U and p[i+1] == D) or (now == D and p[i+1] == U):
        count += 2
    elif (now == L and p[i+1] == R) or (now == R and p[i+1] == L):
        count += 2
    else:
        count += 1
    now = p[i+1]

print(count)
    
    
