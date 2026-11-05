n = int(input())
x = n
total = 0
while n > 0:
    a = n % 10
    total = total + a**3
    n = n//10
if total == x:
    print("True")
else:
    print("false")