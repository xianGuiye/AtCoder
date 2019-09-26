n = int(input())
S = [int(x) for x in input().split()]
m = int(input())
grid = []
for i in range(m):
    array = list(map(int, input().strip().split()))
    grid.append(array)

result = []


for i in range(m):
    tmp = []
    for j in range(n):
        tmp.insert(S[grid[i][j]-1],str(S[j]))
    result.append(''.join(tmp))

print(result)
