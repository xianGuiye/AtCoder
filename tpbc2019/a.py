A,B,C = [int(x) for x in input().split()]

#Cが2番目に大きければYesを返却する
if (A <= C and C <= B) or (B <= C and C <= A):
    print("Yes")
else:
    print("No")


