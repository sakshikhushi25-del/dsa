arr = list(map(int, input().split()))
zero = 0
pos = 0
neg = 0
for i in arr:
    if i == 0:
        zero += 1
    if i < 0:
        neg += 1
    if i > 0:
        pos += 1
print("Zero:", zero, "Pos:", pos, "Neg:", neg)