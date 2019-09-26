N = int(input())
S = input()
count = 0
count2 = 0
flag = False #黒の石を検出すればフラグが立つ.以後は白石は配置できない.

#前から黒石を白石に変えて行く場合の操作回数
for x in range(N):
    if S[x] == '#':
        flag = True
    if S[x] == '.' and flag == True:
        count += 1

flag = False

#後ろから白石を黒石を変えていく場合の操作回数
for x in range(N)[::-1]:
    if S[x] == '.':
        flag = True
    if S[x] == '#' and flag == True:
        count2 += 1

print(min(count,count2))

