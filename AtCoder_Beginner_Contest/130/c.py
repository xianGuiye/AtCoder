W,H,x,y = [int(i) for i in input().split()]
hantei = 0

#どの点(x,y)が与えられても重心を通る線分で分割すれば面積を二等分できて,これが最大である
#点(x,y)が長方形の重心であるなら二分割する方法は無限にある
if x == W/2 and y == H/2:
    hantei = 1
else:
    hantei = 0

print(f"{W*H/2} {hantei}")
    
