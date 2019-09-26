import sys,collections
S = list(input())
S_Collection = collections.Counter(S) #Sの各文字の出現回数

#S_Collectionの内容が[2,2]であれば各文字は2回ずつ出現することになる
if list(S_Collection.values()) == [2,2]:
    print("Yes")
    sys.exit()
print("No")

