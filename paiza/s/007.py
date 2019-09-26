occur = [0]*26

# カッコの倍数を全てかけ合わせたものを計算する関数
def cross_margin(margin_list):
    margin = 1
    for item in margin_list:
        margin *= int(item)
    return margin

#文字列を初めから走査して出現回数を求める関数
def calculate_occur(s,margin_list):
    tmp = "0"
    tmp_item = ""
    margin = cross_margin(margin_list)
    while s != []:
        item = s.pop(0)
        #文字"("がきたときはその倍数をマージンリストに加えて関数を呼び直す
        if item == "(":
            margin_list.append(tmp)
            calculate_occur(s,margin_list)
        #文字")"がきたときは一番手前のマージンをリストから外して関数を呼び直す
        elif item == ")":
            margin_list.pop()
            calculate_occur(s,margin_list)
        #数字がきたときは文字以外が来るまで連結し続ける(倍数となる)
        elif item.isdecimal():
            tmp += item             
        #文字がきたときはマージンと倍数をかけ合わせた分だけ出現回数にカウントする
        elif item.isalpha():
            if item == "a":
                occur[0] += max(int(tmp),1)*margin
            elif item == "b":
                occur[1] += max(int(tmp),1)*margin
            elif item == "c":
                occur[2] += max(int(tmp),1)*margin
            elif item == "d":
                occur[3] += max(int(tmp),1)*margin
            elif item == "e":
                occur[4] += max(int(tmp),1)*margin
            elif item == "f":
                occur[5] += max(int(tmp),1)*margin
            elif item == "g":
                occur[6] += max(int(tmp),1)*margin
            elif item == "h":
                occur[7] += max(int(tmp),1)*margin
            elif item == "i":
                occur[8] += max(int(tmp),1)*margin
            elif item == "j":
                occur[9] += max(int(tmp),1)*margin
            elif item == "k":
                occur[10] += max(int(tmp),1)*margin
            elif item == "l":
                occur[11] += max(int(tmp),1)*margin
            elif item == "m":
                occur[12] += max(int(tmp),1)*margin
            elif item == "n":
                occur[13] += max(int(tmp),1)*margin
            elif item == "o":
                occur[14] += max(int(tmp),1)*margin
            elif item == "p":
                occur[15] += max(int(tmp),1)*margin
            elif item == "q":
                occur[16] += max(int(tmp),1)*margin
            elif item == "r":
                occur[17] += max(int(tmp),1)*margin
            elif item == "s":
                occur[18] += max(int(tmp),1)*margin
            elif item == "t":
                occur[19] += max(int(tmp),1)*margin
            elif item == "u":
                occur[20] += max(int(tmp),1)*margin
            elif item == "v":
                occur[21] += max(int(tmp),1)*margin
            elif item == "w":
                occur[22] += max(int(tmp),1)*margin
            elif item == "x":
                occur[23] += max(int(tmp),1)*margin
            elif item == "y":
                occur[24] += max(int(tmp),1)*margin
            elif item == "z":
                occur[25] += max(int(tmp),1)*margin
            #文字の前に出てきていた倍数を初期化する
            tmp = "0"

s = list(input())
margin_list = [1]
calculate_occur(s,margin_list)
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(26):
    print(alphabets[i],end=" ")
    print(occur[i])


