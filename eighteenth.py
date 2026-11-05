n = int(input())
perf = 0
for i in range(1, n):
    if n % i == 0:
        perf += i
if perf == n:
    print("true")
else:
    print("false")