import copy
N,H,W = [int(x) for x in input().split()]
grid = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    grid.append(array)

d = []
d_ = [[0 for i in range(N)] for j in range(N)]
 
for i in range(N):
    for j in range(i):
        x_d = 0
        y_d = 0
        x_d = min(abs(grid[j][0]-grid[i][0]),abs(grid[i][0]-grid[j][0]+W))
        y_d = min(abs(grid[j][1]-grid[i][1]),abs(grid[i][1]-grid[j][1]+H))
        d.append(x_d+y_d)
        d_[i][j] = x_d+y_d      
list.sort(d)
visited = []
total = 0

d_cp = d.copy()
d__cp = d_.copy()
while len(set(visited)) != N:
    index = 0
    tmp = 0
    for k in range(N):
        if d_cp[0] in d__cp[k]:
            index = d__cp[k].index(d_cp[0])
            tmp = k
    
    if ((tmp in visited) ^ (index in visited)) or visited == []: 
        total += d_cp[0]
        d.remove(d_cp[0])
        visited.append(tmp)
        visited.append(index)
        d_cp = d.copy()
        d__cp = copy.deepcopy(d_)
    else:
        d__cp[tmp][index] = 0
        d_cp.pop(0)
print(total)
    




    
