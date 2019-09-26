W,H,x,y = [int(i) for i in input().split()]
hantei = 0
if x == W/2 and y == H/2:
    hantei = 1
else:
    hantei = 0
print("{0} {1}".format(W*H/2,hantei))
    
