H,W = [int(x) for x in input().split()]
A = [[0]*W]*H
B = [[]]
for i in range(H):
    A[i-1] = input()
count = 0
flag = True
while flag == True:
    flag = False
    count += 1
    for i in range(H):
        for j in range(W):

            if A[i-1][j-1] == "#":
                u = -1
                d = 1
                l = -1
                r = 1

                if i-1 == 0:
                    u = 0
                if i-1 == H-1:
                    d = 0
                if j-1 == 0:
                    l = 0
                if j-1 == W-1:
                    r = 0
            
                A[i-1+u][j-1] = "#"
                A[i-1+d][j-1] = "#"
                A[i-1][j-1+l] = "#"
                A[i-1][j-1+r] = "#"
                flag = True
print(count-1)



            
