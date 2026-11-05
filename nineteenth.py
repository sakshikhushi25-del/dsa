n = int(input())
i = 0
dec = 0
while n > 0:
    a = n % 10
    dec = dec + a*(2**i)
    n = n // 10
    i = i+1
print(dec)