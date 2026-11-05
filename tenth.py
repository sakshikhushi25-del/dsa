n = int(input())
a = n % 10
while n > 0:
    b = n // 10
    n = n // 10
print("first : ", n "last :", a)