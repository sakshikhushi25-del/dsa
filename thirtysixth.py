arr = list(map(int,input().split()))
add = 0
for i in arr:
    add += i
avg = add/len(arr)
print("Sum:", add, "Avg:", avg)