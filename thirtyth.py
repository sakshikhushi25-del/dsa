n = int(input())
i = 0
a = 0
b = 1
while i < n:
    print(a, end=" ")
    c = a+b
    a = b
    b = c
    i += 1