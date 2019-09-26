S = int(input())
yymm = True
mmyy = True


if S >= 1300 or S < 100:
    mmyy = False
if S%100 >= 13 or S%100 == 0:
    yymm = False

if yymm == True:
    if mmyy == True:
        print("AMBIGUOUS")
    else:
        print("YYMM")
else:
    if mmyy == True:
        print("MMYY")
    else:
        print("NA")

