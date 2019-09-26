n = int(input())
p = [int(x) for x in input().split()]
count = 0

#それぞれの3要素の比較において, 昇順または降順にソートしても変化が無ければ真ん中の要素が2番目に大きいことになる
for i in range(1,n-1):
    p_3list = [p[i-1],p[i],p[i+1]]

    if p_3list == sorted(p_3list):
        count += 1
    elif p_3list == sorted(p_3list,reverse=True):
        count += 1

print(count)
