N = int(input())
Str = list(input())
K = int(input())

chikan = Str[K-1] #置換対象外となる文字


for i in range(N):
    if Str[i] != chikan:
        Str[i] = '*'

Str = "".join(Str)
print(Str)

