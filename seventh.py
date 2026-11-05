n = int(input())
add = 0
while n > 0:
    a = n % 10
    add += a
    n = n // 10
print(add)