A,B = [int(x) for x in input().split()]

#5歳以下は無料,6~12歳は半額,それ以上は満額かかる
if A <= 5:
    print(0)
elif 6 <= A and A <= 12:
    print(int(B/2))
else:
    print(B)

