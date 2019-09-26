H,W = [int(x) for x in input().split()]
s = [list(input()) for x in range(H)]
count = 0
From = 0 #左からビームが来るとき→ 0,下なら→ 1,右なら→ 2,上なら→ 3
i = 0
j = 0

while 0 <= i and i < H and 0 <= j and j < W:
    count += 1
    
    #透過なら向きは変わらないのでFromは不変となる
    if s[i][j] == "_":
        if From == 0:
            j += 1
        elif From == 1:
            i -= 1
        elif From == 2:
            j -= 1
        else:
            i += 1
    #光は左から来れば上に反射する.下から来れば右に反射する.逆も然りである.
    elif s[i][j] == "/":
        if From == 0:
            i -= 1
            From = 1
        elif From == 1:
            j += 1
            From = 0
        elif From == 2:
            i += 1
            From = 3
        else:
            j -= 1
            From = 2

    #光は左から来れば下に反射する.上から来れば右に反射する.逆も然りである.
    else:
        if From == 0:
            i += 1
            From = 3
        elif From == 1:
            j -= 1
            From = 2
        elif From == 2:
            i -= 1
            From = 1
        else:
            j += 1
            From = 0
print(count)

