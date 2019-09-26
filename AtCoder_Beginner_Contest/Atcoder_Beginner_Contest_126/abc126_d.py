N = int(input())

grid = []
for i in range(N-1):
    array = list(map(int, input().strip().split()))
    grid.append(array)

print(array[1][2])

for i in range(N-1):
    if array[i][2]%2 == 0:
        break

print(array[1][2])

