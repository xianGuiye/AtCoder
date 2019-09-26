import math
N,D = [int(x) for x in input().split()]

#一人の監視員は2*D+1本の木を監視ができるから重ならないように配置すれば最小人数で済む
print(math.ceil(N / (2*D+1)))

