N = int(input())
d = [int(x) for x in input().split()]
d.sort() #難易度順にソートする

#(N/2)-1番目の要素とN/2番目の要素の間であればどこに境界を持ってきてもリストを2等分できる
print(d[int((N/2))] - d[int((N/2) - 1)])

