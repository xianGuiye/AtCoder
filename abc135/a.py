A,B = [int(x) for x in input().split()]
K = (A+B)/2

#Kが1で割ることが可能なら整数である
if K%1 == 0:
    print(int((B + A) / 2))
else:
    print("IMPOSSIBLE")

