N,A,B,C,D = [int(x) for x in input().split()]
S = input()
cross = False
minG = C
maxG = D

if C > D:
    minG = D
    maxG = C
    cross = True

S_wall = S[A-1:maxG]
S_even = S[B-1-1:minG+1]

wall = S_wall.find("##")
even = S_even.find("...")

if cross == False:
    if wall == -1:
        print("Yes")
    else:
        print("No")
else:
    if wall == -1:
        if even != -1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")




