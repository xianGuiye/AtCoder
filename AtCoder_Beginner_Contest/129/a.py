P,Q,R = [int(x) for x in input().split()]

#A,B,C間を回遊する最も短いコース
print(min((P+Q),(Q+R),(R+P)))
