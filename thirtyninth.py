arr = list(map(int,input().split()))
counte = 0
counto = 0
for i in arr:
    if i % 2 == 0:
        counte += 1
    else:
        counto += 1
print("Even:", counte, "Odd:", counto)