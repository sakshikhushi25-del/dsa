arr = list(map(int, input().split()))
large = 0
small = arr[0]
for i in range(len(arr)):
    if arr[i] > large:
        large = arr[i]
    if arr[i] < small:
        small = arr[i]
print("Max:", large, "Min:", small)