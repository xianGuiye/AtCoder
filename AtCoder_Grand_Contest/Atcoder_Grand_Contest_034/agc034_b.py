s = input()
count = 0

margin = 0
length = len(s)
while length > 0:

    if s[length-1] == "A":
       count += margin
       s = s[:length-1]
    elif s[length-2:] == "BC":
        margin += 1
        s = s[:length-2]
    else:
        s = s[:length-1]
        margin = 0
    
    length = len(s)

print(count)

    

