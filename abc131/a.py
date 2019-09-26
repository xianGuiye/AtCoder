import sys
S = input()
tmp = ""

for i in S:
    #一つ前の文字はtmpに格納されている
    if tmp == i:
        print("Bad")
        sys.exit()
    tmp = i
else:
    print("Good")

