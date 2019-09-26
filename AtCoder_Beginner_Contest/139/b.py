import math
A,B = [int(i) for i in input().split()]

#総差込口は電源タップを1つ使うごとにA-1個増えていくからB<=(A-1)C+1のCを求めれば良い
print(math.ceil((B-1)/(A-1)))
