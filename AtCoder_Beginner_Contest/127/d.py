N,M = [int(x) for x in input().split()]
Card = list(map(int, input().split())) 
List = [list(map(int,input().split())) for i in range(M)]
Card.sort()
List.sort(key=lambda x: x[1],reverse=True)
Card_sum = sum(Card)
iterator = 0
for i in range(M):
    Exit = False
    
    #List[i][1]に書き換えられる枚数を代入する
    loop = List[i][0]
    
    #参照される添字がloopの分を足すとオーバーすることがあるから例外を設定する
    try:
        if Card[iterator+loop-1] <= List[i][1]:
            Card_sum += loop*List[i][1] - sum(Card[iterator:iterator+loop])
            iterator += loop
            continue
    except IndexError:
        pass

    for j in range(min(loop,N-iterator)):
        if Card[iterator+j] > List[i][1]:
        
        #カードと入れ替えカードリストはソートされており,一度でも入れ替えが行われなければそれ以後入れ替えは一切行われない
            Exit = True
            break
    
        Card_sum += List[i][1] - Card[iterator+j]

    if Exit:
        break

print(Card_sum)
