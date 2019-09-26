S = list(input())
T = list(input())
count = 0

#一文字ずつ一致しているか走査する
for i in range(3):
    if S[i] == T[i]:
        count += 1
print(count)
