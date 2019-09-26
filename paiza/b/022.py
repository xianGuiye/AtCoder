M,N,K = [int(x) for x in input().split()]
a = [int(input()) for i in range(K)]
supporter = [N] + [0] * M 

#supporter[i]は立候補者iを支持している有権者の人数を表す
#i=0は誰も支持していない人数を表す


for a_item in a:
    count = 0
    for x in range(len(supporter)):
        #立候補者a_itemが演説するとき,他の立候補者の支持者状況を確認する
        if x != a_item and supporter[x] != 0:
            count += 1
            supporter[x] -= 1
    supporter[a_item] += count

max_temp = []
max_value = sorted(supporter[1:],reverse=True)[0]

#支持者が最も多い立候補者が複数いるかを確認する
for y in range(1,M+1):
    if supporter[y] == max_value:
        max_temp.append(y)

for temp_item in max_temp:
    print(temp_item)
