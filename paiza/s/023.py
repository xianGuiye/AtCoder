import copy
#値の入力を行う
N,M,Q = [int(x) for x in input().split()]
like = []
for i in range(M):
    array = list(map(int, input().strip().split()))
    like.append(array)
op = []
for i in range(Q):
    array = list(map(str, input().strip().split()))
    op.append(array)

#同好会に所属しない村人を格納する配列:non_com
non_com = []
for k in range(N): 
    non_com.append(k+1)

#同好会に所属する村人を格納する配列:com
com = []

#iとjの友好度をList[i][j]で表すような配列(ただしi<j)
List = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    List[like[i][0]-1][like[i][1]-1] = like[i][2]


for i in range(Q):
    #同好会に所属/退会した情報からcomおよびnon_comを更新する
    if op[i][0] == "+":
        non_com.remove(int(op[i][1]))
        com.append(int(op[i][1]))
    else:
        non_com.append(int(op[i][1]))
        com.remove(int(op[i][1]))
    com_tmp = copy.copy(com)
    like_tmp = []

    #comとnon_comの情報から全ての組み合わせにおける友好度を求めて格納
    while com_tmp != []:
        com_tmp_num = com_tmp.pop()
        non_com_tmp = copy.copy(non_com)
        while non_com_tmp != []:
            non_com_tmp_num = non_com_tmp.pop()
            if com_tmp_num <= non_com_tmp_num:
                like_tmp.append(List[com_tmp_num-1][non_com_tmp_num-1])
            else:
                like_tmp.append(List[non_com_tmp_num-1][com_tmp_num-1])

    #格納した友好度リストを降順にソートして一番初めの要素を出力する
    list.sort(like_tmp,reverse=True)
    if like_tmp != []:
        print(like_tmp[0])
    else:
        print(0)
    like_tmp.clear()
