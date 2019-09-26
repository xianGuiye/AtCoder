N,Y=[int(x) for x in input().split()]
x = Y/10000
y = x/5000
z = y/1000
MinN = x + y + z

if Y < 1000*N or 10000*N < Y or N < MinN:
    print("-1 -1 -1")
else:
    if x > N-minN:
        x -= N-minN
        y += 2*N-minN
    else:
        y += 2*x
        x = 0
        if 
                

#20 50000　のとき
#5 6(10)(14) a+b+c=N 10000a+5000b+1000c=Y
#1000(N-a-b)+5000b+10000a=Y
#4000b+9000a=Y-1000N
