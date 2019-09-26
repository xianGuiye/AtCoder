A,B = [int(x) for x in input().split()]

#AとBの差が2以上であれば大きい方を2回押す
if A >= B + 2:
  print(2*a - 1)
elif b >= a + 2:
  print(2*b - 1)

#AとBの差が2未満であればそれぞれ一回ずつ押す
else:
  print(a + b)
