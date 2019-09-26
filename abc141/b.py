import sys
S = list(input())
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "R" or S[i] == "U" or S[i] == "D":
            continue
        else:
            print("No")
            sys.exit()
    else:
        if S[i] == "L" or S[i] == "U" or S[i] == "D":
            continue
        else:
            print("No")
            sys.exit()
else:
    print("Yes")

